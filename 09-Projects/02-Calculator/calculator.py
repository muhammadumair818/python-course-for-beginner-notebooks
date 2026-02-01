"""
CALCULATOR PROGRAM

A simple calculator that performs basic arithmetic operations.

Features:
- Addition, Subtraction, Multiplication, Division
- Modulo and Power operations
- Continuous calculations
- Clear history option
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulo(a, b):
    if b == 0:
        return None
    return a % b

def power(a, b):
    return a ** b

def display_menu():
    """Display the menu options"""
    print("\n" + "="*50)
    print("SIMPLE CALCULATOR")
    print("="*50)
    print("Select operation:")
    print("  1. Add (+)")
    print("  2. Subtract (-)")
    print("  3. Multiply (*)")
    print("  4. Divide (/)")
    print("  5. Modulo (%)")
    print("  6. Power (**)")
    print("  7. Clear history")
    print("  8. Exit")
    print("-"*50)

def calculator():
    """Main calculator loop"""
    
    history = []
    
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ").strip()
        
        if choice == '8':
            print("\nThank you for using the calculator! Goodbye!")
            break
        
        elif choice == '7':
            history.clear()
            print("History cleared!")
            continue
        
        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    operation = '+'
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = '-'
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = '*'
                elif choice == '4':
                    operation = '/'
                    result = divide(num1, num2)
                    if result is None:
                        print("Error: Cannot divide by zero!")
                        continue
                elif choice == '5':
                    operation = '%'
                    result = modulo(num1, num2)
                    if result is None:
                        print("Error: Cannot modulo by zero!")
                        continue
                elif choice == '6':
                    result = power(num1, num2)
                    operation = '**'
                
                # Display result
                print(f"\n{num1} {operation} {num2} = {result}")
                
                # Add to history
                history.append(f"{num1} {operation} {num2} = {result}")
                
                # Show history
                if history:
                    print("\nCalculation History:")
                    for calc in history[-5:]:  # Show last 5
                        print(f"  {calc}")
            
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        
        else:
            print("Invalid choice! Please select 1-8.")

if __name__ == "__main__":
    calculator()
