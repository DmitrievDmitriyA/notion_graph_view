

def notion_to_yEd(relations_per_database, pages_per_database):

    nodes_per_database = []
    edges_per_database = []

    for index, pages in enumerate(pages_per_database):
        relations = relations_per_database[index]
        nodes, edges = _convert_database(relations, pages)
        nodes_per_database.append(nodes)
        edges_per_database.append(edges)

    return nodes_per_database, edges_per_database


def _convert_database(relations, pages):
    nodes = []
    edges = []

    for page in pages:
        # obtain id and name of every page to form a node
        try:
            nodes.append({
                "id": page["id"],
                "name": page["properties"]["Name"]["title"][0]["text"]["content"]
            })
        except IndexError as e:
            print("One of your notes do not have title. Page id: " + page["id"])

        for id, name in relations.items():
            for relation in page["properties"][name]["relation"]:
                e = (page["id"], relation["id"])
                edges.append(e)

    return (nodes, edges)
