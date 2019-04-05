import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

###################### Provided Example Algorithm #####################
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



####################### My First Pass Algorithm ########################
# directory = {}
# duplicates = []

# for name_1 in names_1:
#     if name_1 not in directory:
#         directory[name_1] = 1

#     # directory[name_1] += 1

# for name_2 in names_2:
#     # if name_2 not in directory:
#         # directory[name_2] = 0

#     if name_2 in directory:
#         directory[name_2] += 1

# for name, count in directory.items():
#     if count > 1:
#         duplicates.append(name)



########################### STRETCH Attempt 1 ########################################
# duplicates = []

# def merge(arrA, arrB):
#     # create new array of size [len(arrA) + len(arrB] for merged elements
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements

#     arrAIndex = 0
#     arrBIndex = 0

#     for i in range(0, elements):
#         # if all elements in arrA have been merged, put next element in arrB into merged array
#         if arrAIndex > len(arrA)-1 and arrBIndex <= len(arrB)-1:
#             merged_arr[i] = arrB[arrBIndex]
#             arrBIndex += 1

#         # elif all elements in arrB have been merged, put next element in arrA into merged array
#         elif arrBIndex > len(arrB)-1 and arrAIndex <= len(arrA)-1:
#             merged_arr[i] = arrA[arrAIndex]
#             arrAIndex += 1

#         # elif next element in arrA smaller or equal, add to merged array
#         elif arrA[arrAIndex] <= arrB[arrBIndex]:
#             merged_arr[i] = arrA[arrAIndex]
#             arrAIndex += 1

#         # else next element in arrB smaller, add to merged array
#         elif arrB[arrBIndex] < arrA[arrAIndex]:
#             merged_arr[i] = arrB[arrBIndex]
#             arrBIndex += 1
    
#     return merged_arr

# def merge_sort(arr):
#     if len(arr) > 1:
#         left = merge_sort(arr[0:int(len(arr)/2)])
#         right = merge_sort(arr[int(len(arr)/2):])

#         arr = merge(left, right)

#     return arr


# names_1 = merge_sort(names_1)
# # print(names_1)


# def binary_search(arr, target):
#     if len(arr) == 0:
#         return
        
#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         middle = int((low + high) / 2)

#         if target < arr[middle]:
#             high = middle - 1

#         elif target > arr[middle]:
#             low = middle + 1

#         else:
#             return arr[middle]

#     return


# for name_2 in names_2:
#     result = binary_search(names_1, name_2)
#     if result is not None:
#         duplicates.append(result)



########################### STRETCH Attempt 2 ########################################
# duplicates = []
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)




########################### STRETCH Attempt 3 ########################################
# class Heap:
#   def __init__(self, storage=[]):
#     self.storage = storage
#     # self.storage = [100,36,28,30,10,15,19,27,3,2,5]

#   def insert(self, value):
#     # Insert the value to the end of the storage array.
#     self.storage.append(value)

#     # Save the index the new value is stored at.
#     cur_index = len(self.storage) - 1

#     # Find the index of the parent node for the new value using the provided formula.
#     parent_index = int((cur_index - 1) / 2)

#     # Stops looping if we reach the beginning of the heap's storage array or no swap occurs.
#     swap = True
#     while cur_index > 0 and swap == True:
#       swap = False

#       # Swap the parent and child values if child > parent.
#       if self.storage[cur_index] > self.storage[parent_index]:
#         # Store the parent and child values in variables so we don't lose them. Don't need to store both, but doing for clarity right now.
#         parent = self.storage[parent_index]
#         child = self.storage[cur_index]

#         # Move the parent value to the child's index.
#         self.storage[cur_index] = parent

#         # Move the child value to the parent's index.
#         self.storage[parent_index] = child

#         # Reset the cur_index to the parent_index bc that's now where our new value is.
#         cur_index = parent_index

#         # Find the new index of the parent node for the new value using the provided formula.
#         parent_index = int((cur_index - 1) / 2)

#         # Set wap to True so that it can loop again.
#         swap = True


#   def delete(self):
#     removed_item = self.storage[0]

#     # Replace the first item in the heap's storage array with the last item.
#     self.storage[0] = self.storage[len(self.storage) - 1]
#     self.storage.pop()

#     # Initialize the parent_index to the first item in the list
#     parent_index = 0

#     # Stops looping if we reach the end of the heap's storage array or no swap occurs.
#     swap = True
#     while parent_index < len(self.storage) - 1 and swap == True:
#       swap = False

#       # Define the indexes of the parent, left child, and right child using provided formulas.
#       left_child_index = (2 * parent_index) + 1
#       right_child_index = (2 * parent_index) + 2

#       # Define the values at those indexes.
#       parent = self.storage[parent_index]
#       if left_child_index < len(self.storage):
#         left_child = self.storage[left_child_index]
#       else:
#         left_child = None
#       if right_child_index < len(self.storage):
#         right_child = self.storage[right_child_index]
#       else:
#         right_child = None

#       # Find which child is the largest.
#       if left_child is not None and right_child is not None:
#         if left_child > right_child:
#           largest_child_index = left_child_index
#           largest_child = left_child
#         else:
#           largest_child_index = right_child_index
#           largest_child = right_child
#       elif left_child is None:
#         largest_child_index = right_child_index
#         largest_child = right_child
#       elif right_child is None:
#         largest_child_index = left_child_index
#         largest_child = left_child
#       else:
#         largest_child = None

#       # Swap the parent and largest child if the largest child is larger.
#       if largest_child is not None:
#         if largest_child > parent:
#           # Swapping the values
#           self.storage[parent_index] = largest_child
#           self.storage[largest_child_index] = parent

#           # Reseting the parent_index to the current position of the value so we can do this process again.
#           parent_index = largest_child_index

#           # Set wap to True so that it can loop again.
#           swap = True

#     return removed_item

#   def get_max(self):
#     return self.storage[0]

#   def get_size(self):
#     return len(self.storage)

# names_1 = Heap(names_1)

# # print(names_1.storage)
# # print(int((len(names_1.storage)- 1)/2))
# # print(names_1.storage[len(names_1.storage) - 1 - 0])
# # names_1.storage[0] = names_1.storage[len(names_1.storage) - 1 - 0]
# # print(names_1.storage[0])
# # print(names_1.storage[len(names_1.storage) - 1 - 0])


# for i in range(len(names_1.storage) - 1):
#     names_1.storage[0] = names_1.storage[len(names_1.storage) - 1 - i]


# print(names_1.storage)
    

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

