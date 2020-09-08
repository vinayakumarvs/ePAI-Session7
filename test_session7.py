import importlib
import inspect
import os
import re

import pytest

import session7


README_CONTENT_CHECK_FOR = ["lambda","reduce","partial","list comprehension","zip","filter"]

FUNC_CHECK_FOR = ["fibonacci",
"evenodd_add",
"remove_vowel",
"relu_ai",
"sigmoid_ai",
"shift_char_5",
"profanity_check",
"add_even",
"biggest_char",
"add_third_no",
"gen_kanumber_plate",
"gen_number_plate"]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 6

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_are_defined():
    content = inspect.getsource(session7)
    AllFUNCTIONSDEFINED = True
    for c in FUNC_CHECK_FOR:
        if c not in content:
            AllFUNCTIONSDEFINED = False
            pass
    assert AllFUNCTIONSDEFINED == True, "You have not defined all the required functions"



def test_fibonnaci_positive():
    assert True== session7.fibonacci(2), "Fibonnaci function not working"

def test_evenodd_add():
    l1 = [1,2,3,4]
    l2 = [1,2,3,4]
    assert [] == session7.evenodd_add(l1,l2), "evenodd_add is not working properly"

def test_remove_vowel():
    assert 'vny' == session7.remove_vowel('vinay'),"remove_vowel is not working properly"

def test_relu():
    list = [1,2,3,4,5.00,0,-1,-2,-3]
    assert [1,2,3,4,5.0,0,0,0,0] == session7.relu_ai(list),"relu_ai is not working properly"

def test_sigmoid():
    list = [1,2.00, 3.00, -4,-5.0]
    assert [0.7310585786300049,
 0.8807970779778823,
 0.9525741268224334,
 0.01798620996209156,
 0.0066928509242848554] == session7.sigmoid_ai(list), "sigmoid_ai is not working"

def test_shift5char():
    assert 'ansfd' == session7.shift_char_5('vinay'), "shift_char_5 is not working"

def test_add_even():
    l1 = [1,2,3,4,5]
    assert 6 == session7.add_even(l1), "add_even is not working"

def test_biggest_char():
    assert 'y' == session7.biggest_char('VINAYvinay'), "biggest_char is not working"

def test_add_third_no():
    assert 3 == session7.add_third_no([1,2,3,4,5]), "add_third_no is not working"

def test_gen_kanumber_plate():
    assert bool(session7.gen_kanumber_plate()),"gen_kanumber_plate is not working"

def test_gen_number_plate():
    assert bool(session7.gen_number_plate("MH")), "gen_number_plate is not working"

def test_profanity_check():
    assert session7.profanity_check('There is a large selection of short moral stories for kids online. They range from the classics like The Boy Who Cried Wolf, to somber ones talking about greed. To help you out, we’ve gathered a selection of the most 20 popular stories.'), "profanity_check function is not working properly"