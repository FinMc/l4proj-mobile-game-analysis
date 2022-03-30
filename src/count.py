"""
Get the count of every user in the data set, used for initial data set understanding
"""
import ijson
with open("vertical_data.json", "rb") as inp:
    out = ijson.items(inp, 'item.page_hits.item')
    users = {}
    for line in out:
        if users.get(line["kind"]):
            users[line["kind"]] += 1
        else:
            users[line["kind"]] = 1
    print(users)