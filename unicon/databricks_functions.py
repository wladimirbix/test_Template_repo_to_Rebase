from profile_functions import create_profile, update_profile, delete_profile, list_profiles


def databricks_cli(action):
    """Databricks-specific CLI operations."""
    if action == "create_profile":
        profile_name = input("Enter profile name: ").strip()
        host = input("Enter Databricks host: ").strip()
        token = input("Enter Databricks token: ").strip()
        create_profile("databricks", profile_name, host=host, token=token)
        print(f"Profile '{profile_name}' created successfully.")

    elif action == "update_profile":
        profile_name = input("Enter profile name to update: ").strip()
        new_name = input("New profile name (leave blank to keep current): ").strip()
        host = input("New host (leave blank to keep current): ").strip()
        token = input("New token (leave blank to keep current): ").strip()
        update_profile("databricks", profile_name, new_name=new_name, host=host, token=token)
        print(f"Profile '{profile_name}' updated successfully.")

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete: ").strip()
        delete_profile("databricks", profile_name)
        print(f"Profile '{profile_name}' deleted successfully.")

    elif action == "list_profiles":
        profiles = list_profiles("databricks")
        if profiles:
            for name, details in profiles.items():
                print(f"- {name}: Host: {details['host']}")
        else:
            print("No Databricks profiles found.")
    else:
        print(f"Unknown Databricks action: {action}")
        # Re-prompt or handle unknown action (this can be moved to main CLI logic if necessary)
