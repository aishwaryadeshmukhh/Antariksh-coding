intro = "My name is Jeff!"

print(intro[0]) # prints M

intro[0:2]              #returns 'My'
intro[-5:-1]                #returns 'Jeff'

intro1 = "My name is Jeff!"
intro2 = "Hello all!"
intro3 = "Hi there."
len(intro1) # evaluates 16
len(intro2) # evaluates 10
len(intro3) # evaluates 9


intro = "My name is Jeff!"
print(intro.lower()) # prints 'my name is jeff!'
print(intro.upper()) # prints 'MY NAME IS JEFF!'
print(intro.title()) # prints 'My Name Is Jeff!'

intro = "My name is Jeff!"
print(intro.split()) # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My ', ' is Jeff!']


#LISTS
lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]        #last element taken as 1 element
print(lst[0]) # prints abc
print(lst[4:6]) # prints [62, ['g', 'h', 'i']]


lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst2 = [0, 1, 2, 3, 4]
lst3 = ['I love sushi so much!', 'I also love curry!']
 
print(len(lst1)) # prints 6
print(len(lst2)) # prints 5
print(len(lst3)) # prints 2


lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.append(99) # appends 99 at the end of the list


lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.remove(62) # removes 62 from the list


lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.pop() # removes ['g', 'h', 'i']
lst.pop(0) # removes 'abc'

#TUPLES
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')
print(my_tuple[3:5]) # prints (456, 789)

my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

#DICTIONARIES
party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}
 
party_planning['Location'] # returns 'Our Backyard'


shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}
 
shopping_list1.update(shopping_list2)
 
print(shopping_list1) # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

shopping_list = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
 
shopping_list.keys() # returns dict_keys(['jewelry', 'clothes', 'budget'])
shopping_list.values() # returns dict_values(['earrings', 'jeans', 200])


