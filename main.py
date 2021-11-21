import json
from notion_requests import Client


base_url = "https://api.notion.com/v1/databases/"
api_version = "2021-08-16"


def load_config():
    with open("config.json", "r") as read_file:
        return json.load(read_file)

def main():
    config = load_config()
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

    print(len(pages))


if __name__ == "__main__":
    main()