from profile_functions import create_profile, update_profile, delete_profile, list_profiles


def git_cli(action):
    """Git-specific CLI operations."""
    if action == "create_profile":
        profile_name = input("Enter profile name: ").strip()
        username = input("Enter Git username: ").strip()
        token = input("Enter Git token: ").strip()
        create_profile("git", profile_name, username=username, token=token)
        print(f"Profile '{profile_name}' created successfully.")

    elif action == "update_profile":
        profile_name = input("Enter profile name to update: ").strip()
        new_name = input("New profile name (leave blank to keep current): ").strip()
        username = input("New username (leave blank to keep current): ").strip()
        token = input("New token (leave blank to keep current): ").strip()
        update_profile("git", profile_name, new_name=new_name, username=username, token=token)
        print(f"Profile '{profile_name}' updated successfully.")

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete: ").strip()
        delete_profile("git", profile_name)
        print(f"Profile '{profile_name}' deleted successfully.")

    elif action == "list_profiles":
        # Retrieve Git profiles using the list_profiles function
        profiles = list_profiles("git")
        if profiles:
            for name, details in profiles.items():
                print(f"- {name}: Username: {details['username']}")
        else:
            print("No Git profiles found.")
    else:
        print(f"Unknown Git action: {action}")
        # Re-prompt or handle unknown action (this can be moved to main CLI logic if necessary)
