import json
from notion_requests import Client
import pyyed
import formatting


NODE_TYPE_COLOR = {
    'Concept': "#ccffcc",
    'Observation': "#99ccff",
    'Story': "#cc99ff"
}


def decode(x):
    return [i for i in x]


def load_config():
    with open("config.json", "r") as read_file:
        return json.load(read_file)


def obtain_pages(config):
    notion_key = config["key"]
    notion_database_id = config["database_id"]

    notion = Client(notion_key)

    query = {
        'database_id': notion_database_id,
        'sorts': [
            {
                'property': 'Created',
                'direction': 'descending'
            }
        ]
    }

    pages = []

    # query a database
    # it returns a generator object since this api endpoint supports pagination
    for response in notion.databases.query(**query):
        pages.extend(response['results'])

    return pages


def main():
    config = load_config()
    pages = obtain_pages(config)

    nodes = []
    edges = []

    for page in pages:
        # add the page to nodes
        nodes.append({
            "id": page["id"],
            "type": page["properties"]["Type"]["select"]["name"],
            "content": page["properties"]["Name"]["title"][0]["text"]["content"]
            })

        # check links to previous cards and add edges
        # care only about previous links cause next links only duplicate them
        for node in page["properties"]["Previous card"]["relation"]:
            e = (page["id"], node["id"])
            edges.append(e)

    graph = pyyed.Graph()

    for node in nodes:
        width, height, content = formatting.beautify(node["content"])

        graph.add_node(node["id"], shape_fill=NODE_TYPE_COLOR[node["type"]], label=content, width=str(width), height=str(height))

    for edge in edges:
        graph.add_edge(*edge)

    graph.write_graph("./zettelkasten.graphml")


if __name__ == "__main__":
    main()
