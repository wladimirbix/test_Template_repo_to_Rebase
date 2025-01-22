import os
import json
from typing import Dict
from config_manager import get_config_file_path


def create_profile() -> None:
    """Creates a new Databricks profile."""
    profile_name = input("Enter profile name: ")
    host_name = input("Enter Databricks host: ")
    token = input("Enter Databricks token: ")

    config_path = get_config_file_path()
    profiles = _load_profiles(config_path)
    profiles[profile_name] = {"host": host_name, "token": token}

    _save_profiles(config_path, profiles)
    print(f"Profile '{profile_name}' created successfully.")


def update_profile() -> None:
    """Updates an existing Databricks profile."""
    profile_name = input("Enter profile name to update: ")
    config_path = get_config_file_path()
    profiles = _load_profiles(config_path)

    if profile_name in profiles:
        host_name = input("Enter new Databricks host: ")
        token = input("Enter new Databricks token: ")
        profiles[profile_name].update({"host": host_name, "token": token})
        _save_profiles(config_path, profiles)
        print(f"Profile '{profile_name}' updated successfully.")
    else:
        print(f"Profile '{profile_name}' not found.")


def delete_profile() -> None:
    """Deletes a Databricks profile."""
    profile_name = input("Enter profile name to delete: ")
    config_path = get_config_file_path()
    profiles = _load_profiles(config_path)

    if profile_name in profiles:
        del profiles[profile_name]
        _save_profiles(config_path, profiles)
        print(f"Profile '{profile_name}' deleted successfully.")
    else:
        print(f"Profile '{profile_name}' not found.")


def list_profiles() -> None:
    """Lists all Databricks profiles."""
    config_path = get_config_file_path()
    profiles = _load_profiles(config_path)

    if profiles:
        print("Available profiles:")
        for name, details in profiles.items():
            print(f"- {name}: {details}")
    else:
        print("No profiles found.")


def set_default_profile() -> None:
    """Sets a profile as the default Databricks profile."""
    profile_name = input("Enter profile name to set as default: ")
    config_path = get_config_file_path()
    profiles = _load_profiles(config_path)

    if profile_name in profiles:
        profiles["default"] = profiles[profile_name]
        _save_profiles(config_path, profiles)
        print(f"Profile '{profile_name}' set as default.")
    else:
        print(f"Profile '{profile_name}' not found.")


def _load_profiles(config_path: str) -> Dict[str, Dict[str, str]]:
    """Loads Databricks profiles from the configuration file."""
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}


def _save_profiles(config_path: str, profiles: Dict[str, Dict[str, str]]) -> None:
    """Saves Databricks profiles to the configuration file."""
    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(profiles, file, indent=4)
