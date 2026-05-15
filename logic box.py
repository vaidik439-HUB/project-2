print("\nWelcome to the pattern Generator and Number Analyzer!\n")

print("\nSelect an option:")
print("1. Generate a pattern")
print("2. Analyzer a Range of numbers")
print("3. Exit")
while True:
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        rows=int(input("Enter the number of rows for pattern:"))
        print("\nPattern:")
        for i in range(1,rows+1):
         print("*"*i)
    elif choice==2:
        start=int(input("Enter the start of the range:"))    
        end=int(input("Enter the end of the range:"))
        total_sum=0

        for num in range(start,end+1):
             label="Even" if num % 2 ==0 else "Odd"
             print(f"Number {num} is {label} ")
             total_sum+=num

        print(f"Sum of all numbers from {start} to {end} is:{total_sum}")

    elif choice==3:
        break

    else:
        print("Invalid choice. Please try again.")

print("\n Exiting the program.Goodbye!")

