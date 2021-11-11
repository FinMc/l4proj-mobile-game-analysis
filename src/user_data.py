import sys
import ijson
from datetime import datetime

inp_file_name = sys.argv[1]

with open(inp_file_name, "rb") as inp:
    out = ijson.items(inp, 'item')

    users = []
    for user in out:
        first_time = user['firstSeen']
        last_time = user['lastSeen']
        user = user['deviceid']

        time_dif = datetime.strptime(last_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(first_time, "%Y-%m-%d %H:%M:%S")

        users.append([user, time_dif.days])

    users.sort(key=lambda x: x[1])


    for user in users:
        print("{user}: {time}".format(user=user[0], time=user[1]))