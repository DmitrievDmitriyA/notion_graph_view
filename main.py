import json
from notion_requests import Client
import networkx as nx


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
        nodes.append(page["id"])

        # check links to previous cards and add edges
        # care only about previous links cause next links only duplicate them
        for node in page["properties"]["Previous card"]["relation"]:
            e = (page["id"], node["id"])
            edges.append(e)

    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    nx.write_graphml(graph, "./zettelkasten.graphml")


if __name__ == "__main__":
    main()
