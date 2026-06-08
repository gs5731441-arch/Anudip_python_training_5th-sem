runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player, score in runs.items():

    if score > 500:      # Validation
        print(player)

# 2. Find the Orange Cap winner
first = True

for player, score in runs.items():

    if first == True:
        orange_cap = player
        highest_runs = score
        first = False

    elif score > highest_runs:      # Validation
        highest_runs = score
        orange_cap = player

print("\nOrange Cap Winner:")
print(orange_cap, "(", highest_runs, ")")

# 3. Find the Lowest Scorer
first = True

for player, score in runs.items():

    if first == True:
        lowest_player = player
        lowest_runs = score
        first = False

    elif score < lowest_runs:      # Validation
        lowest_runs = score
        lowest_player = player

print("\nLowest Scorer:")
print(lowest_player, "(", lowest_runs, ")")

# 4. Calculate Total Runs Scored
total_runs = 0

for score in runs.values():

    if score >= 0:      # Validation
        total_runs += score

print("\nTotal Tournament Runs =", total_runs)

# 5. Create a List of Players Scoring Below 400
below_400 = []

for player, score in runs.items():

    if score < 400:      # Validation
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)

# 6. Count Players Scoring Between 400 and 600 Runs
count = 0

for score in runs.values():

    if score >= 400 and score <= 600:      # Validation
        count += 1

print("\nPlayers Between 400 and 600 Runs =", count)