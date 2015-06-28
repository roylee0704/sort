#Introduction (0.1)

Sorting is arrangment of the elements in a list or collection in increasing or decreasing
order of some property. 

    I.e: Sort by order of `value`, sort by order of factor..


##Classification:

We have so many algorithms for sorting that have been design over a period of time:
- Bubble sort
- Selection sort
- Insertion sort
- Merge sort
- Quick sort
- Heap sort
- Counting sort
- Radix sort

We often classify sorting algorithms based on some parameters: 
- Time complexity.
- Space complexity/ Memory usage.
- Stability.
- Internal sort vs External sort.
- Recursive or Non-recursive.
	
### Time Complexity: 

The measure of rate of growth of time taken by an algorithm with respect to input size.	Some algorithm will be relatively faster than others.
	
### Space Complexity/ Memory usage:

1. In-place memory. Some algorihtm are in-place, they use constant amount of memory to rearrange the elements in the list.  

2. External memory. Like merge sort, it uses extra memory to temporarily store data and the **memory usage grows with input size**.

### Stability

A stable sorting algorithm in the case of equality of key, or the property upon which we are sorting, preserves the relative order of elements. So if the key is equal, and the element was coming before in the original list, it wil also come before in the sorted list.

###Internal sort vs External sort

When the records that need to be sorted is in the main memory/RAM, then such sort is *internal sort*. 

If the records are on auxiliary storage like disk and tapes, quite often because its not possible to get all of them in the main memory in one go, then we call such a sort, *external sort*.

###Recursive or Non-recursive

`Quick sort` and `Merge sort` are recursive, while others like `Insertion sort` and `Selection sort` are non-recursive.



