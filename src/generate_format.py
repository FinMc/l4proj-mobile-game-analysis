"""
File used for getting the data set into the required format
Run from the command line and takes 2 parameters the name of the input file (the data set) and an output file name (example.json)

It collects takes a subset of users stored in users list and adds sessions of actions to them
The mappings dictionary changes the mapping to a subset of kinds and removes kinds not needing explored (such as the "konami" kind)

It then removes outlier session lengths
Then adds a UseStop to each user at the end of the file
"""

import sys
import ijson
import json
from datetime import datetime

users = [
    "l17r",
    "apropos0",
    "Frp97",
    "Ellen",
    "Deanerbeck",
    "cptKav",
    "ECDr",
    "creilly1",
    "Luca1802",
    "Nari",
    "timri",
    "Jamie",
    "DX13",
    "sstein",
    "tanini",
    "basta",
    "probablytom",
    "georgedo",
    "Tharry0",
    "Beccccca",
    "Fbomb",
    "kubajj",
    "cwallis",
    "elennon",
    "Martin",
    "alan",
    "creilly2",
    "dalinar",
    "Paddy",
    "DavetheRave",
    "Ezzey",
    "pool27",
    "aaaa",
    "BerrySauce",
    "Beth",
    "Jhannah",
    "Etess",
    "Andy",
    "sophie",
    "eggface",
    "alcam456",
    "EarlofSurl",
    "jack",
    "BetterThanU",
    "DoctorW",
    "walshy1066",
    "Nonni",
    "charlotte",
    "LLilliputian",
    "bladestoe",
    "Apollogize",
    "umachan",
    "Sabotage",
    "vinl",
    "chins",
    "jaymoney",
    "Marta",
    "norgart",
    "Rarno",
    "Significance",
    "jonildo",
    "deathseeker",
    "adamski5298",
    "Jules",
    "sidb",
    "BestWilliam",
    "rocinante",
    "Fudgecakes",
    "pigeon",
    "Gerr",
    "demander",
    "gummytribble",
    "probablyrob",
    "whiplash",
    "CalHaribo",
    "Anakhand",
    "tickler",
    "ruadh_mor",
    "versatile",
    "TheMaster",
    "Manakish",
    "Chrispie111",
    "asdf",
    "meow",
    "Sidthesloth",
    "Mageofheart",
    "OKaemii",
    "Michael",
    "Lotua",
    "Finlad",
    "Alliyana",
    "musicalSpear",
    "bobabell",
    "totem37",
    "CannyCaracal",
    "Benlog",
    "LewisDyer",
    "Paulverise",
    "The_big_Ali",
    "cats",
    "Master4444",
    "rowan",
    "Kjreid",
    "Hide_on_bush",
    "MhairiM",
    "bcslippers",
    "Jambo9000",
    "AMrza99",
    "Lavarider",
    "7Name1eSs",
    "Morntato",
    "Jules_217",
    "Silver",
    "astrospanner",
    "season2_test",
    "Shanys",
    "V4ssilios",
    "Atrps",
    "season2_soon",
    "Felix42",
    "mosam1311",
    "cute320215",
    "Vinc0310",
    "SGUNNER07",
    "Schmofe",
    "Fudgewolf",
    "Rilla_Treesp",
    "Kush",
    "yasmin_f",
    "Williscraft",
    "GraeChan",
    "wasyl2001",
    "Baepsae",
    "Damian",
    "GReat",
    "bijtis",
    "Hippodoodle",
    "Super_Ia",
    "Mando",
    "Porp",
    "Marv_911",
    "Elessar",
    "JoeExotic",
    "Kojack",
    "ruadh_beag",
    "AethelredVS",
    "MarkyMark74",
    "frick",
    "Connman96",
    "grobis",
    "zShi",
    "stru",
    "prof_Marcelo",
    "Suzs",
    "ChrialCentre",
    "claremcskim1",
    "MJWR",
    "simtsui",
    "sophc9797",
    "b00my",
    "BabaG",
    "Cm83",
    "OM222O",
    "JustJoe242",
    "Aloneinkyoto",
    "superrad",
    "Steeple",
    "oxocube",
    "Rooksoup",
    "cubbely",
    "Alhamed",
    "Doodad",
    "squidward",
    "Jack",
    "Marilu",
    "bingoboy",
    "Avodado14",
    "RandomUser",
    "Wormella",
    "Danny_Dog",
    "Trinder"
]

