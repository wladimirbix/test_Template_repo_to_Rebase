from profile_functions import create_profile, update_profile, delete_profile, list_profiles


def azure_cli(action):
    """Azure-specific CLI operations."""
    if action == "create_profile":
        profile_name = input("Enter profile name: ").strip()
        subscription_id = input("Enter Azure subscription ID: ").strip()
        tenant_id = input("Enter Azure tenant ID: ").strip()
        create_profile("azure", profile_name, subscription_id=subscription_id, tenant_id=tenant_id)
        print(f"Profile '{profile_name}' created successfully.")

    elif action == "update_profile":
        profile_name = input("Enter profile name to update: ").strip()
        new_name = input("New profile name (leave blank to keep current): ").strip()
        subscription_id = input("New subscription ID (leave blank to keep current): ").strip()
        tenant_id = input("New tenant ID (leave blank to keep current): ").strip()
        update_profile("azure", profile_name, new_name=new_name, subscription_id=subscription_id, tenant_id=tenant_id)
        print(f"Profile '{profile_name}' updated successfully.")

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete: ").strip()
        delete_profile("azure", profile_name)
        print(f"Profile '{profile_name}' deleted successfully.")

    elif action == "list_profiles":
        profiles = list_profiles("azure")
        if profiles:
            for name, details in profiles.items():
                print(f"- {name}: Subscription ID: {details['subscription_id']}")
        else:
            print("No Azure profiles found.")
    else:
        print(f"Unknown Azure action: {action}")
        # Re-prompt or handle unknown action (this can be moved to main CLI logic if necessary)
