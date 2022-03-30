# Timelog

* Modelling and analysis of a mobile game usage
* Fin McCallum
* 2362646m
* Oana Andrei

## Week 1

### 01 Oct 2021
* *0.5 hours* First meeting with supervisor introducing the project

## Week 2

### 4 Oct 2021

* *2 hours* Read the project guidance notes
* *1 hour* Read gameplay analysis of RPGLite (Kavanagh, 2020)

### 8 Oct 2021

* *0.5 hours* Created GitLab repository and copied project template
* *0.5 hours* meeting with supervisor

## Week 3

### 13 Oct 2021
* *5 hours* Read through readings especially (Andrei, 2014) (Andrei, 2016)

### 14 Oct 2021
* *3 hours* Working through dataset, changed data to vertical to understand easier, can now view in IDE

### 15 Oct 2021
* *0.5 hours* meeting with supervisor
* *1 hour* Formulate ways to get data into form needed for GPAM & PRISM

## Week 4

### 21 Oct 2021
* *3 hours* extracting data from dataset with script
* *2 hours* Created script to extract one users actions in aim to get data in correct form

### 22 Oct 2021
* *0.5 hours* Meeting with supervisor with progress made with the script

## Week 5

### 27 Oct 2021
* *2 hours* Categorise the kinds into sub categories

### 29 Oct 2021
* *0.5 hours* Meeting with supervisor

## Week 6
### 2 Nov 2021
* *4 hours* Extract data for one user and put it in form needed for dataset

### 3 Nov 2021
* *2 hours* Get data in form for 1 user for all categories
* *1 hour* Get data from multiple users and construct a Markov Chain diagram
* *2 hours* Using the category and sub categories, create a mapping so the number of "kinds" is reduced
* *0.5 hours* Create a Markov chain for 5+ users with the smaller dataset

### 4 Nov 2021
* *2 hours* Able to parse all users in the file inplace

### 5 Nov 2021
* *1 hour* Look at parameters for PAM algorithm
* *0.5 hours* Meeting with supervisor

## Week 7
### 9 Nov 2021
* *1 hour* Stripped the users from performing same action twice
* *1 hour* Creates a user_data file that shows how many days each user has been on

### 11 Nov 2021
* *2 hours* Choose time intervals for data and generate models

### 12 Nov 2021
* *0.5 hours* Meeting with supervisor
* *1 hour* Explore SAP properties

## Week 8

### 17 Nov 2021
* *0.5 hours* Added UseStart & UseStop to the file to add states when sessions start and end
* *3.5 hours* Running PAM Models for each of the time sets with k=2 & k=3

### 19 Nov 2021
* *2 hours* Correctly ran PAM models again with UseStop at end of each user
* *0.5 hours* Meeting with supervisor
* *1 hour* Understand the separate SAP properties

## Week 9

### 24 Nov 2021
* *2 hours* Generating stats from userset
* *3 hours* Creating a PRISM output file to txt converter, takes multiple files and multiple tests in file

### 26 Nov 2021
* *0.5 hours* Meeting with supervisor
* *3 hours* Try different values for N

## Week 10

### 29 Nov 2021
* *3 hours* Looking at number of events in sessions and graphing them in excel

### 03 Dec 2021
* *0.5 hours* Meeting with supervisor
* *1 hour* See cutoff for data
### 05 Dec 2021
* *2.5 hours* Investigating the 3k event session and writing results

## Week 11

### 06 Dec 2021
* *2.5 hours* Analysing 2 more long sessions and writing about it

### 08 Dec 2021
* *1.5 hours* Analysis meow and found out that refresh & login are repeated many times

### 09 Dec 2021
* *2 hours* Remove repeated patterns like refresh & login so now the data is more accurate, refreshed all

### 10 Dec 2021
* *0.5 hours* Meeting with supervisor

### 12 Dec 2021
* *2 hours* Removed refresh from dataset and capped the session length to 200 as that covers 98% of sessions and removes extreme results
* *1.5 hour* Rerunning PAM Models for the new dataset

## Week 12

### 13 Dec 2021
* *1 hour* Changes made to prism output converter
* *0.5 hour* Ran prism files through all PAM
* *2 hours* Started analysis of prism outputs by comparing probabilities

