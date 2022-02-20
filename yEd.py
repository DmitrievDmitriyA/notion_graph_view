import pyyed


LETTER_WIDTH = 7
LETTER_HEIGHT = 15
WORDS_PER_LINE = 5


NODE_TYPE_COLOR = [
    "#B9FBC0",
    "#98F5E1",
    "#8EECF5",
    "#90DBF4",
    "#A3C4F3",
    "#CFBAF0",
    "#F1C0E8",
    "#FFCFD2",
    "#FDE4CF",
    "#FBF8CC"
]

EDGE_TYPE_COLOR = [
    "#93C798",
    "#78C2B2",
    "#70BBC2",
    "#72AEC2",
    "#809ABF",
    "#A291BD",
    "#BF99B8",
    "#CCA5A8",
    "#C9B6A5",
    "#C7C4A1",
]


# Helps to format text for node rendering in yEd
def beautify(text):
    words = text.split()

    line = []
    strings = []

    for i in range(len(words)):
        word = words[i]

        line.append(word)

        # Next if statement helps to form a new string and add indention.
        # Second condition checks if the algorithm reached list's end ->
        # have to force it to append the line
        if len(line) == WORDS_PER_LINE or i == len(words)-1:
            new_string = ' '.join(line)
            new_string += '\n'
            strings.append(new_string)
            line = []

    # Simple calculations to adjust node's size
    width = max([len(string) for string in strings]) * LETTER_WIDTH
    height = len(strings) * LETTER_HEIGHT

    # Form the string to put in the node
    content = ""
    for string in strings:
        content += string

    return (width, height, content)


def create_graphML(nodes_per_database, edges_per_database):

    graph = pyyed.Graph()

    for index, nodes in enumerate(nodes_per_database):
        for node in nodes:
            width, height, content = beautify(node["name"])
            graph.add_node(node["id"], shape_fill=NODE_TYPE_COLOR[index], label=content, width=str(width), height=str(height))

    for index, edges in enumerate(edges_per_database):
        for edge in edges:
            graph.add_edge(*edge, color=EDGE_TYPE_COLOR[index])

    graph.write_graph("./zettelkasten.graphml")
