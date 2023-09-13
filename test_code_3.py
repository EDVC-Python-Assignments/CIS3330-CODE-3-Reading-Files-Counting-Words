import os,sys
import random
import pytest
from code_3 import test_word_a
from code_3 import test_word_b
from code_3 import test_word_c
from code_3 import test_word_d
from code_3 import test_number_of_words

def check_if_file_exists():
    try:
        exists = os.path.exists("code_3.py")
        assert exists == True
    except:
        sys.exit()

def test_word_a():
    pass

def test_word_b():
    pass

def test_word_c():
    pass

def test_word_d():
    pass

def test_number_of_words():
    pass