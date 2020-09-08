# Session 7 - First Class Functions Part - II
# EPAi Session7 assignment

#### Objective of Assignment:

1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000

2. Using list comprehension (and zip/lambda/etc if required) write an expression that: 

    a. add 2 iterables a and b such that a is even and b is odd

    b. strips every vowel from a string provided (tsai>>t s)

    c. acts like a ReLU function for a 1D array

    d. acts like a sigmoid function for a 1D array
    
    e.Takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

3. A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt 

4. Using reduce function:
    a. add only even numbers in a list
    b. find the biggest character in a string (printable ascii characters)
    c. adds every 3rd number in a list

5. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 

6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided 




## Functions Defined:

* fibonacci:
    Generates Fibonacci number given for a range passed in as a parameter.

* evenodd_add:
Add 2 iterables a and b such that a is even and b is odd

* remove_vowel:
Strips every vowel from a string provided

* relu_ai:
acts like Relu function

* sigmoid_ai:
acts like a sigmoid function

* shift_char_5: Takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

* profanity_check: A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned

* add_even: add only even numbers in a list

* biggest_char: find the biggest character in a string (printable ascii characters)

* add_third_no: adds every 3rd number in a list

* gen_kanumber_plate: an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets.

* gen_number_plate: an expression where KA can be changed to MH, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided 