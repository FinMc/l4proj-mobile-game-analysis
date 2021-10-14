import sys
import ijson

inp_file_name = sys.argv[1]
out_file_name = sys.argv[2]

# n = 5000
# with open(inp_file_name) as inp:
#     with open(out_file_name, "w") as out:
#         for i in range(5000):
#             out.write(inp.readline())

with open(inp_file_name) as inp:
    objects = ijson.items(inp, 'games.item')
    columns = list(objects)
    print(columns)