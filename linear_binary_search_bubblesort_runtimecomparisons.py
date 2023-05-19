def linear_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0
   
    for i in range(len(numbers)):
        comparisons = comparisons + 1
        if (numbers[i] == key):
           return i, comparisons
    return -1, comparisons # not found
 
def binary_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0

    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts at whole range
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # Calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        comparisons = comparisons + 1
        if (numbers[mid] < key):
            low = mid + 1
      
        elif (numbers[mid] > key):
            high = mid - 1
      
        else:
            return mid, comparisons
  
    return -1, comparisons # not found


# Main program to test both search functions 
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer key to search for: '))
print()
 
# Test linear search
key_index, comparisons = linear_search(numbers, key)      
if (key_index == -1):
    print('Linear search: %d was not found with %d comparisons.' % (key, comparisons))
else:
    print('Linear search: Found %d at index %d with %d comparisons.' % (key, key_index, comparisons))
 
# Test binary search
key_index, comparisons = binary_search(numbers, key)
if (key_index == -1):
    print('Binary search: %d was not found with %d comparisons.' % (key, comparisons))
else:
    print('Binary search: Found %d at index %d with %d comparisons.' % (key, key_index, comparisons))


def bubbleSort(myNumbers):
   myNumbersSize = len(myNumbers)
   for i in range(0,myNumbersSize -1):
      print("\nPass: %d - %s" % (i, str(myNumbers)))
      for j in range(0,myNumbersSize - i - 1):
         if (myNumbers[j] > myNumbers[j+1]):
            print("Swap: %d-%d" % (myNumbers[j], myNumbers[j+1]))
            temp = myNumbers[j]
            myNumbers[j] = myNumbers[j+1]
            myNumbers[j+1] = temp
            print(myNumbers)

myArray = [3, 5, 8, 9, 6, 2]
print('Original Array:',myArray)
bubbleSort(myArray)
print('Sorted Array:',myArray)

# Runtime Comparison
import time

def addUpTo1(n): # O(n)
  total = 0
  for i in range(1,n+1): # i = 1, 2, ... n
    total += i
  return total

def addUpTo2(n): # O(1)
  return (n * (n + 1)) / 2

N = 3 # if N = 3 then 1 + 2 + 3 = 6 also (3*(3+1))/2 = 6
print("N = ", N)
timeStart1 = time.time()
print("Returned value: addUpTo1(N): {}".format(addUpTo1(N)))
timeEnd1 = time.time()
print(f"Runtime of the program addUpTo1(N) is {(timeEnd1 - timeStart1):.8f} (sec)")
timeStart2 = time.time()
print("Returned value: addUpTo2(N): {}".format(addUpTo2(N)))
timeEnd2 = time.time()
print(f"Runtime of the program addUpTo2(N) is {(timeEnd2 - timeStart2):.8f} (sec)")
print()

N = 1000000 # 1M
print("N = ", N)
timeStart1 = time.time()
print("Returned value: addUpTo1(N): {}".format(addUpTo1(N)))
timeEnd1 = time.time()
print(f"Runtime of the program addUpTo1(N) is {(timeEnd1 - timeStart1):.8f} (sec)")
timeStart2 = time.time()
print("Returned value: addUpTo2(N): {}".format(addUpTo2(N)))
timeEnd2 = time.time()
print(f"Runtime of the program addUpTo2(N) is {(timeEnd2 - timeStart2):.8f} (sec)")
print()

N = 1000000000 #1B
print("N = ", N)
timeStart1 = time.time()
print("Returned value: addUpTo1(N): {}".format(addUpTo1(N)))
timeEnd1 = time.time()
print(f"Runtime of the program addUpTo1(N) is {(timeEnd1 - timeStart1):.8f} (sec)")
timeStart2 = time.time()
print("Returned value: addUpTo2(N): {}".format(addUpTo2(N)))
timeEnd2 = time.time()
print(f"Runtime of the program addUpTo2(N) is {(timeEnd2 - timeStart2):.8f} (sec)")
print()
