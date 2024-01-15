"""
Design program that determines award to be received by triathlon participant.
Program must include time (in min) for 3 events:
    Swimming
    Cycling
    Running
"""

# Request participants name.
first_name = input("Enter your name: ")

# Request participants times for each event.
swimming = int(input("Enter your swimming time in minutes: "))
cycling = int(input("Enter your cycling time in minutes: "))
running = int(input("Enter your running time in minutes: "))

# Calculate and display total time to complete triathlon.
total_time = swimming + cycling + running
print(f"Hi {first_name}, your total time is {total_time} minutes.")

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