from notion_requests import Client
import requests
import json
from reject_duplicates import Dict


# Have to cache ids of already processed databases
# to remove duplicates from relations
PROCESSED_DATABASE_IDS = []


def obtain_relation_and_pages(token, database_ids):

    notion = Client(token)

    relations_per_database = []
    pages_per_database = []

    for database_id in database_ids:
        relations_per_database.append(
            _obtain_relations(notion, database_id))
        pages_per_database.append(
            _obtain_pages(notion, database_id))
    return (relations_per_database, pages_per_database)


def _obtain_relations(notion, database_id):

    relations = Dict()

    # try to retrieve a database information
    response = None
    try:
        response = notion.databases.retrieve(database_id)
    except requests.exceptions.HTTPError as e:
        print(json.dumps(e.response.json(), indent=2))
        exit()

    # Obtain information about database relations from page properties
    # Property name is required to obtain information for graph construction
    for key, value in response['properties'].items():
        if value['type'] == 'relation':
            id = value['relation']['database_id']

            # Databases has cross-relations which means that if one of them
            # is already processed there is no point in processing another one.
            # It will cause duplication of relations.
            # That's why caching and this check is needed
            if id not in PROCESSED_DATABASE_IDS:
                try:
                    relations[id] = key
                except ValueError:
                    # duplicates are restricted
                    continue
    PROCESSED_DATABASE_IDS.append(response["id"])
    return relations


def _obtain_pages(notion, database_id):

    pages = []

    query = {
        'database_id': database_id,
        'sorts': [
            {
                'property': 'Created',
                'direction': 'descending'
            }
        ]
    }

    # Query data from the database
    # it returns a generator object since this api endpoint supports pagination
    for response in notion.databases.query(**query):
        pages.extend(response['results'])

    return pages
