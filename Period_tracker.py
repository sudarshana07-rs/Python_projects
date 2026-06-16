print("Period Calender💕💕💕")
print("Your Cycle, Your Health ,Your Balance ❤️❤️❤️!!! ")
name=input("Enter your dear name Girlie: ")
print(f'{name} ❤️, Welcome to Period Calender!!!')
age=int(input("Enter your age: "))
first_time=input("Is it your first time getting period: ")
if (first_time== 'Yes'or first_time== "yes" or first_time=='Yes'):
    print(f"{name}Congratulations On your first period💕💕💕")
start_date=input("Enter the start date of last period: ")
avg_cycle=input("Enter your average cycle length: ")
period_duration=input("Enter your period duration: ")
next_period= start_date + avg_cycle   # Next Period
print(next_period)
 