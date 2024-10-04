lst1 = eval(input('Enter the elements for list1: '))
lst2 = eval(input('Enter the elements for list 2: '))

maxlst1 = max(lst1)
maxlst2 = max(lst2)

if maxlst1 < maxlst2:
    print(f"Maximum: {maxlst2}")
    print(f'Index : {lst2.index(maxlst2)}')
    print("from list 2")
elif maxlst1 == maxlst2:
     print(f"Maximum: {maxlst2}")
     print("Same in both the lists")
else:
    print(f"Maximum: {maxlst1}")
    print(f'Index : {lst1.index(maxlst1)}')
    print("from list 1")
    
