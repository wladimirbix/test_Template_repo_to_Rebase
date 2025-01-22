import configparser
import os


# Path to the Azure config file, typically located in the user's home directory.
AZURE_CFG_PATH = os.path.expanduser("~/.azure/config")


def _ensure_config_directory_exists():
    """Ensure that the directory for the Azure config file exists."""
    config_dir = os.path.dirname(AZURE_CFG_PATH)
    os.makedirs(config_dir, exist_ok=True)


def _read_azure_profiles():
    """Reads the Azure configuration file and returns a dictionary of profiles."""
    profiles = {}
    if os.path.exists(AZURE_CFG_PATH):
        config = configparser.ConfigParser()
        config.read(AZURE_CFG_PATH)
        for section in config.sections():
            if section.startswith("profile "):  # profile section header
                profile_name = section.split('"')[1]  # Extract profile name
                profiles[profile_name] = {
                    "subscription_id": config.get(section, "subscription_id", fallback="N/A"),
                    "tenant_id": config.get(section, "tenant_id", fallback="N/A"),
                }
    return profiles


def _write_azure_profiles(profiles):
    """Writes the profiles back to the Azure configuration file."""
    _ensure_config_directory_exists()  # Ensure directory exists before writing

    config = configparser.ConfigParser()
    for profile_name, profile_data in profiles.items():
        section_name = f'profile "{profile_name}"'
        if not config.has_section(section_name):
            config.add_section(section_name)
        config.set(section_name, "subscription_id", profile_data["subscription_id"])
        config.set(section_name, "tenant_id", profile_data["tenant_id"])

    with open(AZURE_CFG_PATH, "w") as file:
        config.write(file)


def create_profile(profile_name, subscription_id, tenant_id):
    """Create an Azure profile and write it to the config file."""
    profiles = _read_azure_profiles()

    # Check if the profile already exists
    if profile_name in profiles:
        print(f"Profile '{profile_name}' already exists.")
        return

    profiles[profile_name] = {"subscription_id": subscription_id, "tenant_id": tenant_id}

    _write_azure_profiles(profiles)
    print(f"Profile '{profile_name}' created successfully.")


def update_profile(profile_name, new_name=None, subscription_id=None, tenant_id=None):
    """Update an existing Azure profile."""
    profiles = _read_azure_profiles()

    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return

    profile_data = profiles[profile_name]

    # Update fields with new values or keep the old ones
    if subscription_id:
        profile_data["subscription_id"] = subscription_id
    if tenant_id:
        profile_data["tenant_id"] = tenant_id

    if new_name:
        profiles[new_name] = profiles.pop(profile_name)

    _write_azure_profiles(profiles)
    print(f"Profile '{profile_name}' updated successfully.")


def delete_profile(profile_name):
    """Delete an Azure profile from the config file."""
    profiles = _read_azure_profiles()

    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return

    del profiles[profile_name]
    _write_azure_profiles(profiles)
    print(f"Profile '{profile_name}' deleted successfully.")


def list_profiles():
    """List all Azure profiles stored in the config file."""
    profiles = _read_azure_profiles()
    if profiles:
        for name, details in profiles.items():
            print(f"- {name}: Subscription ID: {details['subscription_id']}")
    else:
        print("No Azure profiles found.")


def azure_cli(action):
    """Azure-specific CLI operations."""
    if action == "create_profile":
        profile_name = input("Enter profile name: ").strip()
        subscription_id = input("Enter Azure subscription ID: ").strip()
        tenant_id = input("Enter Azure tenant ID: ").strip()
        create_profile(profile_name, subscription_id=subscription_id, tenant_id=tenant_id)

    elif action == "update_profile":
        profile_name = input("Enter profile name to update: ").strip()
        new_name = input("New profile name (leave blank to keep current): ").strip()
        subscription_id = input("New subscription ID (leave blank to keep current): ").strip()
        tenant_id = input("New tenant ID (leave blank to keep current): ").strip()
        update_profile(
            profile_name,
            new_name=new_name or None,
            subscription_id=subscription_id or None,
            tenant_id=tenant_id or None,
        )

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete: ").strip()
        delete_profile(profile_name)

    elif action == "list_profiles":
        list_profiles()

    else:
        print(f"Unknown Azure action: {action}")
