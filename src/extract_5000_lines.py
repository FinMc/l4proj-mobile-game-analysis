import sys
import operator
import ijson


inp_file_name = sys.argv[1]
out_file_name = sys.argv[2]


## Generate txts
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
    for action in one_user:
        print("{ ", end="")
        for key in action.keys():
            if key not in ["cred_hashed_pw", "message", "user", "cred_username"]:
                print(key + " : "+ action[key], end=", ")
        print("}")
