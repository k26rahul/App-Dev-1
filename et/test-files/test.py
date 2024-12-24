import pytest


@pytest.fixture
def sample_data():
  return {"name": "John", "age": 30}


def test_example(sample_data):
  assert sample_data["name"] == "John"


test_example()

# import sys

# input_list = sys.argv

# var_a, var_b = input_list[1], input_list[2]

# if input_list[1] == 'meera':
#   var_b = 'data analyst'
# elif input_list[1] == 'radha':
#   var_b = 'scientist'

# print(f'{var_a} is {var_b}')
