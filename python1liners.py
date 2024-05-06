#Python one liner utility functions



#=============================================================
# Generate a Random Number between.. 
#=============================================================
import random

def randnum(min, max):
    return round(random.uniform(min, max))

print(randnum(1, 7))  # Outputs a random number between 1 and 7



#=============================================================
# Check first value in an array 
#=============================================================
import numpy as np

def is_first_biggest(xs):
    return xs[0] == sorted(xs, reverse=True)[0]

print(is_first_biggest([20.1, 5, 4, 3, 2, 1]))  # True




#=============================================================
# Remove item from an array
#=============================================================
def remove_array_item(array, item):
    return [x for x in array if x != item]

print( remove_array_item(['red', 'blue', 'green', 'tan'], 'tan') ) #=> ['red','blue','green']



#=============================================================
# Random step counting by..... 
#=============================================================
import random

def rand_step(min, max, step):
    return min + (step * int(random.random() * (max - min) / step))

print( rand_step(0, 100, 20)) #=> 0,20,40,60,80



#=============================================================
# Get random item from an array 
#=============================================================
import random

def get_rand_array_item(arr):
    return random.choice(arr)

print(get_rand_array_item(['red', 'blue', 'green', 'tan']))  #=> green




#=============================================================
# Check array for specific item
#=============================================================
def array_has_item(array, item):
    return item in array

print( array_has_item(['orange', 'red', 'blue'], 'blue') ) #=> True




#=============================================================
# Shuffle an array
#=============================================================
import random

def shuffle_array(arr):
    return sorted(arr, key=lambda x: random.random() - 0.5)

print( shuffle_array(['a','b','c','d']) ) #=> ['d','a','c','b']





#=============================================================
# Sort an array
#=============================================================
def my_sort(*args):
    return sorted(args)

print( my_sort(10, 2, 3) ) #=> [2, 3, 10]





#=============================================================
# Break down an array into chunks
#=============================================================
def chunk_array(arr, size):
    return [arr[i:i + size] for i in range(0, len(arr), size)]

print(chunk_array([1, 2, 3, 4, 5, 9, 8, 7], 3))  #=> [[1, 2, 3], [4, 5, 9], [8, 7]]




#=============================================================
# Create range
#=============================================================
def create_range(start, end):
    return list(range(start, end + 1))
    
print( create_range(5,10) ) #=> [5, 6, 7, 8, 9, 10]
print( create_range(5,10)[::-1] ) #=> [10, 9, 8, 7, 6, 5]







#=============================================================
# Check if array is empty
#=============================================================
def check_empty_array(arr):
    return not isinstance(arr, list) or len(arr) == 0
    
    
print( check_empty_array([]) )	  #=> True
print( check_empty_array([""]) )  #=> False





#=============================================================
# Find similarity in an array
#=============================================================
def find_similarity(arr, values):
    return [v for v in arr if v in values]

print( find_similarity([1,2,3], [1,2,4]) ) #=> [1,2]



#=============================================================
# Count occurences in an array
#=============================================================
def count_occurrences(arr, value):
    return sum(1 for v in arr if v == value)

print( count_occurrences([7,7,7,1,1,2,1,2,3,7], 7) ) #=> 4    
print( count_occurrences(list(map(str.lower,["cat", "dog", "moose", "Cat"])), "cat") ) #=> 2
    


#=============================================================
# Loop through an array 
#=============================================================
upper_case = list(map(lambda x: x.upper(), ['apple', 'banana', 'cherry']))
print(upper_case) #=> ['APPLE', 'BANANA', 'CHERRY']




#=============================================================
# flatten an array 
#=============================================================
def flatten_array(arr):
    return [y for x in arr for y in (flatten_array(x) if isinstance(x, list) else [x])]

print( flatten_array([1,[2],3,4,[10,20,30,40], 90]) ) #=> [1, 2, 3, 4, 10, 20, 30, 40, 90]



#=============================================================
# Zip Function
#=============================================================
students = ['Dilli', 'Vikram', 'Rolex', 'Leo']
grades = [85, 92, 78, 88]

student_grade_pairs = list(zip(students, grades))
print(student_grade_pairs) #=> [('Dilli', 85), ('Vikram', 92), ('Rolex', 78), ('Leo', 88)]





#=============================================================
# Enumerate Function
#=============================================================
grocery_list = ['Apples', 'Milk', 'Bread', 'Eggs', 'Cheese']

for index, item in enumerate(grocery_list):
    print(f"{index}. {item}")

#0. Apples
#1. Milk
#2. Bread
#3. Eggs
#4. Cheese




#=============================================================
# Unpacking List
#=============================================================
numbers = [1, 2, 3]

a, b, c = numbers

print(a, b, c) #=> 1 2 3





#=============================================================
# Convert object to array and array to object
#=============================================================
def obj_to_array(obj):
    return [obj[key] for key in obj.keys()]

def array_to_object(arr, key_field):
    return {item[key_field]: item for item in arr}
    
