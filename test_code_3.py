import os,sys
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

def test_word_great():
    # If your code is returning 26060 it is because your code is case sensitive
    assert get_number_of_great() == 43379
def test_word_recommend():
    # If your code is returning 9296 it is because your code is case sensitive
    assert get_number_of_recommend() == 9496
def test_word_free():
    # If your code is returning 2276 it is because your code is case sensitive
    assert get_number_of_free() == 2681 
def test_word_office():
    # If your code is returning 5335 it is because your code is case sensitive
    assert get_number_of_office() == 7692
def test_number_of_words():
    assert get_number_of_products() == 113412