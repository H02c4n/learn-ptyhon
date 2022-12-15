

word = "Django"

word[0] #D
word[2] #a
word[3] #n
word[5] #0
print( word[-5] ) #j



word[:2]  # 'Dj'
word[4:]  # 'go'
print( word[-5:] ) # 'jango'


len(word) #6

print( 'rin'+2*'tin')  #rintintin

hello = "Hello, world!"

 # The strip() method removes any whitespace from the beginning or the end.
with_whitespaces = " Hello, World! "
with_whitespaces.strip() # "Hello, World!"

# The len() method returns the length of a string.
len(hello) # 13

# The lower() method returns the string in lower case.
hello.lower() # 'hello, world!'

# The upper() method returns the string in upper case.
hello.upper() # 'HELLO, WORLD!'

# The replace() method replaces a string with another string.
hello.replace('H', 'J') # 'Jello, World!'

# The split() method splits the string into substrings if it finds instances of the separator.
hello.split(',') # ['Hello', ' World!']

# Converts the first character to upper case

'low letter at the beginning'.capitalize() 
# 'Low letter at the beginning'

# Returns the number of times a specified value occurs in a string.

'low letter at the beginning'.count('t') # 4

# Searches the string for a specified value and returns the position of where it was found.

'Hello, welcome to my world'.find('welcome') # 7

# Converts the first character of each word to upper case

'Welcome to my world'.title() # 'Welcome To My World'

# Returns a string where a specified value is replaced with a specified value.

'I like bananas'.replace('bananas', 'apples') 
# 'I like apples'

# Joins the elements of an iterable to the end of the string.

my_tuple = ('John', 'Peter', 'Vicky')

', '.join(my_tuple) 
# 'John, Peter, Vicky'

# Returns True if all characters in the string are upper case.

'ABC'.isupper()
not 'AbC'.isupper()

# Check if all the characters in the text are letters.

'CompanyX'.isalpha()
not 'Company 23'.isalpha()

# Returns True if all characters in the string are decimals.

'1234'.isdecimal()
not 'a21453'.isdecimal()

# f string

year = 2018
event = 'conference'

print( f'Results of the {year} {event}' )

# 'Results of the 2018 conference'

# String format
msg = "hello"
name = "ahmet"

print( '{} from our member {}'.format(msg, name) )  

# hello from our member ahmet