import configparser
import os


def get_gitconfig_path():
    """Retrieve the path to the user's .gitconfig file."""
    home_dir = os.path.expanduser("~")
    return os.path.join(home_dir, ".gitconfig")


def create_profile(profile_name, username, token):
    """Create a Git profile in the .gitconfig file."""
    config_path = get_gitconfig_path()
    config = configparser.ConfigParser()
    config.read(config_path)

    section_name = f'profile "{profile_name}"'
    if not config.has_section(section_name):
        config.add_section(section_name)

    config.set(section_name, "username", username)
    config.set(section_name, "token", token)

    with open(config_path, "w") as configfile:
        config.write(configfile)

    print(f"Profile '{profile_name}' created successfully.")


def update_profile(profile_name, new_name=None, username=None, token=None):
    """Update an existing Git profile in the .gitconfig file."""
    config_path = get_gitconfig_path()
    config = configparser.ConfigParser()
    config.read(config_path)

    section_name = f'profile "{profile_name}"'
    if not config.has_section(section_name):
        print(f"Profile '{profile_name}' does not exist.")
        return

    if new_name:
        new_section_name = f'profile "{new_name}"'
        config.add_section(new_section_name)
        for key, value in config.items(section_name):
            config.set(new_section_name, key, value)
        config.remove_section(section_name)
        section_name = new_section_name

    if username:
        config.set(section_name, "username", username)
    if token:
        config.set(section_name, "token", token)

    with open(config_path, "w") as configfile:
        config.write(configfile)

    print(f"Profile '{profile_name}' updated successfully.")


def delete_profile(profile_name):
    """Delete a Git profile from the .gitconfig file."""
    config_path = get_gitconfig_path()
    config = configparser.ConfigParser()
    config.read(config_path)

    section_name = f'profile "{profile_name}"'
    if config.has_section(section_name):
        config.remove_section(section_name)
        with open(config_path, "w") as configfile:
            config.write(configfile)
        print(f"Profile '{profile_name}' deleted successfully.")
    else:
        print(f"Profile '{profile_name}' does not exist.")


def list_profiles():
    """List all Git profiles in the .gitconfig file."""
    config_path = get_gitconfig_path()
    config = configparser.ConfigParser()
    config.read(config_path)

    profiles = [section for section in config.sections() if section.startswith("profile ")]
    if profiles:
        for profile in profiles:
            profile_name = profile.split(" ")[1].strip('"')
            username = config.get(profile, "username", fallback="N/A")
            print(f"- {profile_name}: Username: {username}")
    else:
        print("No Git profiles found.")


def git_cli(action):
    """Git-specific CLI operations."""
    if action == "create_profile":
        profile_name = input("Enter profile name: ").strip()
        username = input("Enter Git username: ").strip()
        token = input("Enter Git token: ").strip()
        create_profile(profile_name, username, token)

    elif action == "update_profile":
        profile_name = input("Enter profile name to update: ").strip()
        new_name = input("New profile name (leave blank to keep current): ").strip()
        username = input("New username (leave blank to keep current): ").strip()
        token = input("New token (leave blank to keep current): ").strip()
        update_profile(profile_name, new_name=new_name or None, username=username or None, token=token or None)

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete: ").strip()
        delete_profile(profile_name)

    elif action == "list_profiles":
        list_profiles()

    else:
        print(f"Unknown Git action: {action}")
