cities = list()

while True:
    length = len(cities)
    city = input("Enter city name: ")
    city = city.lower().replace(" ", "")

    if length > 0:
        first_letter = cities[length - 1][-1]
        print(f"Your city might start on letter {first_letter}")
        if city[0] != first_letter:
            print(f"City name might start on {first_letter}")
            continue

    if city in cities: 
        print(f"{city} had been add early")
        continue
    
    cities.append(city)

    if length == 5: 
        break

print(cities)

