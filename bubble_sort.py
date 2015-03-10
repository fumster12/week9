import random

def sort(items):
  # 1. TO DO: Implement a "bubble sort" routine here
  n = len(items)
  swapped = True
  while swapped:
      swapped = False
      for i, item in enumerate(items):
          if i != n-1 and items[i] > items[i + 1]:
             items[i+1], items[i] = items[i], items[i+1] 
             swapped = True
      
  return items

numbers = list(range(10))
random.shuffle(numbers)

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
#    Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(n^2) ")
