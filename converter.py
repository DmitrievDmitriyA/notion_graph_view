

def notion_to_yEd(relations_per_database, pages_per_database):
    nodes_per_database = []
    edges_per_database = []

    for pages in pages_per_database:
        nodes = []
        for page in pages:
            # obtain id and name of every page to form a node
            nodes.append({
                "id": page["id"],
                "name": page["properties"]["Name"]["title"][0]["text"]["content"]
            })
        nodes_per_database.append(nodes)

    # # extract names from tags database
    # for page in tags_pages:
    #     tags.append({
    #         "id": page["id"],
    #         "name": page["properties"]["Name"]["title"][0]["text"]["content"]
    #     })

    # for page in zet_pages:
    #     # add the page to nodes
    #     nodes.append({
    #         "id": page["id"],
    #         "type": page["properties"]["Type"]["select"]["name"],
    #         "content": page["properties"]["Name"]["title"][0]["text"]["content"]
    #         })

        # # extract tags edges from the page
        # for tag in page["properties"]["Tags"]["relation"]:
        #     e = (page["id"], tag["id"])
        #     tags_edges.append(e)

        # # extract edges from the page
        # # check links to previous cards and add edges
        # # care only about previous links cause next links only duplicate them
        # for node in page["properties"]["Previous card"]["relation"]:
        #     e = (page["id"], node["id"])
        #     edges.append(e)

    return (nodes_per_database, edges_per_database)
