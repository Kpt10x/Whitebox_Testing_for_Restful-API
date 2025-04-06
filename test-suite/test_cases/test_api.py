import requests
import unittest
import os
import sys
from hypothesis import given, strategies as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../api/sample-api/src")))

from app import app  

BASE_URL = "http://127.0.0.1:5000"

class TestAPI(unittest.TestCase):
    
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)  # Expect a list instead of dict

    def test_create_and_get_user(self):
        new_user = {"name": "Charlie", "age": 28}
        post_response = requests.post(f"{BASE_URL}/users", json=new_user)
        self.assertEqual(post_response.status_code, 201)

        user_id = post_response.json().get("id")
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Charlie")

    def test_invalid_user(self):
        response = requests.get(f"{BASE_URL}/users/9999")  # Assuming 9999 does not exist
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.json())

    def test_create_user_invalid(self):
        response = requests.post(f"{BASE_URL}/users", json={"name": "TestUser"})
        self.assertEqual(response.status_code, 400)

    @given(name=st.text(min_size=1, max_size=50), age=st.integers(min_value=18, max_value=100))
    def test_create_user(self, name, age):
        response = requests.post(f"{BASE_URL}/users", json={"name": name, "age": age})
        self.assertIn(response.status_code, [201, 400])  # Expect success or validation error

    @given(user_id=st.integers(min_value=1, max_value=10000))
    def test_get_user(self, user_id):
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        self.assertIn(response.status_code, [200, 404])  # User exists or not found

    @given(user_id=st.integers(min_value=1, max_value=10000))
    def test_delete_user(self, user_id):
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        self.assertIn(response.status_code, [200, 404])  # Deleted or not found

    @given(user_id=st.integers(min_value=1, max_value=10000), name=st.text(min_size=1, max_size=50))
    def test_update_user(self, user_id, name):
        response = requests.put(f"{BASE_URL}/users/{user_id}", json={"name": name})
        self.assertIn(response.status_code, [200, 404, 400])  # Updated, not found, or validation error

if __name__ == "__main__":
    unittest.main()
