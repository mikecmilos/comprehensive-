mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)


mylist = [x for x in mystring]
# print(mylist)

mylist = [x for x in 'word']
print(mylist)

mylist  = [num**2 for num in range(0,11,2)]
print(mylist)

r = mylist = [x for x in range(0,11) if x%2==0]
print(r)



# celzijus in farenhajt
# formula ((9/5)*temp + 32)
"""
celcius = [0,10,20,34.5]

fahrenheit = [((9/5)*temp+32) for temp in celcius]

print("     ", fahrenheit)
"""
celcius = [0,10,20,34.5]
fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp+32))
print(fahrenheit)





st = "Create a list of the first letter for every word in this string"
for word in st.split():
    if word[0].lower() == 's':
        print(word)



# use range() to print all the even numbers 0 to 10
x=list(range(0,11,2))
print(x)
# II naccin
for num in range(0,11):
    if num%2==0:
        print(num)
# III nacin 
for num in range(0,11,2):
    print(num)


# Use a list Comprehension to create a list of all numbers between 1 and 50 that
# are divisible by 3.


[x for x in range(1,51) if x%3==0]



# Go trough the string below and if the length of word is even print "even!"
lp="Create a list of the first letter of every word in this string"
for word in lp.split():
    if len(word) % 2 == 0:
        print(word+' is even!')


# create a program that prints the integers form 1 to 100. But for multiples of three print "Fizz"
# instead of number, and for the multiples of five print "Buzz" a za oba print FizzBuzz

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 ==0 :
        print('Buzz')
    else:
        print(num)




kp = "Create a list of the first letter of every word in this string"

[word[0] for word in kp.split()]




















 
