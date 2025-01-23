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
                default_status = " (default)" if details.get("default", False) else ""
                print(f"- {name}: Host: {details['host']}{default_status}")
        else:
            print("No Databricks profiles found.")

    elif action == "set_default_profile":
        profiles = list_profiles("databricks")
        if not profiles:
            print("No profiles found. Please create a profile first.")
            return

        print("Available profiles:")
        for name, details in profiles.items():
            default_status = " (default)" if details.get("default", False) else ""
            print(f"- {name}{default_status}")

        profile_name = input("Enter the profile name to set as default: ").strip()

        if profile_name not in profiles:
            print(f"Profile '{profile_name}' does not exist.")
            return

        # Set the selected profile as default and unset other defaults
        for name, details in profiles.items():
            if name == profile_name:
                details["default"] = True
            else:
                details["default"] = False

        # Save the updated profiles back
        update_profile("databricks", profile_name, default=True)
        print(f"Profile '{profile_name}' is now set as the default.")

        # Run the build_all_configs function
        from config_builder import build_all_configs  # Importing here to avoid unnecessary dependencies

        build_all_configs()

    else:
        print(f"Unknown Databricks action: {action}")
