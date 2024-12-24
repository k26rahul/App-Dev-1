import pytest


@pytest.fixture
def sample_data():
  return {"name": "John", "age": 30}


def test_example(sample_data):
  assert sample_data["name"] == "John"
