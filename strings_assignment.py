#1

st = 'Python Programming'
x = st.lower()
y = x.replace('python','Python')
print(y)

#output:Python programming

#2

txt = 'Python is powerful and easy'
words = txt.split(' ')
l = len(words)
print(l)

#optput:5

#3.	What would be the output from the following Python program section?

st = ['P','y','t','h','o','n']
w=''.join(st)
print(w)

#output:Python

#4.	How to check if a String contains only digits?

s1 = "abc123"
s2 = "123456"
print(s1.isdigit())
print(s2.isdigit())

# output: False True

# 5.	How to count number of vowels and consonants in a String?

s = "E Abbai Chala Manchodu"
vowels = 'aeiouyAEIOUY'
consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
v = 0
c= 0
for char in s:
	if char in vowels:
		v += 1
	elif char in consonants:
		c += 1
print("No. of Vowels:",v)
print("No. of Consonants:",c)

#Output: No. of Vowels: 9
# No. of Consonants: 10

# 6.	How to replace each given character to other e.g. blank with %20? 

s = 'Welcome to Python Programming'
print(s.replace(' ','%20'))

# output:Welcome%20to%20Python%20Programming

# 7.	How to check if String is Palindrome?

s1 = "madam"

#Palindome of s1 string
pal_s1 = s1[::-1]

if s1 == pal_s1:
	print(True)
else:
	print(False)

output: True

# 8.You are given a string. Your task is to capitalize each word of the string

s = "Welcome to python programming world"
print(s.title())

# 9.You need to write a function to implement an algorithm which will accept a string of characters and should find the highest occurrence of the character and display it.
#  For example, if input is "aaaaaaaaaaaaaaaaabbbbcddddeeeeee" it should return "a".

s = 'adgigora chudu aakathayiro'
d = {}
for value in s:
	if value not in d:
		d[value] = s.count(value)
print(d)
maxval = 0
maxkey = ''
for key,value in d.items():
	if maxval < value:
		maxval = value
		maxkey = key
print("Maximum Occured Character is:",maxkey)

# output:{'a': 6, 'd': 2, 'g': 2, 'i': 2, 'o': 2, 'r': 2, ' ': 2, 'c': 1, 'h': 2, 'u': 2, 'k': 1, 't': 1, 'y': 1}
# Maximum Occured Character is: a

# 10.How to count occurrence of a given character in String?

s = "This is a string"
d= {}
for char in s:
	if char not in d:
		d[char] = s.count(char)
print(d)

# output: {'T': 1, 'h': 1, 'i': 3, 's': 3, ' ': 3, 'a': 1, 't': 1, 'r': 1, 'n': 1, 'g': 1}
