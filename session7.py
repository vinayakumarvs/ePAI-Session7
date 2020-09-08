from functools import reduce, partial
import numpy as np
import requests
import random
import string

# tell whether a number is a Fibonacci number or not
def fibonacci(n):
    '''the function can tell whether a number is a Fibonacci number or not'''
    fbnc = lambda x: reduce(lambda y, _: y+[y[-1]+y[-2]], range(x-2),[0,1])
    fbnc_list = fbnc(10000)
    return bool(list(filter(lambda y : y in [n],fbnc_list))) 

# add 2 iterables a and b such that a is even and b is odd
def evenodd_add(l1,l2):
    '''add two numbers a and b only if a is even and b is odd'''
    return [a+b for a,b in zip (l1,l2) if a % 2 == 0 and b % 2 != 0]

# strips every vowel from a string provided (tsai>>t s)
def remove_vowel(str):
    '''the function will remove vowels from a string provided'''
    return "".join(txt for txt in str if txt not in ['a','e','i','o','u'])

# acts like a ReLU function for a 1D array
def relu_ai(lst):
    '''shows negative numbers as 0 and positive numbers as it is: like Relu function'''
    return [0 if n < 0 else n for n in lst]

# acts like a sigmoid function for a 1D array
def sigmoid_ai(l):
    ''' works like a sigmoid function'''
    sig_lst = [1/(1+np.exp(-n)) for n in l]
    return sig_lst

# takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
shift_char_5 = lambda s : ''.join(chr((ord(char) - 97 + 5) % 26 + 97) for char in s)

# checks whether it has any of the swear words mentioned
def profanity_check(passage:'string') -> 'checks for validating profanity words':
    target_url=' https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt'
    response = requests.get(target_url)
    checked_list = [i for i in passage.split() if i not in response.text]
    return bool(checked_list)

# add only even numbers in a list
add_even = lambda n: reduce(lambda a,b: a+b if b%2==0  else a,n,0)

# find the biggest character in a string (printable ascii characters)
biggest_char = lambda n: reduce(lambda a,b: a if ord(a) > ord(b) else b,n)

# adds every 3rd number in a list
add_third_no = lambda n : reduce(lambda a,b: a+b if (n.index(b)+1) %3 ==0 else a,n,0)

# KA random 15 number plates
def gen_kanumber_plate() -> 'generates karnataka number plates':
    return ['KA' + str(random.randint(10,100)) + random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase) + str(random.randint(1000,10000)) for i in range(15)]

# number plate Generator
def gen_flex_num_plate(state_code,area_code,alpha_code,reg_no):
    return state_code + str(area_code) + alpha_code + str(reg_no)

reg_num = partial(gen_flex_num_plate,area_code = random.randint(10,99),alpha_code = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase), reg_no = random.randint(1000,10000))

def gen_number_plate(state_code):
    return [reg_num(state_code) for i in range(15)]