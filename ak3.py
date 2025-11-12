class Stack:
    def __init__(self):
        self.top = -1  # This will represent the index of the top element
        self.stk = []  # This will hold the stack elements
        self.max = 50  # Maximum size of the stack

    def push(self):
        if self.top == self.max - 1:
            print("Stack Overflow: Unable to push, the stack is full.")
        else:
            item = int(input("Enter an item to be pushed: "))
            self.top += 1
            self.stk.append(item)
            print("Item pushed successfully.")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow: Unable to pop, the stack is empty.")
        else:
            item = self.stk.pop()  # Pop the last item from the stack
            self.top -= 1
            print(f"{item} is popped successfully.")

    def display(self):
        if self.top == -1:
            print("Stack Underflow: No items to display.")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(f"{self.stk[i]}")

# Main function to interact with the stack
if __name__ == "__main__":
    st = Stack()  # Create a new Stack object
    while True:
        print("\n\n***** Menu for Stack Operations *****\n")
        print("1. PUSH")
        print("2. POP")
        print("3. DISPLAY")
        print("4. EXIT")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            st.push()
        elif choice == 2:
            st.pop()
        elif choice == 3:
            st.display()
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")