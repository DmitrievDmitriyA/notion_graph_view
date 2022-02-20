import secrets
import notion_database
import converter
import yEd


def main():
    token, database_ids = secrets.load_config()

    relations_per_database, pages_per_database = notion_database.obtain_relation_and_pages(token, database_ids)

    yEd.create_graphML(*converter.notion_to_yEd(relations_per_database, pages_per_database))


if __name__ == "__main__":
    main()
