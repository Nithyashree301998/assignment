#########Question 1#############
def binarySearch(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

array = [3, 4, 5, 6, 7, 8, 9]
print(array)
x = int(input("Enetr the element to be searched:"))
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

###########Question 2##########
def merge(l1,l2):
    sorted_array=[]
    i=0
    j=0
    len_first=len(l1)
    len_second=len(l2)
    while i<len_first and j<len_second:
        if l1[i]<l2[j]:
            sorted_array.append(l1[i])
            i=i+1
        else:
            sorted_array.append(l2[j])
            j=j+1
    sorted_array.extend(l1[i:])
    sorted_array.extend(l2[j:])        
    return sorted_array

def merge_sort(l):
    if len(l)<=1:
        return l
    else:
        first_half=l[:len(l)//2]
        second_half=l[len(l)//2:]
        first_half=merge_sort(first_half)
        second_half=merge_sort(second_half)
        return merge(first_half,second_half)

array = [34,23,2,3,1,11,15]
print(array)
result=merge_sort(array)                    
print("Sorted array:")
print(result)


#######Question 3#######
def partition(array, low, high):

  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:

      i = i + 1

      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)


##########Question 4##########
def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i- 1
           
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


#########Question 5##########
lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']
lst.sort()
print(lst)
