import subprocess

def upgrade_all_packages():
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
    print("All packages upgraded successfully.")

def package_upgrade(index):
    print(f"{index}")
    

def get_available_updates():
    print("Checking for updates...")
    res = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)
    result = res.stdout.split("/")[1:]

    if len(result) > 1:
        index = 1
        for package in result:
            print(f'{index}:{package}')
            index = index + 1
        all_updates = input("Do you want to upgrade all the packages? (y/n): ").strip().lower()
        if(all_updates == "n"):
            package_index = input("Enter the index the the package that you want to upgrade: ")
            package_upgrade(package_index)
        if(all_updates == "y"):
            upgrade_all_packages()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            package_upgrade()  
    else:
        print("No packages are available for update")

get_available_updates()