### 14 Dec 2021
* *3 hours* Writing status report
* *1 hour* Changes made to prism output converter to put all K values in same file rather than separate
* *0.5 hours* Updated PRISM Properties file
* *0.5 hours* Meeting with supervisor

### 15 Dec 2021
* *3 hours* Ran PRISM files with new VisitCountInit for each kind

### 17 Dec 2021
* *0.5 hours* Meeting with supervisor
* *4 hours* Construct plan over holidays

## Week 13

### 05 Jan 2022
* *8 hours* Spent time on Introduction & Background of dissertation

### 06 Jan 2022
* *7 hours* Spent time on the Background and completed the introduction of presentation

### 07 Jan 2022
* *3 hours* Work on dissertation added section on RPGLite
* *1 hour* Downloading and playing RPGLite on 2 mobile phones to know what the game plays like
* *3 hour* Investigating the difference if prev_prev was kept in the main generate format. Found 200,000 lines difference where the majority would be about how the game was played, whether they fastforwarded rolls or not. Worth talking about how it can remove tasks such as home->leaderboard->home

## Week 14

### 10 Jan 2022
* *3 hours* Looked at difference in values between time intervals from PRISM analysis
* *2 hours* Time spent on dissertation with finishing section on RPGLite background

### 14 Jan 2022
* *0.5 hours* Meeting with supervisor

## Week 15

### 21 Jan 2022
* *0.5 hours* Meeting with supervisor

### 22 Jan 2022
* *6 hours* Worked on chapter 4 of the dissertation, working with the dataset

### 24 Jan 2022
* *2 hours* Read background on probabilistic temporal properties
* *0.5 hours* Meeting with supervisor

### 28 Jan 2022
* *0.5 hours* Meeting with supervisor

## Week 16

### 03 Feb 2022
* *5 hours* Working further on background work

### 04 Feb 2022
* *0.5 hours* Meeting with supervisor

## Week 17

### 10 Feb 2022
* *5 hours* Working on Section 3 on Case Study of RPGLite

### 11 Feb 2022
* *0.5 hours* Meeting with supervisor

## Week 18

### 14 Feb 2022
* *5 hours* Starting work on Section 4

### 17 feb 2022
* *10 hours* Section 4 on preparing the data set

## Week 19
### 23 Feb 2022
* *6 hours* Editing section 4

## Week 20

### 28 Feb 2022
*8 hours* Writing Chapter 5 on Analysis of data set intro

### 01 Mar 2022
* *5 hours* Formalise method of analysis

### 02 Mar 2022
* *6 hours* Conduct analysis of data, create tables from SAP properties

### 03 Mar 2022
* *4 hours* Create graphs from table of SAP properties from each time interval

### 05 Mar 2022
* *5 hours* Add data from analysis into dissertation

### 06 Mar 2022
* *5 hours* Work on Core Game Functionalities in the dissertation

## Week 21

### 07 Mar 2022
* *6 hours* Analyse graph data set by using writing thoughts from graph comparing time intervals

### 10 Mar 2022
* *0.5 hours* Meeting with supervisor
* *6 hours* Further work on adding analysis to dissertation

### 13 Mar 2022
* *7 hours* More analysis added to dissertation

## Week 22

### 14 Mar 2022
* *10 hours* Bring analysis from paper into dissertation writing chapter 5

### 15 Mar 2022
* *5 hours* Write evaluation on method and RPGLite data set


### 16 Mar 2022
* *7 hours* Evaluation section

### 20 Mar 2022
* *6 hours* Further evaluation dissertation
## Week 23

### 21 Mar 2022
* *7 hours* Further evaluation dissertation
* *3 hours* Write conclusion

### 23 Mar 2022
* *8 hours* Conclusion on diss

### 24 Mar 2022
* *0.5 hours* Final meeting with supervisor
* *6 hours* Make changes suggested by supervisor

### 25 Mar 2022
* *8 hours* Write overall evaluation


### 27 Mar 2022
* *6 hours* Create presentation and script for video recording

## Week 24

### 28 Mar 2022
* *3 hours* Updating timelog for missing times
* *2 hours* Cleaning repo for submission

### 29 Mar 2022
* *1 hour* Write abstract
* *8 hours* Review dissertation and make grammar changes

### 30 Mar 2022
* *10 hours* Fix repo and record presentation