mappings = {
    "home_screen_logout": "logout",
    "registration": "registration",
    "challenge_sent": "challenge_sent",
    "login": "login",
    "joined_queue": "joined_queue",
    "searching_from_find_games": "searching",
    "searched_for_opponent": "searching",
    "home_to_choose_chars": "choose_char",
    "character_selected": "choose_char",
    "char_select_to_home": "home",
    "home_to_gameplay": "gameplay",
    "rolls_fastforwarded": "rolls_fastforwarded",
    "move_viewed": "move_viewed",
    "online_game_to_home": "home",
    "home_screen_to_profile": "profile",
    "tabbed_to_history": "history",
    "home_screen_to_leaderboard": "leaderboard",
    "game_history_checked": "game_history",
    "home_screen_to_practice_select": "practice_select",
    "practice_character_selected": "practice_char",
    "practice_selection_to_game": "practice_game",
    "practice_gameover_to_home": "home",
    "left_queue": "left_queue",
    "practice_char_select_to_home": "home",
    "game_abandoned": "game_abandoned",
    "practice_game_show_moves": "practice_game",
    "gameover_viewed": "gameover",
    "gameover_to_home": "home",
    "practice_game_to_home": "home",
    "opponent_searched_from_history": "searching",
    "profile_to_home": "home",
    "leaderboard_to_home": "home",
    "leaderboard_user_zoom": "leaderboard",
    "leaderboard_user_zoom_match_attempted": "leaderboard",
    "practice_gameover_play_again": "practice_game",
    "character_deselected": "choose_char",
    "practice_character_deselected": "practice_char",
    "move_made": "move_made"
}


inp_file_name = sys.argv[1]
out_file_name = sys.argv[2]

outfile = []
excluded = []
user_mapping = {}

user_counter = 0
with open(inp_file_name, "rb") as inp:
    out = ijson.items(inp, 'page_hits.item')

    for line in out:
        if line['user'] in users and mappings.get(line['kind']) is not None:
            user_id = user_mapping.get(line['user'])
            if user_id is None:
                user_mapping[line['user']] = user_counter
                user_id = user_counter
                user_counter += 1
                outfile.append({"deviceid": line['user'], "sessions": []})
            cur_session = []
            if len(outfile[user_id]['sessions']) == 0:
                cur_session_time = datetime(2000, 1, 1)  # Start of century
                prev_prev_kind = ""
                prev_kind = ""
                prev_prev_prev_kind = ""
                if "." in line["time"]:
                    outfile[user_id]["firstSeen"] = datetime.strptime(
                        line["time"], "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S")
                else:
                    outfile[user_id]["firstSeen"] = line["time"]
            else:
                # Get the latest session and the latest action in that session
                cur_session_time = datetime.strptime(
                    outfile[user_id]['sessions'][-1][-1]["timestamp"], "%Y-%m-%d %H:%M:%S")
                prev_kind = outfile[user_id]['sessions'][-1][-1]["data"]
                if len(outfile[user_id]['sessions'][-1]) >= 2:
                    prev_prev_kind = outfile[user_id]['sessions'][-1][-2]["data"]

            if "." not in line["time"]:
                current_action_time = datetime.strptime(
                    line["time"], "%Y-%m-%d %H:%M:%S")
            else:
                current_action_time = datetime.strptime(
                    line["time"], "%Y-%m-%d %H:%M:%S.%f")

            if mappings.get(line['kind']) not in [prev_kind, prev_prev_kind]:
                # If more than 30mins between action, different session
                if divmod((current_action_time - cur_session_time).total_seconds(), 60)[0] > 30:
                    outfile[user_id]["sessions"].append(
                        [{"timestamp": current_action_time.strftime("%Y-%m-%d %H:%M:%S"), "data": "UseStart"}])
                    if len(outfile[user_id]["sessions"]) > 1:
                        outfile[user_id]["sessions"][-2].append(
                            {"timestamp": cur_session_time.strftime("%Y-%m-%d %H:%M:%S"), "data": "UseStop"})

                outfile[user_id]["sessions"][-1].append(
                    {"timestamp": current_action_time.strftime("%Y-%m-%d %H:%M:%S"), "data": mappings[line["kind"]]})

            outfile[user_id]["lastSeen"] = current_action_time.strftime(
                "%Y-%m-%d %H:%M:%S")

# Trim the sessions to remove outliers
for i in range(len(outfile)):
    del_data = []
    for j in range(len(outfile[i]["sessions"])):
        if len(outfile[i]["sessions"][j]) > 200:
            del_data.append(j)
    offset = 0
    for j in range(len(del_data)):
        del outfile[i]["sessions"][del_data[j]-offset]
        offset += 1

# Add the final UseStop to each user
for i in range(len(outfile)):
    if len(outfile[i]["sessions"]) > 0:
        if outfile[i]["sessions"][-1][-1] != "UseStop":
            outfile[i]["sessions"][-1].append(
                {"timestamp": outfile[i]["sessions"][-1][-1]["timestamp"], "data": "UseStop"})
    else:
        print("No Sessions: " + outfile[i]["deviceid"])


with open(out_file_name, 'w', encoding='utf-8') as f:
    json.dump(outfile, f, ensure_ascii=False, indent=4)
