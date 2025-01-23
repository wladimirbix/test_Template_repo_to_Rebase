import sys
from profile_functions import create_profile, update_profile, delete_profile, list_profiles, set_default_profile
from databricks_functions import databricks_cli
from azure_cli_functions import azure_cli
from git_functions import git_cli
from config_builder import build_all_configs  # Import the function


def prompt_for_action():
    """Prompts the user to select a platform and action."""
    print("Welcome to Unicon CLI!")

    while True:  # Loop to allow restarting the process
        # Platform selection with exit option
        while True:
            platform = input("Choose a platform (databricks, azure, git) or type 'exit' to quit: ").strip().lower()

            if platform == "exit":
                print("Exiting Unicon CLI...")
                sys.exit(0)  # Exit the program
            elif platform not in ["databricks", "azure", "git"]:
                print("Invalid platform. Please choose from: databricks, azure, or git, or type 'exit' to quit.")
            else:
                break  # Proceed to action selection if a valid platform is chosen

        # Action selection
        while True:
            if platform == "databricks":
                action = (
                    input(
                        "Choose action (create_profile, update_profile, delete_profile, list_profiles, set_default_profile) or type 'back' to go back: "
                    )
                    .strip()
                    .lower()
                )
                if action == "back":
                    print("\nReturning to platform selection...\n")
                    break  # This will restart the loop to choose platform
                elif action not in [
                    "create_profile",
                    "update_profile",
                    "delete_profile",
                    "list_profiles",
                    "set_default_profile",
                ]:
                    print(
                        "Invalid action. Please choose from: create_profile, update_profile, delete_profile, list_profiles, set_default_profile."
                    )
                else:
                    # Handle actions
                    databricks_cli(action)
                    if action == "list_profiles":
                        print("\nWhat would you like to do next?")
                        continue
                    break
            elif platform == "azure":
                action = (
                    input(
                        "Choose action (create_profile, update_profile, delete_profile, list_profiles) or type 'back' to go back: "
                    )
                    .strip()
                    .lower()
                )
                if action == "back":
                    print("\nReturning to platform selection...\n")
                    break
                elif action not in [
                    "create_profile",
                    "update_profile",
                    "delete_profile",
                    "list_profiles",
                ]:
                    print(
                        "Invalid action. Please choose from: create_profile, update_profile, delete_profile, list_profiles."
                    )
                else:
                    # Handle actions
                    azure_cli(action)
                    if action == "list_profiles":
                        print("\nWhat would you like to do next?")
                        continue
                    break
            elif platform == "git":
                action = (
                    input(
                        "Choose action (create_profile, update_profile, delete_profile, list_profiles) or type 'back' to go back: "
                    )
                    .strip()
                    .lower()
                )
                if action == "back":
                    print("\nReturning to platform selection...\n")
                    break
                elif action not in [
                    "create_profile",
                    "update_profile",
                    "delete_profile",
                    "list_profiles",
                ]:
                    print(
                        "Invalid action. Please choose from: create_profile, update_profile, delete_profile, list_profiles."
                    )
                else:
                    # Handle actions
                    git_cli(action)
                    if action == "list_profiles":
                        print("\nWhat would you like to do next?")
                        continue
                    break

            # If any of the profile creation, update or deletion happens, return to platform selection
            if action in ["create_profile", "update_profile", "delete_profile"]:
                print("\nAction completed! Returning to platform selection...\n")
                break


