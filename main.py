import secrets
import notion_database
import converter
import yEd


def main():

    print("Reading config...")
    token, database_ids = secrets.load_config()
    print("Done")

    print("Obtaining data from notion...")
    relations_per_database, pages_per_database = notion_database.obtain_relation_and_pages(token, database_ids)
    print("Done")

    print("Converting notion data to yed format...")
    nodes_per_database, edges_per_database = converter.notion_to_yEd(relations_per_database, pages_per_database)
    print("Done")

    print("Creating graphML file...")
    yEd.create_graphML(nodes_per_database, edges_per_database)
    print("Done")


if __name__ == "__main__":
    main()
