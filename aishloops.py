nums = [1, 2, 3, 4, 5]
 
for num in nums:
  print(num + 1)

#This will output:

#2
#3
#4
#5
#6

#nested for loop
teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
  for name in team:
    print(name)

#while loop
i = 1
while i < 6:
  print(i)
  i += 1