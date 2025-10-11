from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("James", "Michelson") == "Michelson; James"
    assert make_full_name("Baden", "Powell") == "Powell; Baden"
    assert make_full_name("Gabe", "Newell") == "Newell; Gabe"

def test_extract_family_name():
    assert extract_family_name("Michelson; James") == "Michelson"
    assert extract_family_name("Powell; Baden") == "Powell"
    assert extract_family_name("Newell; Gabe") == "Newell"

def test_extract_given_name():
    assert extract_given_name("Michelson; James") == "James"
    assert extract_given_name("Powell; Baden") == "Baden"
    assert extract_given_name("Newell; Gabe") == "Gabe"

pytest.main(["-v", "--tb=line", "-rN", "week03/code_along/test_names.py"])