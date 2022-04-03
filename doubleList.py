List1=[10, 20, 23, 11, 17]
List2=[13, 43, 24, 36, 12]

List3 = []

for num in List1:
    if (num%2)!=0:
        List3.append(num)

for num in List2:
    if (num%2)==0:
        List3.append(num)
print(List3)

def selection_sort(list):
    for i in range(len(list)):
        min_i = i
        for j in range( i+1, len(list)):
            if list[min_i] > list[j]:
                min_i = j
            list[i], list[min_i] = list[min_i], list[i]

selection_sort(List3)
print("Sorted: ",List3)