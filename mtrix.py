list1 = [1,2,3]
list2 = [1,2,1]
list3 = [1,1,1]
matrix =[list1, list2, list3]
print(f"{list1}\n{list2}\n{list3}")
i, j = map(int, input("Enter the index where you stored the money (i j): ").split())
matrix[i-1][j-1] = int(input("Enter the new value: "))
print(f"{list1}\n{list2}\n{list3}")