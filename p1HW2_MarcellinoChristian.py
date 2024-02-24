# Christian Marcellino

 # 2/24/24

 # P1HW2

 # This program will go over budgeting options.
 
print('This program calculates and displays travel expenses.')
print('Enter Budget:', end = ' ')
Budget=int(input())
print('Enter your travel destination:', end = ' ')
Destination=input()
print('How much do you think you will spend on gas?')
Gas=int(input())
print('Approximately, how much will you need for accomodation/hotel?')
Room=int(input())
print('Last, how much do you need for food?')
Food=int(input())

print('---------------Travel Expenses----------')
print('Location:'+Destination)
print('Initial Budget:'+str(Budget))
print()
print('Fuel:'+str(Gas))
print('Accomodation:'+str(Room))
print('Food:'+str(Food))
print('Remaining Balance:'+str(Budget-Gas-Room-Food))

            



