# Health Management System - By Sadiya 💻
from datetime import datetime

# Function to get current date and time
def get_time():
    return datetime.now()

# Function to log data
def log_data(client_name):
    print("\nWhat do you want to log?")
    choice = int(input("1. Exercise\n2. Food\nEnter choice: "))
    
    if choice == 1:
        data = input("Enter exercise details: ")
        filename = f"{client_name}-exercise.txt"
    elif choice == 2:
        data = input("Enter food details: ")
        filename = f"{client_name}-food.txt"
    else:
        print("Invalid choice.")
        return

    with open(filename, "a") as f:
        f.write(f"[{get_time()}] {data}\n")
    print("Data logged successfully!")

# Function to retrieve data
def retrieve_data(client_name):
    print("\nWhat do you want to retrieve?")
    choice = int(input("1. Exercise\n2. Food\nEnter choice: "))
    
    if choice == 1:
        filename = f"{client_name}-exercise.txt"
    elif choice == 2:
        filename = f"{client_name}-food.txt"
    else:
        print("Invalid choice.")
        return

    try:
        with open(filename, "r") as f:
            print(f"\n--- {client_name}'s Records ---")
            print(f.read())
    except FileNotFoundError:
        print("No records found yet.")

# Main program
def main():
    print("Welcome to Health Management System")

    while True:
        print("\nSelect Client:")
        print("1. Harry")
        print("2. Rohan")
        print("3. Hammad")
        client_choice = int(input("Enter choice (1-3): "))

        clients = {1: "harry", 2: "rohan", 3: "hammad"}

        if client_choice in clients:
            client_name = clients[client_choice]
            print("\nChoose Action:")
            print("1. Log Data")
            print("2. Retrieve Data")
            action = int(input("Enter choice: "))

            if action == 1:
                log_data(client_name)
            elif action == 2:
                retrieve_data(client_name)
            else:
                print("Invalid action.")
        else:
            print("Invalid client selection.")

        cont = input("\nDo you want to continue? (yes/no): ").lower()
        if cont != "yes":
            print("Thank you for using the Health Management System!")
            break

# Run the main function
if __name__ == "__main__":
    main()
