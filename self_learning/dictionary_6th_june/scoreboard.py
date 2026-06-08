scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# 1. Display players who scored 50 or more runs
print("Players Scoring 50 or More Runs:")

for player, score in scores.items():

    if score >= 50:      # Validation
        print(player, ":", score)

# 2. Count the number of centuries
century_count = 0

for score in scores.values():

    if score >= 100:      # Validation
        century_count += 1

print("\nNumber of Centuries =", century_count)

# 3. Find the player with the highest score
first = True

for player, score in scores.items():

    if first == True:
        highest_player = player
        highest_score = score
        first = False

    elif score > highest_score:      # Validation
        highest_score = score
        highest_player = player

print("\nHighest Scorer:")
print(highest_player, ":", highest_score)

# 4. Create a list of players scoring below 30 runs
low_score_players = []

for player, score in scores.items():

    if score < 30:      # Validation
        low_score_players.append(player)

print("\nPlayers Scoring Below 30 Runs:")
print(low_score_players)

# 5. Count players scoring between 50 and 99
count_50_99 = 0

for score in scores.values():

    if score >= 50 and score <= 99:      # Validation
        count_50_99 += 1

print("\nPlayers Scoring Between 50 and 99 =", count_50_99)