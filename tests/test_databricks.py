import unittest
from unittest.mock import patch
from databricks import create_profile, update_profile, delete_profile, list_profiles, set_default_profile


class TestDatabricks(unittest.TestCase):
    @patch("builtins.input", side_effect=["test_profile", "test_host", "test_token"])
    @patch("unicon.databricks._save_profiles")
    @patch("unicon.databricks._load_profiles", return_value={})
    def test_create_profile(self, mock_load, mock_save, mock_input):
        """Test creating a new Databricks profile."""
        create_profile()
        mock_save.assert_called_once()
        saved_profiles = mock_save.call_args[0][1]
        self.assertIn("test_profile", saved_profiles)
        self.assertEqual(saved_profiles["test_profile"], {"host": "test_host", "token": "test_token"})

    # Add similar tests for update_profile, delete_profile, list_profiles, set_default_profile


if __name__ == "__main__":
    unittest.main()
