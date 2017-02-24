import pytest
def func(i):
	return i
def test_func():
	print('test jenkins')
	assert func(3)==2