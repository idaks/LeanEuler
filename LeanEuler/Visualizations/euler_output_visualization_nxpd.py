import networkx as nx
from PW_explorer.pwe_helper import pw_slicer, rel_slicer
from PW_explorer.run_clingo import run_clingo
from PW_explorer.load_worlds import load_worlds
from PW_explorer.export import PWEExport


def get_styles(project_name, pw_id):
    return {
        'graph': {
            'label': '{}_pw_{}'.format(str(project_name), str(pw_id)),
            'fontsize': '16',
            'fontcolor': 'black',
            'bgcolor': '#ffffff',
            'rankdir': 'RL',
        },
        'node_styles': {
            'node_equal': {
                'shape': 'box',
                'style': '"filled,rounded"',
                'fontname': 'helvetica',
                'fillcolor': '#EEEEEE',
                'fontcolor': 'black',
            },
        },
        'edge_styles': {
            'overlap_edge': {
                'arrowhead': 'none',
                'style': 'dotted',
                'constraint': 'false',
                'penwidth': '1',
                'color': '#ce2118',
            },
            'proper_part_edge': {
                'arrowhead': 'normal',
                'style': 'solid',
                'color': 'black',
                'constraint': 'true',
                'penwidth': '1',
            },
        }
    }

# Utility functions


def remove_quotes(x):
    if x[0] == '"':
        x = x[1:]
    if x[-1] == '"':
        x = x[:-1]
    return x


def generate_node_style(fillcolor, fontcolor='black', shape='box', style='filled', fontname='helvetica'):
    return dict(fillcolor=fillcolor, fontcolor=fontcolor, shape=shape, style=style, fontname=fontname)


# Disjoint Sets Utility Functions

def get_parent(node, djs):
    if djs[node] == node:
        return node
    parent = get_parent(djs[node], djs)
    djs[node] = parent
    return parent


def union(node1, node2, djs):
    node1 = get_parent(node1, djs)
    node2 = get_parent(node2, djs)
    if node1 != node2:
        djs[node2] = node1
    return node1


def setup_djs(djs):
    for child, parent in djs.items():
        djs[child] = get_parent(child, djs)

# Nodes merge function


def merge_nodes(G,nodes, new_node, attr):
    G_ = G
    for i in range(1, len(nodes)):
        G_ = nx.contracted_nodes(G_, nodes[0], nodes[i], self_loops=False)  # Only works for two nodes at a time apparently
    G__ = nx.relabel.relabel_nodes(G_, {nodes[0] : new_node})
    G__.nodes[new_node].update(attr)
    return G__


def remove_redundant_edges(orig_pw_obj, edges_rel_name: str='pp_2'):
    _,_, sliced_orig_pw_obj = rel_slicer(None, None, [orig_pw_obj], [edges_rel_name])
    orig_pp_facts = PWEExport.export_as_asp_facts(sliced_orig_pw_obj, include_pw_ids=False)
    rel_name = edges_rel_name.rsplit('_', maxsplit=1)[0]  # Without arity
    output_rel_name = 'useful_e'
    redundancy_removal_rules = ['% define child(CHILD, PARENT)',
                                'child(X,Y) :- {}(X,Y).'.format(rel_name),
                                'child(X,Y) :- {}(X,Z), child(Z,Y).'.format(rel_name),
                                'redundant_child(X,Y) :- child(X,Y), child(X,Z), child(Z,Y), X!=Y, Y!=Z, X!=Y.',
                                '{}(X,Y) :- child(X,Y), not redundant_child(X,Y).'.format(output_rel_name),
                                '#show {}/2.'.format(output_rel_name),
                                ]
    useful_pp_clingo_soln, _ = run_clingo(orig_pp_facts+redundancy_removal_rules)
    useful_pp_dfs, _, _ = load_worlds(useful_pp_clingo_soln)  # TODO: Add silent option once it's added to PWE
    useful_pp_dfs, _ = pw_slicer(useful_pp_dfs, None, [1])
    return useful_pp_dfs['{}_2'.format(output_rel_name)]

# Visualization function


def visualize(pw_rels_dfs, project_name, pws_to_use: list):
    """
    Assumees the pw_rels_dfs has been sliced to contain the pws of interest
    :param pw_rels_dfs:
    :param project_name:
    :param pws_to_use:
    :return:
    """

    def visualize_pw(units_df, proper_part_edges_df, partial_overlap_df, equivalent_nodes_df, pw_id):

        NODE_COLORS = ['#CCFFCC', '#FFFFCC', '#f4bf42', '#6346d6']
        NODE_COLORS_USED = 0
        styles = get_styles(project_name, pw_id)
        g = nx.DiGraph(**styles['graph'])

        # Add all the units to the graph
        for idx, row in units_df.iterrows():
            node_name = remove_quotes(row['x1'])
            tax = node_name.split('_')[0]
            if tax not in styles['node_styles']:
                new_node_style = generate_node_style(NODE_COLORS[NODE_COLORS_USED])
                NODE_COLORS_USED += 1
                styles['node_styles'][tax] = new_node_style
            g.add_node(node_name, **styles['node_styles'][tax])

        # Add proper part edges
        for idx, row in proper_part_edges_df.iterrows():
            g.add_edge(remove_quotes(row['x1']), remove_quotes(row['x2']), **styles['edge_styles']['proper_part_edge'])

        # Add partial overlap edges
        for idx, row in partial_overlap_df.iterrows():
            n1 = remove_quotes(row['x1'])
            n2 = remove_quotes(row['x2'])
            if not g.has_edge(n2, n1):
                g.add_edge(n1, n2, **styles['edge_styles']['overlap_edge'])

        # Find the equivalent sets
        nodes = list(g.nodes)
        dj_sets = dict(zip(nodes, nodes))
        for idx, row in equivalent_nodes_df.iterrows():
            n1 = remove_quotes(row['x1'])
            n2 = remove_quotes(row['x2'])
            if n1 == n2:
                continue
            else:
                union(n1, n2, dj_sets)
        setup_djs(dj_sets)

        final_djs = {}
        for child, parent in dj_sets.items():
            if parent not in final_djs:
                final_djs[parent] = set([])
            final_djs[parent].add(child)
        final_djs = list(map(list, final_djs.values()))

        final_djs = list(filter(lambda x: len(x) > 1, final_djs))

        # Merge equivalent nodes
        for final_djs_ in final_djs:
            g = merge_nodes(g, final_djs_, '\n'.join(final_djs_), styles['node_styles']['node_equal'])

        return g

    graphs = {}

    for pw in pws_to_use:
        dfs, _ = pw_slicer(pw_rels_dfs, None, [pw.pw_id])
        proper_part_edges = remove_redundant_edges(pw, edges_rel_name='pp_2')
        graphs[pw.pw_id] = visualize_pw(dfs['u_1'], proper_part_edges, dfs['po_2'], dfs['eq_2'], pw.pw_id)

    return graphs
