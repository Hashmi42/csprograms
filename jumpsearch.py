import math


def jumpSearch(arr, x, n):
    # Finding block size to be jumped
    step = int(math.sqrt(n))

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while arr[int(prev)] < x:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1

    # If element is found
    if arr[int(prev)] == x:
        return prev

    return -1

#
def binarySearch(lyst,lo,hi, target):
    mid = lo + (hi - lo) // 2
    if hi>=1:
        if lyst[mid] == target:
            return mid
        elif lyst[mid] > target:
            return binarySearch(lyst, lo, mid - 1, target)
        elif lyst[mid] < target:
            return binarySearch(lyst,mid+1, hi,target)
    return -1

#
# def bubbleSort(alist):
#     for j in range(1,len(alist)):
#         print("Pass",j)
#         for i in range(1,len(alist)):
#             if alist[i-1] > alist[i]:
#                 print("Switch",alist[i-1],"and",alist[i])
#                 alist[i], alist[i-1] = alist[i-1], alist[i]
#             else:
#                 print("Don't switch",alist[i-1],"and",alist[i])
#         print(alist)
#
def insertionSort(lyst):
    counter= 0
    for i in range(1,len(lyst)):
        for j in range(i-1,-1,-1):
            if lyst[j] > lyst[j+1]:
                lyst[j],lyst[j+1] = lyst[j+1], lyst[j]
            else:
                break
        print(lyst)
        counter+=1
    print(lyst)
#
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        print("merging",lefthalf,"and",righthalf)
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
        print("result of merge:",alist)

def quickSort(lyst):
    quickSort2(lyst,0,len(lyst)-1)
    print(lyst)

def quickSort2(lyst,low,hi):
    if low<hi:
        p = partition(lyst,low,hi)
        quickSort2(lyst,low,p-1)
        quickSort2(lyst,p+1,hi)

def get_pivot(lyst,low,hi):
    mid = (hi+low) //2
    pivot = hi
    if lyst[low] < lyst[mid]:
        if lyst[mid] < lyst[hi]:
            pivot = mid
    elif lyst[low] < lyst[hi]:
        pivot = low
    return pivot

def partition(lyst,low,hi):
    pivotIndex = get_pivot(lyst,low,hi)
    pivotValue = lyst[pivotIndex]
    lyst[pivotIndex], lyst[low] = lyst[low], lyst[pivotIndex]
    border = low
    for i in range(low,hi+1):
        if lyst[i] < pivotValue:
            border += 1
            lyst[i], lyst[border] = lyst[border], lyst[i]
    lyst[low], lyst[border] = lyst[border], lyst[low]
    return border

#
def main():

    lyst = [0,1,1,2,3,5,8,13,21,34,55,89,144,377,610,700]
    length = len(lyst)
    print(jumpSearch(lyst,55,length))

    # print(binarySearch(lyst,0,length,13))

    # bubbleSort(lyst)

    lyst2 = [7,8,5,4,9,2]

    # (insertionSort(lyst2))

    # mergeSort(lyst)

    (quickSort(lyst2))




main()


#
# def heapify(alist):
#     start = (len(alist) - 2) // 2  # the last internal node
#     while start >= 0:
#         print("Sifting: start =", start, " end =", len(alist) - 1)
#         siftDown(alist, start, len(alist) - 1)
#         start -= 1
# def siftDown(alist, start, end):
#     root = start
#     print("   siftDown: start =", start, "  end =", end)
#     while root * 2 + 1 <= end:
#         # initially, "child" is left child, "child+1" is right child
#         child = root * 2 + 1
#         # if there is a right child and it's bigger, use that
#         if child + 1 <= end and alist[child] < alist[child + 1]:
#             print("      using right child")
#             child += 1
#         else:
#             print("      using left child")
#         # if the bigger child is greater than parent, swap them
#         if child <= end and alist[root] < alist[child]:
#             print("      swapping", alist[root], "and", alist[child])
#             temp = alist[root]
#             alist[root] = alist[child]
#             alist[child] = temp
#             root = child
#         else:
#             print("      No need to swap", alist[root], "and", alist[child])
#             return
# def heapSort(alist):
#     print("Phase 1:  calling heapify to make the list a heap")
#     heapify(alist)
#     print("alist", alist, "is now a heap.")
#     print("\n\nPhase 2:")
#     end = len(alist) - 1
#     while end > 0:
#         print("moving root (largest element) to last position")
#         print("   swapping", alist[0], "and", alist[end])
#         temp = alist[0]
#         alist[0] = alist[end]
#         alist[end] = temp
#         print("   end of list is now " + str(end - 1) + ". Resift to fix heap")
#         siftDown(alist, 0, end - 1)
#         end -= 1


