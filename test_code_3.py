import os,sys
import random
import pytest
from code_3 import get_number_of_great
from code_3 import get_number_of_recommend
from code_3 import get_number_of_free
from code_3 import get_number_of_office
from code_3 import get_number_of_products

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