def create_or_update_profile(profile_type, action):
    """Handles profile creation or update with a cancel option."""
    profiles = list_profiles(profile_type)

    if action == "create_profile":
        while True:
            profile_name = input("Enter profile name or type 'cancel' to go back: ").strip()
            if profile_name == "cancel":
                print("Profile creation cancelled. Returning to platform selection...\n")
                return  # Exit the function to avoid further processing

            if profile_name in profiles:
                print(f"Profile '{profile_name}' already exists. Please choose a different name.")
                continue  # Ask for a different name if the profile exists
            else:
                break  # Continue if the profile name is unique

        subscription_id = input("Enter subscription ID: ").strip()
        tenant_id = input("Enter tenant ID: ").strip()

        # Confirm before creating
        if input(f"Create profile '{profile_name}'? (yes/cancel): ").strip().lower() == "yes":
            create_profile(profile_type, profile_name, subscription_id=subscription_id, tenant_id=tenant_id)
            print(f"Profile '{profile_name}' created successfully.")
            build_all_configs()  # Call the function after deleting a profile
        else:
            print(f"Profile creation for '{profile_name}' cancelled.")

        # Return to platform selection after creation
        prompt_for_action()

    elif action == "update_profile":
        profile_name = input("Enter profile name to update or type 'cancel' to go back: ").strip()
        if profile_name == "cancel":
            print("Profile update cancelled. Returning to platform selection...\n")
            return  # Exit the function to avoid further processing
        if profile_name not in profiles:
            print(f"Profile '{profile_name}' does not exist.")
            return

        new_name = input("New profile name (leave blank to keep current): ").strip()

        # Check if the new name already exists
        if new_name and new_name in profiles:
            print(
                f"Profile '{new_name}' already exists. Please choose a different name or leave blank to keep current name."
            )
            return  # Don't allow overwriting of an existing profile

        subscription_id = input("New subscription ID (leave blank to keep current): ").strip()
        tenant_id = input("New tenant ID (leave blank to keep current): ").strip()

        # Confirm before updating
        if input(f"Update profile '{profile_name}'? (yes/cancel): ").strip().lower() == "yes":
            update_profile(
                profile_type, profile_name, new_name=new_name, subscription_id=subscription_id, tenant_id=tenant_id
            )
            print(f"Profile '{profile_name}' updated successfully.")
            build_all_configs()  # Call the function after deleting a profile
        else:
            print(f"Profile update for '{profile_name}' cancelled.")

        # Return to platform selection after update
        prompt_for_action()

    elif action == "select_default_profile":
        profile_name = input("Enter profile name to set as default or type 'cancel' to go back: ").strip()
        if profile_name == "cancel":
            print("Default profile selection cancelled. Returning to platform selection...\n")
            return  # Exit the function to avoid further processing
        if profile_name not in profiles:
            print(f"Profile '{profile_name}' does not exist.")
            return

        # Confirm before setting default
        if input(f"Set '{profile_name}' as the default profile? (yes/cancel): ").strip().lower() == "yes":
            set_default_profile(profile_type, profile_name)  # Assuming set_default_profile is implemented
            print(f"Profile '{profile_name}' is now set as the default profile.")
            build_all_configs()  # Call the function to rebuild the configurations
        else:
            print(f"Default profile selection for '{profile_name}' cancelled.")

        # Return to platform selection after setting the default
        prompt_for_action()

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete or type 'cancel' to go back: ").strip()
        if profile_name == "cancel":
            print("Profile deletion cancelled. Returning to platform selection...\n")
            return  # Exit the function to avoid further processing
        # Confirm before deleting
        if input(f"Delete profile '{profile_name}'? (yes/cancel): ").strip().lower() == "yes":
            delete_profile(profile_type, profile_name)
            print(f"Profile '{profile_name}' deleted successfully.")
            build_all_configs()  # Call the function after deleting a profile
        else:
            print(f"Profile deletion for '{profile_name}' cancelled.")
        # Return to platform selection after deletion
        prompt_for_action()

    elif action == "list_profiles":
        profiles = list_profiles(profile_type)
        if profiles:
            for name, details in profiles.items():
                print(f"- {name}: Subscription ID: {details['subscription_id']}")
        else:
            print(f"No profiles found for {profile_type}.")
        # Return to platform selection after listing profiles
        prompt_for_action()


def main():
    """Central CLI interface for Unicon."""
    if len(sys.argv) > 1:  # If arguments are provided, process them directly
        command = sys.argv[1]
        if command == "databricks":
            databricks_cli(sys.argv[2])  # Pass the action as a string, not a list
        elif command == "azure":
            azure_cli(sys.argv[2])  # Pass the action as a string, not a list
        elif command == "git":
            git_cli(sys.argv[2])  # Pass the action as a string, not a list
        else:
            print("Unknown command.")
            sys.exit(1)
    else:
        # Otherwise, prompt for input interactively
        prompt_for_action()


if __name__ == "__main__":
    main()
