

def notion_to_yEd(pages):
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

    return (nodes, edges)