our_data = {
    "123456a": {
        "name": "tim",
        "age": 40,
        "city": "Farmtown"
    },
    "123456b": {
        "name": "jerry",
        "age": 40,
        "city": "Beachroad"
    },
    "123456c": {
        "name": "bob",
        "age": 30,
        "city": "Busyville"
    }
}


print( obj_to_array(our_data) )

#[{'name': 'tim', 'age': 40, 'city': 'Farmtown'}, {'name': 'jerry', 'age': 40, 'city': 'Beachroad'}, {'name': 'bob', 'age': 30, 'city': 'Busyville'}]


print( array_to_object(obj_to_array(our_data), "city") ) 

#{'Farmtown': {'name': 'tim', 'age': 40, 'city': 'Farmtown'}, 'Beachroad': {'name': 'jerry', 'age': 40, 'city': 'Beachroad'}, 'Busyville': {'name': 'bob', 'age': 30, 'city': 'Busyville'}}





#=============================================================
# Sum up value in an object
#=============================================================
arr_obj = [
    {"name": "Dayana", "likes": 300},
    {"name": "Sarah", "likes": 100},
    {"name": "Samantha", "likes": 50}
]

result = sum(map(lambda d: sum([d["likes"]]), arr_obj))
print(result) #=> 450




#=============================================================
# Dictionary
#=============================================================
def search_dic(name):
    the_dict = {'red': '#ff4444', 'blue': '#3b5998', 'yellow': '#fff68f'}
    return the_dict[name]

print( search_dic('red') ) # => '#ff4444'



#=============================================================
# Check if number is odd
#=============================================================
def is_odd(num):
    return True if num % 2 != 0 else False

print( is_odd(7) ) #=> True




#=============================================================
# Check if number is even
#=============================================================
def iseven(num):
    return False if num % 2 != 0 else True

print( iseven(4) ) #=> True



#=============================================================
# Get average
#=============================================================
def get_average(tests):
    return sum(tests) / len(tests)

print( get_average([10, 20, 30]) ) #=> 20.0





#=============================================================
# Sum Over Every Other Value Python One-Liner
#=============================================================
sum(stock_prices[::2])




#=============================================================
# Return index number
#=============================================================
lst = [1, 2, 3, 'Alice', 'Alice']
indices = [i for i in range(len(lst)) if lst[i]=='Alice']
print(indices) # [3, 4]




#=============================================================
# Multiply All
#=============================================================
from functools import reduce
def calculate(*n):
    return reduce(lambda a, b: a * b, n)
    
print(calculate(10,10,20)) #=> 2000



#=============================================================
# CSV file to json
#=============================================================
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"



#=============================================================
# Compress CSS file
#=============================================================
python -c 'import re,sys;print re.sub("\s*([{};,:])\s*", "\\1", re.sub("/\*.*?\*/", "", re.sub("\s+", " ", sys.stdin.read())))'



#=============================================================
# This can be used to convert a string into a "url safe" string
#=============================================================
python -c "import urllib, sys ; print urllib.quote_plus(sys.stdin.read())";



#==================================================================================
# Encrypt string
#==================================================================================
from hashlib import sha256

input_ = input('Enter something: ')
print(sha256(input_.encode('utf-8')).hexdigest())




#==================================================================================
# IP address to decimal conversion
#==================================================================================
from functools import reduce

def ip_converter(ip_or_int):
    return '.'.join(str((ip_or_int >> (8 * i)) & 0xFF) for i in range(3, -1, -1)) if isinstance(ip_or_int, int) else sum(int(byte) << (8 * (3 - i)) for i, byte in enumerate(ip_or_int.split('.'))) if isinstance(ip_or_int, str) else ValueError("Input must be either a string representing an IP address or an integer.")


print( ip_converter('8.8.8.8') ) #=> returns decimal 134744072
print( ip_converter(387591167) ) #=> returns ip 23.26.43.255



#==================================================================================
# Scytale Cipher - https://en.wikipedia.org/wiki/Scytale
#==================================================================================
plaintext = "Iamhurtverybadlyhelp"
plaintext2 = "Iryyatbhmvaehedlurlp"
'''
  |   |   |   |   |   |  |
       | I | a | m | h | u |  |
     __| r | t | v | e | r |__|
    |  | y | b | a | d | l |
    |  | y | h | e | l | p |
    |  |   |   |   |   |   |
'''
plaintext3 = "howdoesthiswork" 
plaintext4 = "hdsioootsrwehwk"
'''
  |   |   |   |   |   |
       | H | O | W |  |
     __| D | O | E |__|
    |  | S | T | H |
    |  | I | S | W |
    |  | O | R | K |
'''
def encrypt(rows, plaintext):
    assert len(plaintext) % rows == 0
    n = len(plaintext)
    columns = n // rows
    ciphertext = ['-'] * n
    for i in range(n):
        row, col = i // columns, i % columns
        ciphertext[col * rows + row] = plaintext[i]
    return "".join(ciphertext)

def decrypt(rows, ciphertext):
    assert len(ciphertext) % rows == 0
    return encrypt(len(ciphertext) // rows, ciphertext)
    
print(decrypt(5, plaintext)) #=> Iryyatbhmvaehedlurlp
print(encrypt(3, plaintext4)) #=> howdoesthiswork
