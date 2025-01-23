from typing import Dict, Optional
from config_manager import load_profiles, save_profiles


def create_profile(profile_type: str, profile_name: str, **kwargs) -> None:
    """Creates a new profile for the specified platform."""
    profiles = load_profiles(profile_type)
    profiles[profile_name] = kwargs
    save_profiles(profile_type, profiles)


def update_profile(profile_type: str, profile_name: str, new_name: Optional[str] = None, **kwargs) -> None:
    """Updates an existing profile."""
    profiles = load_profiles(profile_type)
    if profile_name not in profiles:
        raise ValueError(f"Profile '{profile_name}' does not exist.")

    if new_name:
        profiles[new_name] = profiles.pop(profile_name)
        profile_name = new_name

    profiles[profile_name].update(kwargs)
    save_profiles(profile_type, profiles)


def delete_profile(profile_type: str, profile_name: str) -> None:
    """Deletes a profile."""
    profiles = load_profiles(profile_type)
    if profile_name in profiles:
        del profiles[profile_name]
        save_profiles(profile_type, profiles)
    else:
        raise ValueError(f"Profile '{profile_name}' does not exist.")


def list_profiles(profile_type: str) -> Dict[str, Dict[str, str]]:
    """Lists all profiles for the specified platform."""
    return load_profiles(profile_type)


def set_default_profile(profile_type, profile_name):
    """
    Set the specified profile as the default profile for the given platform type.

    Args:
        profile_type (str): The type of profile (e.g., 'azure', 'databricks', 'git').
        profile_name (str): The name of the profile to set as default.

    """
    profiles = load_profiles(profile_type)  # Load existing profiles (replace with actual implementation)

    if profile_name not in profiles:
        print(f"Profile '{profile_name}' does not exist. Cannot set as default.")
        return

    # Clear any existing default profile
    for name in profiles:
        profiles[name]["default"] = False

    # Set the specified profile as default
    profiles[profile_name]["default"] = True

    # Save updated profiles (replace with actual save logic)
    save_profiles(profile_type, profiles)
    print(f"Default profile set to '{profile_name}'.")
