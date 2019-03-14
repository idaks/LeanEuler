from ..lean_euler_helper_funcs import mkdir_p
from nxpd import draw
import networkx as nx
import os
from collections import defaultdict
from PW_explorer.pwe_helper import pw_slicer


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


# Visualization function


def visualize(pw_rels_dfs, project_name, pws_to_use: list=None):
    """
    Assumees the pw_rels_dfs has been sliced to contain the pws of interest
    :param pw_rels_dfs:
    :param project_name:
    :param pws_to_use:
    :return:
    """


    def get_pw_ids(pw_rels_dfs):
        pw_ids = set([])
        for rel_name, rel_df in pw_rels_dfs.items():
            pw_ids = pw_ids.union(set(list(rel_df['pw'].unique())))
        return list(pw_ids)

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

        # Remove the redundant edges i.e. edges that go to ancestors of a parent
        for node in g.nodes:
            pred = list(g.predecessors(node))
            succ = list(g.successors(node))
            # print('node: {}'.format(node))
            for pred_ in pred:
                # print('predecessor: {}'.format(pred_))
                for succ_ in succ:
                    # print('successor: {}'.format(succ_))
                    if g.has_edge(pred_, succ_):
                        #  print('removing edge {} {}'.format(pred_, succ_))
                        g.remove_edge(pred_, succ_)

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

        # TODO Merged nodes may have redundant edges (direct edges to successors of parent)

        return g

    graphs = {}
    if not pws_to_use:
        pws_to_use = get_pw_ids(pw_rels_dfs)

    for pw_id in pws_to_use:
        dfs, _ = pw_slicer(pw_rels_dfs, None, [pw_id])
        graphs[pw_id] = visualize_pw(dfs['u_1'], dfs['pp_2'], dfs['po_2'], dfs['eq_2'], pw_id)

    return graphs
