# Store statistics of at least 30 cricket players. 
# Example Structure 
# players = { 
#     "Virat": { 
#         "runs": 645, 
#         "matches": 12, 
#         "wickets": 0 
#     } 
# } 
# Requirements 
# 1. Display all player statistics.  
# 2. Find highest run scorer.  
# 3. Find lowest run scorer.  
# 4. Calculate average runs.  
# 5. Find player with maximum wickets.  
# 6. Find all-rounders (runs > 300 and wickets > 5).  
# 7. Display players scoring above average.  
# 8. Create categories:  
# o Star Performer  
# o Good Performer  
# o Average Performer  
# o Poor Performer  
# 9. Generate team statistics.  
# 10. Display top 5 batsmen.  
# 11. Display top 5 bowlers.  
# 12. Create a separate dictionary for award winners. 
# ==============================================================================
# CRICKET PLAYER PERFORMANCE ANALYSIS SYSTEM
# Developed using Basic Python Core Constructs (Loops, Conditionals, and Dictionaries)
# ==============================================================================
#create sample data for players
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 512, "matches": 12, "wickets": 1},
    "Gill": {"runs": 698, "matches": 12, "wickets": 0},
    "Rahul": {"runs": 435, "matches": 11, "wickets": 0},
    "Hardik": {"runs": 278, "matches": 10, "wickets": 8},
    "Pant": {"runs": 534, "matches": 12, "wickets": 0},
    "Surya": {"runs": 389, "matches": 11, "wickets": 1},
    "Jadeja": {"runs": 301, "matches": 12, "wickets": 12},
    "Iyer": {"runs": 455, "matches": 11, "wickets": 0},
    "KL": {"runs": 410, "matches": 10, "wickets": 0},
    "Bumrah": {"runs": 55, "matches": 12, "wickets": 18},
    "Shami": {"runs": 48, "matches": 11, "wickets": 16},
    "Siraj": {"runs": 42, "matches": 12, "wickets": 15},
    "Kuldeep": {"runs": 60, "matches": 10, "wickets": 14},
    "Axar": {"runs": 245, "matches": 10, "wickets": 10},
    "Ashwin": {"runs": 210, "matches": 9, "wickets": 11},
    "Rinku": {"runs": 320, "matches": 8, "wickets": 0},
    "Tilak": {"runs": 290, "matches": 9, "wickets": 1},
    "Jaiswal": {"runs": 580, "matches": 11, "wickets": 0},
    "Samson": {"runs": 355, "matches": 10, "wickets": 0},
    "Chahal": {"runs": 35, "matches": 9, "wickets": 13},
    "Arshdeep": {"runs": 28, "matches": 10, "wickets": 12},
    "Prasidh": {"runs": 18, "matches": 8, "wickets": 9},
    "Ishan": {"runs": 390, "matches": 10, "wickets": 0},
    "Gaikwad": {"runs": 470, "matches": 11, "wickets": 0},
    "Dube": {"runs": 330, "matches": 10, "wickets": 4},
    "Washington": {"runs": 215, "matches": 9, "wickets": 7},
    "Harshal": {"runs": 75, "matches": 9, "wickets": 10},
    "Mukesh": {"runs": 22, "matches": 8, "wickets": 8},
    "Avesh": {"runs": 30, "matches": 8, "wickets": 9}
}
# 1. Display all player statistics
print("Player Statistics:")
for player in players:
    print(player, ":", players[player])
# 2 & 3. Find highest and lowest run scorer
first = True
for player in players:
    if first:
        highest = player
        lowest = player
        first = False
    else:
        if players[player]["runs"] > players[highest]["runs"]:
            highest = player
        if players[player]["runs"] < players[lowest]["runs"]:
            lowest = player
print("\nHighest Run Scorer:", highest, "-", players[highest]["runs"])
print("Lowest Run Scorer:", lowest, "-", players[lowest]["runs"])
# 4. Calculate average runs
total_runs = 0
count = 0
for player in players:
    total_runs = total_runs + players[player]["runs"]
    count = count + 1
average = total_runs / count
print("Average Runs:", average)
# 5. Find player with maximum wickets
first = True
for player in players:
    if first:
        best_bowler = player
        first = False
    elif players[player]["wickets"] > players[best_bowler]["wickets"]:
        best_bowler = player
print("Maximum Wickets:", best_bowler, "-", players[best_bowler]["wickets"])
# 6. Find all-rounders
print("\nAll-Rounders (Runs > 300 and Wickets > 5):")
for player in players:
    if players[player]["runs"] > 300 and players[player]["wickets"] > 5:
        print(player)
# 7. Display players scoring above average
print("\nPlayers Scoring Above Average:")
for player in players:
    if players[player]["runs"] > average:
        print(player, "-", players[player]["runs"])
# 8. Create performance categories
star = []
good = []
average_perf = []
poor = []
for player in players:
    runs = players[player]["runs"]
    if runs >= 500:
        star.append(player)
    elif runs >= 300:
        good.append(player)
    elif runs >= 100:
        average_perf.append(player)
    else:
        poor.append(player)
print("\nStar Performers:", star)
print("Good Performers:", good)
print("Average Performers:", average_perf)
print("Poor Performers:", poor)
# 9. Generate team statistics
total_wickets = 0
total_matches = 0
for player in players:
    total_wickets = total_wickets + players[player]["wickets"]
    total_matches = total_matches + players[player]["matches"]
print("\nTeam Statistics")
print("Total Players:", count)
print("Total Runs:", total_runs)
print("Total Wickets:", total_wickets)
print("Total Matches Played:", total_matches)
# 10. Display top 5 batsmen
print("\nTop 5 Batsmen:")
temp = players.copy()
for i in range(5):
    first = True
    for player in temp:
        if first:
            best = player
            first = False
        elif temp[player]["runs"] > temp[best]["runs"]:
            best = player
    print(i + 1, ".", best, "-", temp[best]["runs"])
    del temp[best]
# 11. Display top 5 bowlers
print("\nTop 5 Bowlers:")
temp = players.copy()
for i in range(5):
    first = True
    for player in temp:
        if first:
            best = player
            first = False
        elif temp[player]["wickets"] > temp[best]["wickets"]:
            best = player
    print(i + 1, ".", best, "-", temp[best]["wickets"])
    del temp[best]
# 12. Create separate dictionary for award winners
awards = {}
for player in players:
    if players[player]["runs"] >= 500 or players[player]["wickets"] >= 10:
        awards[player] = players[player]
print("\nAward Winners:")
for player in awards:
    print(player, ":", awards[player])
# Tournament Report
print("\n========== TOURNAMENT REPORT ==========")
print("Highest Run Scorer :", highest, "-", players[highest]["runs"])
print("Highest Wicket Taker :", best_bowler, "-", players[best_bowler]["wickets"])
print("Average Team Runs :", average)
print("Total Runs Scored :", total_runs)
print("Total Wickets Taken :", total_wickets)
print("Number of Award Winners :", len(awards))
print("======================================")