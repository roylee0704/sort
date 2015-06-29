"""


  if     n = 4, (total length)
     n - 1 = 3, (last index)
     n - 2 = 2, (look ahead stop index)


   5,  4,  2,  3
  [0] [1] [2] [3]
  
  [0] loop to [2]:                        | for (0 < (n-1))  
    
    checkpoint at 5, [0] 
    if 5 > 4:  [1]: look-ahead  
      swap 4 and 5

    checkpoint at 5, [1]
    if 5 > 2:  [2]: look-ahead
      swap 2 and 5

    checkpoint at 5, [2]        !(the end): remember final-swap index
    if 5 > 3:  [3]: look-ahead
      swap 3 and 5


   4,  2,  3,  5
  [0] [1] [2] [3]

  [0] loop to [1]:                        | for (0 < (n-2))

    checkpoint at 4, [0]
    if 4 > 2: [1]: look-ahead
      swap 2 and 4

    checkpoint at 4, [1]        !(the end): remember final-swap index
    if 4 > 3: [2]: look-ahead
      swap 3 and 4 


   2,  3,  4,  5
  [0] [1] [2] [3]

  [0] loop to [0]:                        | for (0 < (n-3))

    checkpoint at 2, [0]        !(the end): remember final-swap index
    if 2 > 3: [1]: look-ahead
      swap 2 and 3




"""
def swap(a, b):
  return b, a



def selection_sort(list):
  n = len(list)
  maxIndex = n - 1
  last_check = maxIndex #inclusive

  for i in range(0, n - 1):
    for j in range(0, last_check):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
        maxIndex = j

    last_check = maxIndex

  print list    


def main():
  elemList = [3, 1, 2, 5, 4]
  selection_sort(elemList)


if __name__ == '__main__':
  main()