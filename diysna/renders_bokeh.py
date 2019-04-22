import math
import pandas as pd
import networkx as nx
from bokeh.models import Plot, Range1d, MultiLine, Circle, GraphRenderer, Oval
from bokeh.models.tools import ResetTool, PanTool, WheelZoomTool, HoverTool, PointDrawTool
from bokeh.palettes import Spectral4, Spectral8
from bokeh.plotting import figure
from bokeh.models.graphs import from_networkx, StaticLayoutProvider


def render_minimal_graph():
    print('rendering minimal graph')
    N = 8
    node_indices = list(range(N))

    plot = Plot(
        sizing_mode='stretch_both',
        x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
        tools="", toolbar_location=None)

    graph_renderer = GraphRenderer()

    graph_renderer.node_renderer.glyph = Oval(
        height=0.1, width=0.2, fill_color="fill_color", )

    graph_renderer.node_renderer.data_source.data = dict(
        index=node_indices,
        fill_color=Spectral8)
    graph_renderer.edge_renderer.data_source.data = dict(
        start=[0]*N,
        end=node_indices)

    # start of layout code (this is the part networkX helps to build!
    # the layout...)
    circ = [i*2*math.pi/8 for i in node_indices]
    x = [math.cos(i) for i in circ]
    y = [math.sin(i) for i in circ]

    graph_layout = dict(zip(node_indices, zip(x, y)))
    graph_renderer.layout_provider = StaticLayoutProvider(
        graph_layout=graph_layout)

    plot.axis.axis_line_width = 0
    plot.grid.grid_line_width = 0
    plot.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
    plot.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks
    plot.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
    plot.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
    plot.xaxis.major_label_text_color = None  # Remove label x axis
    plot.yaxis.major_label_text_color = None  # Remove label x axis
    plot.border_fill_color = None
    plot.outline_line_color = None
    plot.renderers.append(graph_renderer)
    return plot


def render_karate_graph():
    G = nx.karate_club_graph()

    SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "black", "red"
    edge_attrs = {}
    for start_node, end_node, _ in G.edges(data=True):
        edge_color = SAME_CLUB_COLOR if G.nodes[start_node][
            "club"] == G.nodes[end_node]["club"] else DIFFERENT_CLUB_COLOR
        edge_attrs[(start_node, end_node)] = edge_color

    nx.set_edge_attributes(G, edge_attrs, "edge_color")

    # Show with Bokeh
    plot = Plot(plot_width=400, plot_height=400,
                x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
    plot.title.text = "Graph Interaction Demonstration"

    node_hover_tool = HoverTool(
        tooltips=[("index", "@index"), ("club", "@club")])
    plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

    graph_renderer = from_networkx(
        G, nx.spectral_layout, scale=1, center=(0, 0))

    graph_renderer.node_renderer.glyph = Circle(
        size=15, fill_color=Spectral4[0])
    graph_renderer.edge_renderer.glyph = MultiLine(
        line_color="edge_color", line_alpha=0.8, line_width=1)
    plot.renderers.append(graph_renderer)
    return plot

# create a graph using networkX
# https://networkx.github.io/documentation/stable/tutorial.html


def render_custom_graph(nodes, edges):
    G = nx.Graph()

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    print(nx.info(G))
    # Show with Bokeh
    plot = Plot(plot_width=800, plot_height=600,
                x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
    plot.title.text = "Graph Interaction Demonstration"

    graph_renderer = from_networkx(
        G, nx.circular_layout)

    graph_renderer.node_renderer.glyph = Circle(
        size=15, fill_color=Spectral4[0])
    graph_renderer.edge_renderer.glyph = MultiLine(
        line_alpha=0.8, line_width=1)
    plot.renderers.append(graph_renderer)
    return plot


def render_from_fb_combined():
    print('rendering from facebook_combined.txt')
    df = pd.read_csv('facebook_combined.txt', sep=" ", header=None)
    G = nx.from_pandas_edgelist(df.head(1000), 0, 1)
    print(nx.info(G))

    plot = Plot(background_fill_color="white",
                plot_width=800, plot_height=600,
                x_range=Range1d(-0.5, 0.5), y_range=Range1d(-0.5, 0.5))

    graph_renderer = from_networkx(
        G, nx.spring_layout, scale=1, center=(0, 0))

    graph_renderer.node_renderer.glyph = Circle(
        size=15, fill_color=Spectral4[0])
    graph_renderer.edge_renderer.glyph = MultiLine(
        line_alpha=0.8, line_width=1)

    plot.add_tools(WheelZoomTool())
    plot.add_tools(ResetTool())
    plot.add_tools(PanTool())
    plot.add_tools(HoverTool(
        tooltips=[("user", "datracka"), ("url", "https://twitter.com/datracka")]))
    plot.add_tools(PointDrawTool(
        renderers=[], empty_value='black'))

    plot.axis.axis_line_width = 0
    plot.grid.grid_line_width = 0
    plot.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
    plot.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks
    plot.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
    plot.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
    plot.xaxis.major_label_text_color = None  # Remove label x axis
    plot.yaxis.major_label_text_color = None  # Remove label x axis
    plot.border_fill_color = None
    plot.outline_line_color = None

    plot.renderers.append(graph_renderer)

    return plot
