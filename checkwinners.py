# script for looking at potentially-discretionary or pseudo-random rewards to identifying multiwinners
files = {'20210823_AllNBAShowcaseChallenge': 'winners/20210823_AllNBAShowcaseChallenge.txt',
         '20210904_EndofS2Trivia': 'winners/20210904_EndofS2TriviaWinners.txt',
         '20210929_WNBARunItBackTrivia': 'winners/20210929_WNBARunItBackTriviaWinners.txt',
         '20210929_Top100PlaysTrivia': 'winners/20210929_Top100PlaysTriviaWinners.txt',
         '20210930_Top100PlaysShowcaseChallenge': 'winners/20210930_Top100PlaysShowcaseChallenge.txt',
         '20211004_HBDTopShotTrivia': 'winners/20211004_HBDTopShotTriviaWinners.txt'}
# unannounced/pending winners:
# Top Shot Birthday Showcase (Oct 1 -7): https://hoo.ps/bday-showcasechallenge
winners = {}
mult_winners = {}
for k, v in files.items():
    winners[k] = []
    lines = open(v, "r").readlines()
    print(f"{k} has {len(lines)-1} winners")
    for a in lines[1:]:  # skip line 1, containing reward title/source and winner list URL
        winners[k].append(a.format().strip())
for k, v in winners.items():
    for k2, v2 in winners.items():
        if k == k2:
            break
        both = set(winners[k]) & set(winners[k2])
        if both:
            print(f'{len(both)} accounts appears in both {k} and {k2}')
            for i in both:
                if i in mult_winners.keys():
                    mult_winners[i].extend([k, k2])
                    mult_winners[i] = list(set(mult_winners[i]))
                else:
                    mult_winners[i] = []
                    mult_winners[i].extend([k, k2])
                    mult_winners[i] = list(set(mult_winners[i]))
print('\n')
wincounts = [0 for i in range(len(files))]
for i in mult_winners:
    count = len(mult_winners[i])
    for j in range(len(files)):
        if count == j+1:
            wincounts[j] += 1
        if count >= 4 and j == len(files)-1:
            print(f'***** account {i} has {count} wins: *****\n{mult_winners[i]}\n')
print('Accumulated multi-winners (# of wins: # of accounts):')
for i in range(1, len(wincounts)):
    print(f'{i+1}: {wincounts[i]}')



