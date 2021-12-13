# Timelog

* Modelling and analysis of a mobile game usage
* Fin McCallum
* 2362646m
* Oana Andrei

## Guidance

* This file contains the time log for your project. It will be submitted along with your final dissertation.
* **YOU MUST KEEP THIS UP TO DATE AND UNDER VERSION CONTROL.**
* This timelog should be filled out honestly, regularly (daily) and accurately. It is for *your* benefit.
* Follow the structure provided, grouping time by weeks.  Quantise time to the half hour.

## Week 1

### 4 Oct 2021

* *2 hours* Read the project guidance notes
* *1 hour* Read gameplay analysis of RPGLite (Kavanagh, 2020)

## 8 Oct 2021

* *0.5 hours* Created GitLab repository and copied project template
* *0.5 hours* meeting with supervisor

## 13 Oct 2021
* *5 hours* Read through readings especially (Andrei, 2014) (Andrei, 2016)

## 14 Oct 2021
* *3 hours* Working through dataset, changed data to vertical to understand easier, can now view in IDE

## 15 Oct 2021
* *0.5 hours* meeting with supervisor
* *1 hour* Formulate ways to get data into form needed for GPAM & PRISM

## 21 Oct 2021
* *3 hours* extracting data from dataset with script
* *2 hours* Created script to extract one users actions in aim to get data in correct form

## 22 Oct 2021
* *0.5 hours* Meeting with supervisor with progress made with the script

## 27 Oct 2021
* *2 hours* Categorise the kinds into sub categories

## 2 Nov 2021
* *4 hours* Extract data for one user and put it in form needed for dataset

## 3 Nov 2021
* *2 hours* Get data in form for 1 user for all categories
* *1 hour* Get data from multiple users and construct a Markov Chain diagram
* *2 hours* Using the category and sub categories, create a mapping so the number of "kinds" is reduced
* *0.5 hours* Create a Markov chain for 5+ users with the smaller dataset

## 4 Nov 2021
* *2 hours* Able to parse all users in the file inplace

## 9 Nov 2021
* *1 hour* Stripped the users from performing same action twice
* *1 hour* Creates a user_data file that shows how many days each user has been on

## 11 Nov 2021
* *2 hours* Choose time intervals for data and generate models

## 17 Nov 2021
* *0.5 hours* Added UseStart & UseStop to the file to add states when sessions start and end
* *3.5 hours* Running PAM Models for each of the time sets with k=2 & k=3

## 19 Nov 2021
* *2 hours* Correctly ran PAM models again with UseStop at end of each user

## 24 Nov 2021
* *2 hours* Generating stats from userset
* *3 hours* Creating a PRISM output file to txt converter, takes multiple files and multiple tests in file

## 29 Nov 2021
* *3 hours* Looking at number of events in sessions and graphing them in excel

## 05 Dec 2021
* *2.5 hours* Investigating the 3k event session and writing results

## 06 Dec 2021
* *2.5 hours* Analysing 2 more long sessions and writing about it

## 08 Dec 2021
* *1.5 hours* Analysis meow and found out that refresh & login are repeated many times

## 09 Dec 2021
* *2 hours* Remove repeated patterns like refresh & login so now the data is more accurate, refreshed all

## 12 Dec 2021
* *2 hours* Removed refresh from dataset and capped the session length to 200 as that covers 98% of sessions and removes extreme results
* *1.5 hour* Rerunning PAM Models for the new dataset

## 13 Dec 2021
* *1 hour* Changes made to prism output converter
* *0.5 hour* Ran prism files through all PAM
* *2 hours* Started analysis of prism outputs by comparing probabilities