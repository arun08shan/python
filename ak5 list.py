# Initialize the global variables
list = []
n = 0

# Function to create a list and input elements
def Create():
    global n
    print("Enter the number of elements to be added in the list:", end=" ")
    n = int(input())
    print("Enter the list elements:")
    for i in range(n):
        list.append(int(input()))
    display()

# Function to insert an element at a specific position
def Insert():
    global n
    print("Enter the data to be inserted:", end=" ")
    data = int(input())
    print("Enter the position at which the element should be inserted:", end=" ")
    pos = int(input())

    # Insert the element by shifting elements to the right
    list.append(0)  # Increase the list size by 1
    for i in range(n, pos - 1, -1):
        list[i] = list[i - 1]
    list[pos - 1] = data  # Place the new element at the specified position
    n += 1
    display()

# Function to delete an element at a specific position
def Delete():
    global n
    print("Enter the position of the data to be deleted:", end=" ")
    pos = int(input())
    
    if pos < 1 or pos > n:
        print("Invalid position!")
        return

    print("The data deleted is:", list[pos - 1])
    for i in range(pos - 1, n - 1):
        list[i] = list[i + 1]
    list.pop()  # Remove the last element
    n -= 1
    display()

# Function to display the current list
def display():
    global n
    print("\n** List elements **")
    for i in range(n):
        print(list[i], end=" ")
    print()

# Function to search for an element in the list
def Search():
    global n
    print("Enter the data to be searched:", end=" ")
    data = int(input())
    found = False
    for i in range(n):
        if list[i] == data:
            print(f"Data found at position {i + 1}")
            found = True
            break
    if not found:
        print("Data not found!")

# Main function to drive the menu and program execution
def main():
    while True:
        print("\nImplementation of list operations:")
        print("\t1. Create")
        print("\t2. Insert")
        print("\t3. Delete")
        print("\t4. Display")
        print("\t5. Search")
        print("\t6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            Create()
        elif choice == 2:
            Insert()
        elif choice == 3:
            Delete()
        elif choice == 4:
            display()
        elif choice == 5:
            Search()
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()