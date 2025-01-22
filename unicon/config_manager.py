import os


def get_config_file_path() -> str:
    """Gets the path to the Databricks profiles configuration file."""
    config_dir = os.path.expanduser("~/.unicon")
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "databricks_profiles.json")
