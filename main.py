import secrets
import notion_database
import converter
import yEd


def main():
    token, database_ids = secrets.load_config()

    pages = []
    for database_id in database_ids:
        pages.append(notion_database.obtain_pages(token, database_id))

    yEd.create_graphML(*converter.notion_to_yEd(zet_pages, tags_pages))


if __name__ == "__main__":
    main()
