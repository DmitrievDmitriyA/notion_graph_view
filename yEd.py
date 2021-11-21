import pyyed


LETTER_WIDTH = 7
LETTER_HEIGHT = 15
WORDS_PER_LINE = 5


NODE_TYPE_COLOR = {
    'Concept': "#ccffcc",
    'Observation': "#99ccff",
    'Story': "#cc99ff",
    'Tag': "#ffcc99"
}

EDGE_TYPE_COLOR = {
    "Tag": "#ffcc99"
}


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


def create_graphML(nodes, edges, tags, tags_edges):

    graph = pyyed.Graph()

    for tag in tags:
        width, height, content = beautify(tag["name"])
        graph.add_node(tag["id"], shape_fill=NODE_TYPE_COLOR["Tag"], label=content, width=str(width), height=str(height))

    for node in nodes:
        width, height, content = beautify(node["content"])
        graph.add_node(node["id"], shape_fill=NODE_TYPE_COLOR[node["type"]], label=content, width=str(width), height=str(height))

    for edge in tags_edges:
        graph.add_edge(*edge, color=EDGE_TYPE_COLOR["Tag"])

    for edge in edges:
        graph.add_edge(*edge)

    graph.write_graph("./zettelkasten.graphml")
