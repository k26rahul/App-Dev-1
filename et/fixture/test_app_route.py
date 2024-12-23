import pytest
import requests


@pytest.fixture  # fixture ~ attachment
def get_response():
  resp = requests.get("http://127.0.0.1:5000/greet/IITM")
  return resp


def test_response(get_response):
  assert get_response.text == "Hello, IITM"
