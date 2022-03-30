"""
File used for descriptive statistics on the data set
Each section has a command which can pipe to a text file as an output

Uncomment a section to get the required stats
"""

import sys
import ijson
import numpy as np
from datetime import datetime

#The formatted file
inp_file_name = sys.argv[1]

# User times
# python user_data.py com_data.json > user_times.txt
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



# Total User Actions
# python user_data.py com_data.json > user_actions.txt
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')

#     users = []
#     type_dict = {}
#     for user in out:
#         on = True
#         summer = 0
#         for session in user['sessions']:
#             summer += len(session)
#         users.append([user["deviceid"], summer])
#     users.sort(key=lambda x: x[1])
#     users.reverse()
#     for user in users:
#         print("{0} : {1}".format(user[0], user[1]))



# Session lengths to csv
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')

#     users = []
#     type_dict = {}
#     for user in out:
#         for session in user['sessions']:
#             users.append([user["deviceid"],len(session)])
#     users.sort(key=lambda x: x[1])
#     for user in users:
#         # print("{0} : {1}".format(user[0], user[1]))
#         # 
#         # CSV
#         print("{0},".format(user[1]))



# Session analyser
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')

#     users = []
#     type_dict = {}
#     for user in out:
#         on = True
#         for session in user['sessions']:
#             if len(session) == 2535:
#                 for event in session:
#                     if type_dict.get(event["data"]):
#                         type_dict[event["data"]] += 1
#                     else:
#                         type_dict[event["data"]] = 1
#                 print(session)
#                 # print(type_dict)
#                 # print(user["deviceid"])
#                 break



#Session Length
# python user_data.py com_data.json > session_length.txt
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     session_lengths = []
#     users = []
#     for user in out:
#         for session in user["sessions"]:
#             time_dif = datetime.strptime(session[-1]["timestamp"], "%Y-%m-%d %H:%M:%S") - datetime.strptime(session[0]["timestamp"], "%Y-%m-%d %H:%M:%S")
#             session_lengths.append(time_dif.seconds)
#
# math_sessions = np.array(session_lengths)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))



# No. Events per Session
# python user_data.py com_data.json > no_events_per_session.txt
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     no_events_session = []
#     for user in out:
#         for session in user["sessions"]:
#             no_events_session.append(len(session))
#
# math_sessions = np.array(no_events_session)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))



#No. Sessions
# python user_data.py com_data.json > no_sessions.txt
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     no_sessions = []
#     for user in out:
#         no_sessions.append(len(user["sessions"]))
#
# math_sessions = np.array(no_sessions)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))



#No. Events per User
# python user_data.py com_data.json > no_events_per_user.txt
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     no_events_user = []
#     for user in out:
#         user_total = 0
#         for session in user["sessions"]:
#             user_total += len(session)
#         no_events_user.append(user_total)
#
# math_sessions = np.array(no_events_user)
# print("Average: {avg}".format(avg=np.mean(math_sessions)))
# print("Median: {med}".format(med=np.median(math_sessions)))
# print("Min: {min}".format(min=np.min(math_sessions)))
# print("Max: {max}".format(max=np.max(math_sessions)))
# print("STD: {sd}".format(sd=np.std(math_sessions)))



#No. of occurrences per action
# python user_data.py com_data.json > kind_vals.txt
# with open(inp_file_name, "rb") as inp:
#     out = ijson.items(inp, 'item')
#     kind_vals = {}
#     for user in out:
#         for session in user["sessions"]:
#             for event in session:
#                 if kind_vals.get(event["data"]) == None:
#                     kind_vals[event["data"]] = 1
#                 else:
#                     kind_vals[event["data"]] += 1
#     for k, v in sorted(kind_vals.items(), key=lambda x: x[1]):
#         print("{:<25} : {:<}".format(k, v))