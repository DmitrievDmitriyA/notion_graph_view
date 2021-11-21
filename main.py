import secrets
import notion_database
import converter
import yEd


def main():
    pages = notion_database.obtain_pages(*secrets.load_config())

    nodes, edges = converter.notion_to_yEd(pages)
    yEd.create_graphML(nodes, edges)


if __name__ == "__main__":
    main()
