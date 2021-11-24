import sys
import ijson
states = {
    0: "UseStart",
    1: "registration",
    2: "challenge_sent",
    3: "login",
    4: "refresh",
    5: "searching",
    6: "choose_char",
    7: "home",
    8: "gameplay",
    9: "rolls_fastforwarded",
    10: "move_viewed",
    11: "UseStop",
    12: "leaderboard",
    13: "profile",
    14: "gameover",
    15: "history",
    16: "game_history",
    17: "game_abandoned",
    18: "practice_select",
    19: "joined_queue",
    20: "logout",
    21: "move_made",
    22: "left_queue",
    23: "practice_char",
    24: "practice_game"
}

loop = 0
while loop < len(sys.argv) - 1:
    loop += 1
    outs = {}
    with open(sys.argv[loop], "rb") as inp:
        out = ijson.items(inp, 'item')
        k = 0
        start = -1
        end = -1
        mind = 0
        for i in out:
            k = i["k"]
            start = i["timecut"]["start"]
            end = i["timecut"]["end"]
            mind = i["timecut"]["mindays"]
            break

        for rrow in out:
            test_id = rrow["pctl"]["name"] + "k"+str(rrow["k"])
            if outs.get(test_id) is None:
                outs[test_id] = {"name": rrow["pctl"]["name"], "k": k,
                                 "start": start, "end": end, "min": mind, "results": []}
            value = rrow["result"]["value"]
            if value == None:
                value = -1
            outs[test_id]["results"].append([rrow["result"]["j"], value])
    for test in outs.keys():
        filename = outs[test]["name"]+"-k"+str(outs[test]["k"])+"-"+str(
            outs[test]["start"])+"-"+str(outs[test]["end"])+"-min"+str(outs[test]["min"])+".txt"
        with open(filename, "w") as out:
            results = outs[test]["results"]
            for i in results:
                out.write("{0:20} {1}\n".format(states[int(i[0])], i[1]))
