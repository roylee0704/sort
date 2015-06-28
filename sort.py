"""
	Sorting is arranging the elements in a list or collection in increasing or decreasing
	order of some property. 

	I.e: Sort by order of `value`, sort by order of factor

"""

def numOfFactors(val):
  test = 1
  total = 0
  while test < val:
    if val % test == 0:
      total += 1
    test += 1
  return total;

def sortByOrderOfFactor(list):
	
  print sorted(list, key = numOfFactors)



def main():
  num_list = [2, 3, 9, 4, 6]

  sortByOrderOfFactor(num_list)




if __name__ == '__main__':
  main()