from os import curdir
import sys
import operator
import ijson
import json
from datetime import datetime


inp_file_name = sys.argv[1]
out_file_name = sys.argv[2]


# Generate txts
# kinds = {}
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item.page_hits.item.user')
#     for num, item in enumerate(out):
#         if item in kinds:
#             kinds[item] += 1
#         else:
#             kinds[item] = 1
# kinds = dict(sorted(kinds.items(), key=operator.itemgetter(1), reverse=True))
# for k, v in kinds.items():
#     print(k, " : ", v)


with open(inp_file_name, "rb") as inp:
    out = ijson.items(inp, 'item.page_hits.item')
    one_user = (o for o in out if o['user'] == "Manakish")
    outfile = [{"deviceid": "1", "sessions": []}]
    cur_session = []
    
    for action in one_user:
        cur_session_time = datetime.strptime(action["time"], "%Y-%m-%d %H:%M:%S.%f")
        break
    for action in one_user:
        current_action_time = datetime.strptime(action["time"], "%Y-%m-%d %H:%M:%S.%f")
        
        #If more than 30mins between action, different session
        if divmod((current_action_time - cur_session_time).total_seconds(), 60)[0] > 30:
            outfile[0]["sessions"].append(cur_session)
            cur_session = []
            cur_session_time = current_action_time

        cur_session.append({"timestamp": action["time"], "data": action["kind"]})


with open(out_file_name, 'w', encoding='utf-8') as f:
    json.dump(outfile, f, ensure_ascii=False, indent=4)
