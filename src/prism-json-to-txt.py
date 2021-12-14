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
            test_id = rrow["pctl"]["name"]
            if outs.get(test_id) is None:
                res = {}
                for i in range(24):
                    res[i] = []
                outs[test_id] = {"name": rrow["pctl"]["name"], "k": rrow["k"],
                                "start": rrow["timecut"]["start"], "end": rrow["timecut"]["end"], "min": rrow["timecut"]["mindays"], "results": res}
            value = rrow["result"]["value"]
            if value == None:
                value = "inf"
            j_val = int(rrow["result"]["j"])
            outs[test_id]["results"][j_val].append(value)
    for test in outs.keys():
        filename = outs[test]["name"]+"-"+str(
            outs[test]["start"])+"-"+str(outs[test]["end"])+"-min"+str(outs[test]["min"])+".txt"
        with open("out_files\\"+str(outs[test]["start"])+"-"+str(outs[test]["end"])+"\\k"+str(max_k)+"\\"+filename, "w") as outputWriter:
            results = outs[test]["results"]
            for k,v in results.items():
                if len(v) == 2:
                    outputWriter.write(
                        "{:<25}{:<25}{:<}\n".format(states[int(k)], v[0], v[1]))
                else:
                    outputWriter.write("{:<25}{:<25}{:<25}{:<}\n".format(states[int(k)], v[0], v[1], v[2]))
