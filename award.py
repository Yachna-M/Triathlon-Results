"""
Design program that determines award to be received by triathlon participant.
Program must include time (in min) for 3 events:
    Swimming
    Cycling
    Running
"""

# Request participants first name and surname.
first_name = input("Enter your name: ")
surname = input("Enter your surname: ")

# Request participants times for each event.
swimming_time = int(input("Enter your swimming time in minutes: "))
cycling_time = int(input("Enter your cycling time in minutes: "))
running_time = int(input("Enter your running time in minutes: "))

# Calculate and display total time to complete triathlon.
total_time = swimming_time + cycling_time + running_time
print(f"Hi {first_name} {surname}, your total time is {total_time} minutes.")

"""
Qualifying time is 100 minutes.

Display award the participant will receive based on below criteria.
    Within qualifying time: Provincial Colours
    Within 5 minutes of qualifying time: Provincial Half Colours
    Within 10 minutes of qualifying time: Provincial Scroll
    More than 10 minutes off from qualifying time: No award.
"""

if total_time <= 100:
    print("Congratulations, you will receive Provincial Colours!")

elif (total_time > 100) and (total_time <= 105):
    print("Congratulations, you will receive Provincial Half Colours!")

elif (total_time > 105) and (total_time <= 110):
    print("Congratulations, you will receive a Provincial Scroll!")

else:
    print("Unfortunately you will not receive an award.")