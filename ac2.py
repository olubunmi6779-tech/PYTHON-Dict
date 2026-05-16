lst = ['Apple','Banana', 'Mango', 'Orange',]  

print( "Lenght of list:", len(lst))
print( "First Element:", lst[0])
print( "Last Element:", lst[-1])

lst.append('Pineapple')
print("Update list :", lst)

lst.remove('Orange')
print("Update list :", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop(1)
print("Update list :", lst)

lst.reverse()
print("Update list :", lst)

print("Multiplication on List :", lst*2)

lst = lst[:4]
print("Sliced list :", lst)

lst.clear
print("Update list :", lst)
