import secrets
import notion_database
import converter
import yEd


def main():
    token, database_ids = secrets.load_config()

    pages_per_database = []
    for database_id in database_ids:
        pages_per_database.append(notion_database.obtain_pages(token, database_id))

    yEd.create_graphML(converter.notion_to_yEd(pages_per_database)) # TODO: return tuple


if __name__ == "__main__":
    main()
