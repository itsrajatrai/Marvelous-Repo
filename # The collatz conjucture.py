
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

# Main Program
li=[]
number = int(input("Enter a number: "))
while number != 1:
  number = collatz(number)
  li.append(number)
print(li)
import matplotlib.pyplot as plt
import numpy
pq=numpy.log10(li)
plt.plot(pq)
plt.show()
   
   


