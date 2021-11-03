from os import curdir
import sys
import operator
import ijson
import json
from datetime import datetime

mappings = {
    "home_screen_logout": "logout",
    "registration": "registration",
    "challenge_sent": "challenge_sent",
    "login": "login",
    "joined_queue": "joined_queue",
    "hs_refresh_pressed": "refresh",
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
    "refresh_online_game_pressed": "refresh",
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
outfile = []
users = ["Manakish", "Paddy", "elennon", "Beth", "cptKav", "Deanerbeck", "vinl"]
excluded = []

for user_id, user in enumerate(users):
    with open(inp_file_name, "rb") as inp:
        out = ijson.items(inp, 'item.page_hits.item')

        outfile.append({"deviceid": user, "sessions": []})
        one_user = (o for o in out if o['user'] == user and mappings.get(o['kind']) is not None)
        cur_session = []

        for action in one_user:
            if "." not in action["time"]:
                cur_session_time = datetime.strptime(
                action["time"], "%Y-%m-%d %H:%M:%S")
            else:
                cur_session_time = datetime.strptime(
                    action["time"], "%Y-%m-%d %H:%M:%S.%f")
            break


        for action in one_user:
            if "." not in action["time"]:
                current_action_time = datetime.strptime(
                    action["time"], "%Y-%m-%d %H:%M:%S")
                
            else:
                current_action_time = datetime.strptime(
                    action["time"], "%Y-%m-%d %H:%M:%S.%f")

            # If more than 30mins between action, different session
            if divmod((current_action_time - cur_session_time).total_seconds(), 60)[0] > 30:
                outfile[user_id]["sessions"].append(cur_session)
                cur_session = []
                cur_session_time = current_action_time
            cur_session.append(
                {"timestamp": current_action_time.strftime("%Y-%m-%d %H:%M:%S"), "data": mappings[action["kind"]]})

        outfile[user_id]["firstSeen"] = outfile[user_id]["sessions"][0][0]["timestamp"]
        outfile[user_id]["lastSeen"] = outfile[user_id]["sessions"][0][-1]["timestamp"]


with open(out_file_name+".json", 'w', encoding='utf-8') as f:
    json.dump(outfile, f, ensure_ascii=False, indent=4)
