import secrets
import notion_database
import converter
import yEd


def main():
    token, zet_database_id, tags_database_id = secrets.load_config()

    zet_pages = notion_database.obtain_pages(token, zet_database_id)
    tags_pages = notion_database.obtain_pages(token, tags_database_id)

    yEd.create_graphML(*converter.notion_to_yEd(zet_pages, tags_pages))


if __name__ == "__main__":
    main()
