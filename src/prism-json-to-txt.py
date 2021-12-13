import sys
import ijson
import os
states = {
    0: "UseStart",
    1: "registration",
    2: "challenge_sent",
    3: "login",
    4: "searching",
    5: "choose_char",
    6: "home",
    7: "gameplay",
    8: "rolls_fastforwarded",
    9: "move_viewed",
    10: "UseStop",
    11: "leaderboard",
    12: "profile",
    13: "gameover",
    14: "history",
    15: "game_history",
    16: "game_abandoned",
    17: "practice_select",
    18: "joined_queue",
    19: "logout",
    20: "move_made",
    21: "left_queue",
    22: "practice_char",
    23: "practice_game"
}

files = []
directory = r'in_files'
for filename in os.listdir(directory):
    files.append(os.path.join(directory, filename))

loop = -1
while loop < len(files) - 1:
    loop += 1
    outs = {}
    with open(files[loop], "rb") as inp:
        out = ijson.items(inp, 'item')
        max_k = 0
        for rrow in out:
            if rrow["k"] > max_k:
                max_k = rrow["k"]
            test_id = rrow["pctl"]["name"] + "k"+str(rrow["k"])
            if outs.get(test_id) is None:
                outs[test_id] = {"name": rrow["pctl"]["name"], "k": rrow["k"],
                                "start": rrow["timecut"]["start"], "end": rrow["timecut"]["end"], "min": rrow["timecut"]["mindays"], "results": []}
            value = rrow["result"]["value"]
            if value == None:
                value = "inf"
            outs[test_id]["results"].append([rrow["result"]["j"], value])
    for test in outs.keys():
        filename = outs[test]["name"]+"-k"+str(outs[test]["k"])+"-"+str(
            outs[test]["start"])+"-"+str(outs[test]["end"])+"-min"+str(outs[test]["min"])+".txt"
        with open("prism_outs\\"+str(outs[test]["start"])+"-"+str(outs[test]["end"])+"\\k"+str(max_k)+"\\"+filename, "w") as outputWriter:
            results = outs[test]["results"]
            for i in results:
                outputWriter.write("{0:20} {1}\n".format(states[int(i[0])], i[1]))
