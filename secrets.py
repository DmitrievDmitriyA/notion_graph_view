import json


def load_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return (config["token"], config["database_ids"])
