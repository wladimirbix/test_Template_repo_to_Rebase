import os

# Define the path to the Databricks CLI configuration file
PROFILE_FILE = os.path.expanduser("~/.databrickscfg")


# Function to load profiles (if any exist)
def load_profiles():
    profiles = {}
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            current_profile = None
            for line in file:
                line = line.strip()
                if line.startswith("["):
                    # Start a new profile section
                    current_profile = line.strip("[]")
                    profiles[current_profile] = {}
                elif "=" in line and current_profile:
                    key, value = line.split("=", 1)
                    profiles[current_profile][key.strip()] = value.strip()
    return profiles


# Function to save a profile to the Databricks CLI configuration file
def save_profile(profile_name, host_name, token):
    profiles = load_profiles()

    # If the profile already exists, overwrite it
    profiles[profile_name] = {"host": host_name, "token": token}

    with open(PROFILE_FILE, "w") as file:
        for profile, details in profiles.items():
            file.write(f"[{profile}]\n")
            for key, value in details.items():
                file.write(f"{key} = {value}\n")
    print(f"Profile '{profile_name}' saved successfully in {PROFILE_FILE}")


# Create a new profile for Databricks CLI
def create_profile():
    print("\n--- Create New Profile for Databricks CLI ---")
    profile_name = input("Enter profile name: ")
    host_name = input("Enter host name (Databricks workspace URL): ")
    token = input("Enter your Databricks token: ")

    save_profile(profile_name, host_name, token)


# Update an existing profile
def update_profile():
    print("\n--- Update Profile for Databricks CLI ---")
    profiles = load_profiles()
    if not profiles:
        print("No profiles found.")
        return

    profile_name = input("Enter profile name to update: ")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' does not exist.")
        return

    host_name = input(f"Enter new host name (current: {profiles[profile_name].get('host', 'N/A')}): ")
    token = input("Enter new token (leave blank to keep current): ")

    # If the user leaves token blank, keep the existing token
    if not token:
        token = profiles[profile_name].get("token")

    save_profile(profile_name, host_name, token)


# Delete an existing profile
def delete_profile():
    print("\n--- Delete Profile ---")
    profiles = load_profiles()
    if not profiles:
        print("No profiles found.")
        return

    profile_name = input("Enter profile name to delete: ")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' does not exist.")
        return

    # Load the profiles and remove the selected profile
    profiles.pop(profile_name)

    with open(PROFILE_FILE, "w") as file:
        for profile, details in profiles.items():
            file.write(f"[{profile}]\n")
            for key, value in details.items():
                file.write(f"{key} = {value}\n")

    print(f"Profile '{profile_name}' deleted successfully.")


# List all profiles
def list_profiles():
    print("\n--- List Profiles ---")
    profiles = load_profiles()
    if not profiles:
        print("No profiles found.")
        return

    for profile_name, details in profiles.items():
        print(f"\nProfile: {profile_name}")
        print(f"Host: {details.get('host', 'N/A')}")
        print(f"Token: {details.get('token', 'N/A')}")


# Main function to handle the console
def main():
    while True:
        print("\n--- Unicon CLI ---")
        print("1. Create Profile (Databricks CLI)")
        print("2. Update Profile (Databricks CLI)")
        print("3. Delete Profile (Databricks CLI)")
        print("4. List Profiles (Databricks CLI)")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            create_profile()
        elif choice == "2":
            update_profile()
        elif choice == "3":
            delete_profile()
        elif choice == "4":
            list_profiles()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
