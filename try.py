#How do i make the code such that, when i remove elements from list "l", list "p" isn't affected although i have written code: p = l above the code that removes elements from list "p"in python?


p = [1,2,3,4,5,6,7]
k = int(input("Enter number of times to rotate the array: "))
l = []
for i in range(0,k%len(p)):

    l.append(p[len(p)-1])
    for j in range(1,len(p)):
        l.append(p[j-1])
    p = list(l)
    l=[]
    

print(p)