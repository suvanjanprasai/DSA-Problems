# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. The time complexity of this code is O(k * n).

array = [1,2,3,4,5,6,7]
k = abs(int(input("Enter number of times to rotate the array: ")))
l = []
for i in range (0, k % len(array)):
    l.append( array[len( array )-1])
    for j in range ( 1, len(array)):
        l.append (array[j-1])
    array = list (l)
    l=[]
print(array)
