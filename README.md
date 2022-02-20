# Notion graph view

The script helps to create graph view based on information it retrieves from notion database.
It takes the data and converts it to graphml format, so it could be viewed in [yEd](https://www.yworks.com/products/yed) afterwards.

It is created to analyze relations between databases and and draw them.
Also you can use it as a source of inspiration. 

![](./examples/radial_graph.png)

### Prerequisites

- Python 3

### Installation

```bash 
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Execution

- Add config.json to the root folder. The process of generating a token and collecting a database id is described [here](https://developers.notion.com/docs/getting-started)
```json
{
    "token": "token",
    "database_ids": [
        "id_1",
        "id_2",
        ...,
        "id_n"
    ]
}
```
- Execute:
```bash
python main.py
```
- Once zettelkasten.graphml is created open it in [yEd](https://www.yworks.com/products/yed) and apply a layout of your choice

![](./examples/layout.png)

- Profit

### To Do
- [ ] Let to set path and name of final file
- [ ] Exe
