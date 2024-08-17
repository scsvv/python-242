score = 0

questions = [
    ["2+2=?", "4"],
    ["First letter in English's alphabet", "a"],
    ["Capital of Ukraine: ", "kiev"],
    ["First element in periodical table", "h"], 
    ["Best autos mark", "bmw"]
]

for question in questions:
    answer = input(f'{question[0]} \n\nYour answer is: ')

    if answer.lower() == question[1]:
        score += 1
        print("✅ Right\n\n")
    else: 
        print("❌ Wrong")

print(f"Score: {score}")
if score > 3:
    print("You win 🏆")
else: 
    print("You lose 💩")