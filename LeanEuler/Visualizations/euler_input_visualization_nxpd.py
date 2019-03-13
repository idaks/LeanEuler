#!/usr/bin/env python3

import networkx as nx
import pandas as pd

NODE_COLORS = ['#CCFFCC', '#FFFFCC', '#f4bf42', '#6346d6']

GRAPH_STYLE = {
    'label': "Input Taxonomy",
    'fontsize': '16',
    'fontcolor': 'black',
    'bgcolor': '#ffffff',
    'rankdir': 'LR',
}

PARENT_EDGE_STYLE = {
    'arrowhead': 'normal',
    'style': 'solid',
    'color': 'black',
    'constraint': 'true',
    'penwidth': '1',
}

NODE_STYLE = {
    'fontcolor': 'black',
    'shape': 'box',
    'style': 'filled',
    'fontname': 'helvetica',
    'fillcolor': '#CCFFCC',
}

RELATION_EDGE_STYLE = {
    'style': 'dashed',
    'color': "#AA00FF",
    'constraint': 'true',
    'penwidth': '1',
    'dir': 'both',
    'arrowhead': 'normal',
    'label': '',
}


def get_node_style(node_color):
    k = NODE_STYLE.copy()
    k.update({'fillcolor': node_color})
    return k


def get_rel_edge_style(rl: str):
    k = RELATION_EDGE_STYLE.copy()
    k.update({'label': rl})
    return k


def add_tax_to_graph(G, root, node_style, tax_id):

    def add_children(G, sub_root, tax_styles):
        for child in sub_root.children:
            G.add_node(child.name, **node_style)
            if tax_id % 2 == 1:
                G.add_edge(child.name, sub_root.name, **PARENT_EDGE_STYLE, dir='forward')
            else:
                G.add_edge(sub_root.name, child.name, **PARENT_EDGE_STYLE, dir='back')
            add_children(G, child, tax_styles)

    G.add_node(root.name, **node_style)
    add_children(G, root, node_style)


def visualize_euler_input(rel_data: pd.DataFrame, taxes):
    G = nx.DiGraph(**GRAPH_STYLE)
    for i, (tax_name, tax_desc) in enumerate(taxes.items()):
        node_style = get_node_style(NODE_COLORS[i % len(NODE_COLORS)])
        root = tax_desc[tax_name].children[0]
        add_tax_to_graph(G, root, node_style, i)

    articulations = rel_data[rel_data['Relation'] != 'parent']
    for i, row in articulations.iterrows():
        G.add_edge(row['Node1'], row['Node2'], **get_rel_edge_style(row['Relation']))

    return G
