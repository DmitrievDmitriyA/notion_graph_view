from notion_requests import Client


def obtain_pages(token, database_id):

    notion = Client(token)

    query = {
        'database_id': database_id,
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

    return pages
