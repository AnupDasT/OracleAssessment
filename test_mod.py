# write the Pytest fixture script to validate the GET request APi https://reqres.in/api/users?page=2
import pytest
import requests


@pytest.fixture
def get_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    assert response.status_code == 200, "Failed to fetch users data"
    return response.json()


def test_get_users(get_users):
    users_data = get_users
    assert "data" in users_data, "No data found in the response"
    assert len(users_data["data"]) > 0, "No users found in the response"
    assert users_data["page"] == 2, "Incorrect page number in the response"
    print(users_data)
    print("Test passed successfully!")

#verify the response Json data 'per_page': 6
def test_per_page(get_users):
    users_data = get_users
    assert users_data["per_page"] == 6, "Incorrect 'per_page' value in the response"
    print("Test passed successfully!")
    print(users_data)

