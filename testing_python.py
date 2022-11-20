import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)
weekdays.append('Sabado')
weekdays.remove('Monday')
print(weekdays)
print(f'Today is: {day}')


if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
elif(day == 'Sabado'):
    print('The handover is coming')
else:
    print('Not quite there yet.')


x = 70
if x > 50:
	print("mayor que 50")
else:
	print("menor que 50")

