import sys
import operator
import ijson


inp_file_name = sys.argv[1]
out_file_name = sys.argv[2]

kinds = {}
with open(inp_file_name, "rb") as inp:
    out = ijson.items(inp, 'item.page_hits.item.user')
    for num, item in enumerate(out):
        if item in kinds:
            kinds[item] += 1
        else:
            kinds[item] = 1

kinds = dict(sorted(kinds.items(), key=operator.itemgetter(1), reverse=True))
for k, v in kinds.items():
    print(k, " : ", v)
