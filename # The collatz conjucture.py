# To Code Collatz Conjecture
# By: J.T. Conklin
# Date: 4/18/18

# Recursion of Collatz Conjecture
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

# Main Program
try:
    li=[]
    number = int(input("Enter a number: "))
    while number != 1:
        number = collatz(number)
        li.append(number)

    print(li)
    import matplotlib.pyplot as plt
    plt.plot(li)
    plt.show()
except ValueError:
    print("Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except:
    print("An error occurred.")
    raise
    exit()
print("\nThe program completed successfully.")
exit()
# End of Program
# By: J.T. Conklin
# Date: 4/18/18
# End of Collatz Conjecture
