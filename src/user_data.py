import sys
import ijson
import numpy as np
from datetime import datetime

#The formatted file
inp_file_name = sys.argv[1]

# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')

#     users = []
#     for user in out:
#         first_time = user['firstSeen']
#         last_time = user['lastSeen']
#         user = user['deviceid']

#         time_dif = datetime.strptime(last_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(first_time, "%Y-%m-%d %H:%M:%S")

#         users.append([user, time_dif.days])

#     users.sort(key=lambda x: x[1])


#     for user in users:
#         print("{user}: {time}".format(user=user[0], time=user[1]))

with open(inp_file_name, "rb") as inp:
    out = ijson.items(inp, 'item')

    users = []
    type_dict = {}
    for user in out:
        on = True
        for session in user['sessions']:
            if len(session) == 2459:
                for event in session:
                    if type_dict.get(event["data"]):
                        type_dict[event["data"]] += 1
                    else:
                        type_dict[event["data"]] = 1
                print(session)
                break
            users.append(len(session))      

    # users.sort()
    # for user in users:
    #     print("{0},".format(user))
        #print("\n\n\n\n")


#Session Length
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     session_lengths = []
#     users = []
#     for user in out:
#         for session in user["sessions"]:
#             time_dif = datetime.strptime(session[-1]["timestamp"], "%Y-%m-%d %H:%M:%S") - datetime.strptime(session[0]["timestamp"], "%Y-%m-%d %H:%M:%S")
#             session_lengths.append(time_dif.seconds)


# math_sessions = np.array(session_lengths)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))

# No. Events per Session
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     no_events_session = []
#     for user in out:
#         for session in user["sessions"]:
#             no_events_session.append(len(session))


# math_sessions = np.array(no_events_session)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))

#No. Sessions
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     no_sessions = []
#     for user in out:
#         no_sessions.append(len(user["sessions"]))


# math_sessions = np.array(no_sessions)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))


#No. Events per User
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     no_events_user = []
#     for user in out:
#         user_total = 0
#         for session in user["sessions"]:
#             user_total += len(session)
#         no_events_user.append(user_total)


# math_sessions = np.array(no_events_user)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))