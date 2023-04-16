#title: gonzalez_hobbies.py
#author: Janis Gonzalez
#date: 04/16/2023
#description: list of hobbies and days


#list of 5 hobbies
hobbies = ["Graphic Design", "Research", "Painting", "Clay Making", "Writing"]
#for loop to iterate over the list of hobbies and print them to console window
for hobby in hobbies:
    print(hobby)

#list of the days 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#for loop to iterate over the list of days and an if…else statement to display what the day is with a message
for day in days:
    if day == "Sunday":
        print("Today is Sunday which means no work so enjoy your hobbies!")
    elif day == "Monday":
        print("Today is Monday which means we have work.")
    elif day == "Tuesday":
        print("Today is Tuesday which means we have work.")
    elif day == "Wednesday":
        print("Today is Wednesday which means we have work.")
    elif day == "Thursday":
        print("Today is Thursday which means we have work.")
    elif day == "Friday":
        print("Today is Friday which means we have work.")
    elif day == "Saturday":
        print("Today is Saturday which means no work so enjoy your hobbies!")