# def main():
#     myList = [13, 14, 94, 33, 82, 21, 59, 65, 23, 45, 27, 73, 25, 10]
#
#     heapSort(myList)
#     print(myList)
#
#
# main()
#
# class BSTree:
#     def __init__(self, initval, parent=None):
#         self.val = initval
#         self.left = None
#         self.right = None
#         self.parent = parent
#     def put(self, val):
#         self._put(val, self)  # call helper function
#     def _put(self, val, current):
#         if int(val) < int(current.val):
#             # add to left subtree
#             if current.left == None:
#                 current.left = BSTree(val, parent=current)
#                 print(val + " is new left child of " + current.val)
#             else:
#                 self._put(val, current.left)
#         else:
#             # add to right subtree
#             if current.right == None:
#                 current.right = BSTree(val, parent=current)
#                 print(val + " is new right child of " + current.val)
#                 # dummy=input("")
#             else:
#                 self._put(val, current.right)
#     def find_min(self):
#         # Gets minimum node in a subtree
#         current = self
#         while current.left != None:
#             current = current.left
#         return current
#     def replace_node_in_parent(self, pointer):
#         # go to my parent & make it point at â€œpointerâ€ instead of me
#         if self.parent.left == self:
#             self.parent.left = pointer
#         else:
#             self.parent.right = pointer
#         if pointer != None:
#             pointer.parent = self.parent
#     def getRootData(self):
#         return self.val
#     def setRootData(self,data):
#         self.val = data
#     def delete(self, item):
#         if item < self.getRootData():
#             self.left.delete(item) # recursive call
#         elif item > self.getRootData():
#             self.right.delete(item)
#         else:
#             # delete this node
#             if self.left != None and self.right != None:
#                 # both children are present
#                 successor = self.right.find_min()
#                 self.setRootData(successor.getRootData())
#                 successor.delete(successor.getRootData())
#             elif self.left != None:
#                 # the node has only a left child
#                 self.replace_node_in_parent(self.left)
#             elif self.right != None:
#                 # the node has only a right child
#                 self.replace_node_in_parent(self.right)
#             else:
#                 # this node has no children
#                 self.replace_node_in_parent(None)
#     def inOrder(self):
#         if self.left == None:
#             leftVal = ""
#         else:
#             leftVal = self.left.inOrder() + " "
#         if self.right == None:
#             rightVal = ""
#         else:
#             rightVal = " " + self.right.inOrder()
#         return (leftVal + self.val + rightVal)
#     def dumpTree(self):
#         if self.left != None:
#             print("left child of ", self.val, ":", self.left.val)
#             self.left.dumpTree()
#         if self.right != None:
#             print("right child of ", self.val, ":", self.right.val)
#             self.right.dumpTree()
#
#
# def main():
#     myTree = BSTree("100")
#     print("Root node is 100")
#     myTree.put("50")
#     myTree.put("150")
#     myTree.put("25")
#     myTree.put("125")
#     myTree.put("140")
#     myTree.put("110")
#     myTree.put("145")
#     myTree.put("75")
#     myTree.put("130")
#     myTree.put("175")
#
#     print(myTree.inOrder())
#     myTree.dumpTree()
#
#
#
# main()