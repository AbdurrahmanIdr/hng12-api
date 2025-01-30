import unittest
import json
from app import create_app


class APITestCase(unittest.TestCase):
    """Test case for the Flask API endpoints."""

    def setUp(self):
        """Set up the test client before each test."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_info(self):
        """Test the GET request to '/' endpoint."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertIn("email", data)
        self.assertIn("current_datetime", data)
        self.assertIn("github_url", data)

        # Ensure the email and GitHub URL are correctly formatted
        self.assertIsInstance(data["email"], str)
        self.assertTrue(data["email"].endswith("@gmail.com") is True)

        self.assertIsInstance(data["github_url"], str)
        self.assertTrue(data["github_url"].startswith("https://github.com/"))

        # Ensure datetime is in ISO 8601 format
        self.assertIsInstance(data["current_datetime"], str)
        self.assertTrue(data["current_datetime"].endswith("Z"))


if __name__ == "__main__":
    unittest.main()
