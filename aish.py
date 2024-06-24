x = 4
y = 3
 
x + y  # returns 7
x - y  # returns 1
x * y  # returns 12
x ** y # returns 64
x / y  # returns 1.333
x // y # returns 1
x % y # returns 1

x += 4  # x is 8
x -= 4  # x is 0
x *= 4  # x is 16
x /= 4  # x is 1.0
x %= 4  # x is 0

x = 4
y = 3
 
x > 2 and y > 1      # returns True
x > 5 or y <= 3      # returns True
not(x > 2 and y > 1) # returns False


#if else statements
score = 90
 
if score >= 80:
   print('You pass the course!')



#elif
   score = 70
 
if score >= 80:
   print('You pass the course with flying colors!')
 
elif score > 65:
   print('You pass the course! Talk to your instructor.')
  
else:
   print('You do not pass the course!')

   