from queue import Queue

# Custom Queue class inheriting from the Queue class
class CustomQueue(Queue):
    def __init__(self, max_size=5):
        super().__init__(maxsize=max_size)

    def insert_q(self):
        """Insert an item into the queue."""
        if self.full():
            print("Queue Overflow: Cannot insert, the queue is full.")
        else:
            item = input("Enter an item to be inserted: ")
            self.put(item)  # Correctly use put() to insert an item
            print(f"Item '{item}' inserted successfully into the queue.")

    def delete_q(self):
        """Delete an item from the queue."""
        if self.empty():
            print("Queue Underflow: The queue is empty, nothing to delete.")
        else:
            item = self.get()  # Correctly use get() to remove an item
            print(f"Item '{item}' deleted successfully from the queue.")

    def display_q(self):
        """Display all items in the queue."""
        if self.empty():
            print("Queue is empty.")
        else:
            print("Items in the queue are:")
            for item in list(self.queue):  # self.queue is a list that holds the queue items
                print(f"|{item}|", end=" <--> ")
            print()  # Print a newline after displaying all items

# Main function to interact with the custom queue
def main():
    q = CustomQueue()  # Create a CustomQueue object
    
    while True:
        print("\n\n*** Menu for Queue Operations ***\n")
        print("1. INSERT")
        print("2. DELETE")
        print("3. DISPLAY")
        print("4. EXIT")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            q.insert_q()
        elif choice == 2:
            q.delete_q()
        elif choice == 3:
            q.display_q()
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()