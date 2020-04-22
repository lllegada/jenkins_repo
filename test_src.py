import pytest

def practice_func():
	user_json = {
	'first_name' : 'Peppa',
	'last_name' : 'Pig',
	'occupation' : 'Tik Tok Master'
	}
	return user_json

@pytest.mark.sc1
def test_user():
	json_payload = practice_func()
	assert json_payload['first_name'] == 'Peppa'

@pytest.mark.sc1
def test_prac_1():
	assert 1 == 3

@pytest.mark.sc2
def test_prac_2():
	assert 2 == 2

@pytest.mark.sc2
def test_prac_3():
	assert 3 == 3