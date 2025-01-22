import os


# Path to the .databrickscfg file, typically located in the user's home directory.
DATABRICKS_CFG_PATH = os.path.expanduser("~/.databrickscfg")


def _read_databricks_profiles():
    """Reads the .databrickscfg file and returns a dictionary of profiles."""
    profiles = {}
    if os.path.exists(DATABRICKS_CFG_PATH):
        with open(DATABRICKS_CFG_PATH, "r") as file:
            lines = file.readlines()
            profile_name = None
            profile_data = {}
            for line in lines:
                line = line.strip()
                if line.startswith("["):  # profile section header
                    if profile_name:
                        profiles[profile_name] = profile_data
                    profile_name = line[1:-1]
                    profile_data = {}
                elif "=" in line:
                    key, value = line.split("=", 1)
                    profile_data[key.strip()] = value.strip()
            if profile_name:
                profiles[profile_name] = profile_data  # last profile
    return profiles


def _write_databricks_profiles(profiles):
    """Writes the profiles back to the .databrickscfg file."""
    with open(DATABRICKS_CFG_PATH, "w") as file:
        for profile_name, profile_data in profiles.items():
            file.write(f"[{profile_name}]\n")
            for key, value in profile_data.items():
                file.write(f"{key} = {value}\n")
            file.write("\n")


def create_profile(profile_name, host, token):
    """Create a Databricks profile and write it to the .databrickscfg file."""
    profiles = _read_databricks_profiles()

    # Check if the profile already exists
    if profile_name in profiles:
        print(f"Profile '{profile_name}' already exists.")
        return

    profiles[profile_name] = {"host": host, "token": token}  # Add new profile

    _write_databricks_profiles(profiles)
    print(f"Profile '{profile_name}' created successfully.")


def update_profile(profile_name, new_name=None, host=None, token=None):
    """Update an existing Databricks profile."""
    profiles = _read_databricks_profiles()

    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return

    profile_data = profiles[profile_name]

    # Update fields with new values or keep the old ones
    if host:
        profile_data["host"] = host
    if token:
        profile_data["token"] = token

    if new_name:
        profiles[new_name] = profiles.pop(profile_name)

    _write_databricks_profiles(profiles)
    print(f"Profile '{profile_name}' updated successfully.")


def delete_profile(profile_name):
    """Delete a Databricks profile from the .databrickscfg file."""
    profiles = _read_databricks_profiles()

    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return

    del profiles[profile_name]
    _write_databricks_profiles(profiles)
    print(f"Profile '{profile_name}' deleted successfully.")


def list_profiles():
    """List all profiles stored in the .databrickscfg file."""
    profiles = _read_databricks_profiles()
    return profiles


def databricks_cli(action):
    """Databricks-specific CLI operations."""
    if action == "create_profile":
        profile_name = input("Enter profile name: ").strip()
        host = input("Enter Databricks host: ").strip()
        token = input("Enter Databricks token: ").strip()
        create_profile(profile_name, host=host, token=token)

    elif action == "update_profile":
        profile_name = input("Enter profile name to update: ").strip()
        new_name = input("New profile name (leave blank to keep current): ").strip()
        host = input("New host (leave blank to keep current): ").strip()
        token = input("New token (leave blank to keep current): ").strip()
        update_profile(profile_name, new_name=new_name, host=host, token=token)

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete: ").strip()
        delete_profile(profile_name)

    elif action == "list_profiles":
        profiles = list_profiles()
        if profiles:
            for name, details in profiles.items():
                print(f"- {name}: Host: {details['host']}")
        else:
            print("No Databricks profiles found.")
    else:
        print(f"Unknown Databricks action: {action}")
