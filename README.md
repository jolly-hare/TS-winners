# TS-winners

Simple pet project looking for anything interesting in the accounts that are winning the random packs on NBATopShot. I've captured the winner lists from the past few Showcase Challenges and Trivia drawings and found that there seems to be a fair bit of overlap such that roughly half of the winners of the Top Plays Shawcase Challenge were also winners of hte All NBA Showcase Challenge; considering that many tens of thousands of people completed these challenge, that ~1800 accounts managed to win both seems a little off. 

Happy to have anyone else take a look at the code; verify the data, and determine if my figures are off.

The data files contain the URL of the original winners list in line #1

NBATopshot user @jolly_hare2634
Twitter @ts_hare

# Expected Output

20210823_AllNBAShowcaseChallenge has 10000 winners
20210904_EndofS2Trivia has 120 winners
20210929_WNBARunItBackTrivia has 100 winners
20210929_Top100PlaysTrivia has 100 winners
20210930_Top100PlaysShowcaseChallenge has 3600 winners
20211004_HBDTopShotTrivia has 120 winners
57 accounts appears in both 20210904_EndofS2Trivia and 20210823_AllNBAShowcaseChallenge
49 accounts appears in both 20210929_WNBARunItBackTrivia and 20210823_AllNBAShowcaseChallenge
7 accounts appears in both 20210929_WNBARunItBackTrivia and 20210904_EndofS2Trivia
50 accounts appears in both 20210929_Top100PlaysTrivia and 20210823_AllNBAShowcaseChallenge
6 accounts appears in both 20210929_Top100PlaysTrivia and 20210904_EndofS2Trivia
4 accounts appears in both 20210929_Top100PlaysTrivia and 20210929_WNBARunItBackTrivia
1798 accounts appears in both 20210930_Top100PlaysShowcaseChallenge and 20210823_AllNBAShowcaseChallenge
15 accounts appears in both 20210930_Top100PlaysShowcaseChallenge and 20210904_EndofS2Trivia
12 accounts appears in both 20210930_Top100PlaysShowcaseChallenge and 20210929_WNBARunItBackTrivia
16 accounts appears in both 20210930_Top100PlaysShowcaseChallenge and 20210929_Top100PlaysTrivia
44 accounts appears in both 20211004_HBDTopShotTrivia and 20210823_AllNBAShowcaseChallenge
1 accounts appears in both 20211004_HBDTopShotTrivia and 20210904_EndofS2Trivia
3 accounts appears in both 20211004_HBDTopShotTrivia and 20210929_Top100PlaysTrivia
16 accounts appears in both 20211004_HBDTopShotTrivia and 20210930_Top100PlaysShowcaseChallenge


***** account HambisCA has 4 wins: *****
['20211004_HBDTopShotTrivia', '20210823_AllNBAShowcaseChallenge', '20210929_Top100PlaysTrivia', '20210904_EndofS2Trivia']

***** account dardMC21 has 5 wins: *****
['20210930_Top100PlaysShowcaseChallenge', '20210823_AllNBAShowcaseChallenge', '20210904_EndofS2Trivia', '20210929_Top100PlaysTrivia', '20210929_WNBARunItBackTrivia']

Accumulated multi-winners (# of wins: # of accounts):
2: 1936
3: 42
4: 1
5: 1
6: 0
