# The government wants to analyze city data. 
# Store details of at least 30 cities. 
# Example Structure 
# cities = { 
#     "Delhi": { 
#         "population": 32000000, 
#         "area": 1484, 
#         "literacy": 89 
#     } 
# } 
# Requirements:
# 1. Display all city details.   
# 2. Find the most populated city.   
# 3. Find the least populated city.   
# 4. Calculate average population.   
# 5. Display cities with literacy rate above 90%.   
# 6. Display cities with literacy below average.   
# 7. Calculate population density.   
# 8. Find city with highest density.   
# 9. Categorize cities (Small, Medium, Large).   
# 10. Create a development-priority list.   
# 11. Generate separate dictionaries for High/Low Literacy Cities.   
# 12. Generate a national summary report.   
# Challenge: Rank all cities based on population density.
# ==============================================================================
# Create data 
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 206, "literacy": 88},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 90},
    "Bengaluru": {"population": 13000000, "area": 741, "literacy": 91},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 87},
    "Ahmedabad": {"population": 8400000, "area": 505, "literacy": 86},
    "Pune": {"population": 7200000, "area": 518, "literacy": 89},
    "Jaipur": {"population": 4100000, "area": 467, "literacy": 84},
    "Lucknow": {"population": 3900000, "area": 631, "literacy": 83},
    "Kanpur": {"population": 3200000, "area": 403, "literacy": 82},
    "Nagpur": {"population": 2900000, "area": 218, "literacy": 91},
    "Indore": {"population": 3100000, "area": 530, "literacy": 88},
    "Bhopal": {"population": 2400000, "area": 463, "literacy": 85},
    "Patna": {"population": 2600000, "area": 250, "literacy": 81},
    "Surat": {"population": 7000000, "area": 326, "literacy": 89},
    "Ludhiana": {"population": 1800000, "area": 159, "literacy": 86},
    "Agra": {"population": 2000000, "area": 188, "literacy": 85},
    "Nashik": {"population": 1700000, "area": 264, "literacy": 90},
    "Vadodara": {"population": 2100000, "area": 235, "literacy": 88},
    "Meerut": {"population": 1600000, "area": 142, "literacy": 82},
    "Varanasi": {"population": 1500000, "area": 112, "literacy": 84},
    "Rajkot": {"population": 1400000, "area": 170, "literacy": 87},
    "Amritsar": {"population": 1300000, "area": 139, "literacy": 85},
    "Allahabad": {"population": 1200000, "area": 365, "literacy": 83},
    "Ranchi": {"population": 1100000, "area": 175, "literacy": 87},
    "Jabalpur": {"population": 1050000, "area": 367, "literacy": 86},
    "Gwalior": {"population": 1000000, "area": 423, "literacy": 84},
    "Coimbatore": {"population": 2200000, "area": 247, "literacy": 92},
    "Vijayawada": {"population": 1500000, "area": 261, "literacy": 89}
}
while True:
    print("\n====== CITY POPULATION & DEVELOPMENT DASHBOARD ======")
    print("1. Display All City Details")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Cities with Literacy > 90%")
    print("6. Cities with Literacy Below Average")
    print("7. Population Density")
    print("8. Highest Density City")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. High & Low Literacy Dictionaries")
    print("12. National Summary Report")
    print("13. Rank Cities by Population Density")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    # 1. Display all city details
    if choice == 1:
        print("\nCity Details:")
        for city in cities:
            print(city, ":", cities[city])
    # 2. Most populated city
    elif choice == 2:
        first = True
        for city in cities:
            if first:
                max_city = city
                first = False
            elif cities[city]["population"] > cities[max_city]["population"]:
                max_city = city
        print("Most Populated City:", max_city,
              "-", cities[max_city]["population"])
    # 3. Least populated city
    elif choice == 3:
        first = True
        for city in cities:
            if first:
                min_city = city
                first = False
            elif cities[city]["population"] < cities[min_city]["population"]:
                min_city = city
        print("Least Populated City:", min_city,
              "-", cities[min_city]["population"])
    # 4. Average population
    elif choice == 4:
        total = 0
        count = 0
        for city in cities:
            total = total + cities[city]["population"]
            count = count + 1
        average = total / count
        print("Average Population:", average)
    # 5. Literacy above 90%
    elif choice == 5:
        print("Cities with Literacy Above 90%:")
        for city in cities:
            if cities[city]["literacy"] > 90:
                print(city)
    # 6. Literacy below average
    elif choice == 6:
        total_lit = 0
        count = 0
        for city in cities:
            total_lit = total_lit + cities[city]["literacy"]
            count = count + 1
        avg_lit = total_lit / count
        print("Cities with Literacy Below Average:")
        for city in cities:
            if cities[city]["literacy"] < avg_lit:
                print(city)
    # 7. Population Density
    elif choice == 7:
        print("Population Density:")
        for city in cities:
            density = cities[city]["population"] / cities[city]["area"]
            print(city, ":", round(density, 2))
    # 8. Highest Density City
    elif choice == 8:
        first = True
        for city in cities:
            density = cities[city]["population"] / cities[city]["area"]
            if first:
                high_density_city = city
                high_density = density
                first = False
            elif density > high_density:
                high_density = density
                high_density_city = city
        print("Highest Density City:", high_density_city)
    # 9. Categorize Cities
    elif choice == 9:
        small = []
        medium = []
        large = []
        for city in cities:
            pop = cities[city]["population"]
            if pop < 2000000:
                small.append(city)
            elif pop <= 10000000:
                medium.append(city)
            else:
                large.append(city)
        print("Small Cities:", small)
        print("Medium Cities:", medium)
        print("Large Cities:", large)
    # 10. Development Priority List
    elif choice == 10:
        print("Development Priority Cities:")
        for city in cities:
            if cities[city]["literacy"] < 85:
                print(city)
    # 11. High & Low Literacy Dictionaries
    elif choice == 11:
        high_literacy = {}
        low_literacy = {}
        for city in cities:
            if cities[city]["literacy"] >= 90:
                high_literacy[city] = cities[city]
            else:
                low_literacy[city] = cities[city]
        print("High Literacy Cities:")
        print(high_literacy)
        print("\nLow Literacy Cities:")
        print(low_literacy)
    # 12. National Summary Report
    elif choice == 12:
        total_population = 0
        total_area = 0
        for city in cities:
            total_population = total_population + cities[city]["population"]
            total_area = total_area + cities[city]["area"]
        print("\n====== NATIONAL SUMMARY REPORT ======")
        print("Total Cities:", len(cities))
        print("Total Population:", total_population)
        print("Total Area:", total_area)
        print("Average Population:", total_population / len(cities))
    # 13. Rank Cities by Population Density (without sort)
    elif choice == 13:
        temp = cities.copy()
        rank = 1
        print("\nRanking by Population Density:")
        while len(temp) > 0:
            first = True
            for city in temp:
                density = temp[city]["population"] / temp[city]["area"]
                if first:
                    best_city = city
                    best_density = density
                    first = False
                elif density > best_density:
                    best_density = density
                    best_city = city
            print(rank, ".", best_city, "-", round(best_density, 2))
            del temp[best_city]
            rank = rank + 1
    # Exit
    elif choice == 0:
        print("Program Ended.")
        break
    else:
        print("Invalid Choice! Please try again.")