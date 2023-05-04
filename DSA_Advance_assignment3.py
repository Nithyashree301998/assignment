##########Question 1#########
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):

      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()


##########Question 2#########
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):

    if root is None:
      return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)

    return max(leftAns, rightAns) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left =Node(4)
 
print("Height of the binary tree is: " + str(height(root)))


###########Question 3###########
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):

      if self.data is None:
         self.data=data
         return
      if self.data>data:
         if self.left:
           self.left.insert(data)
         else:
           self.left=Node(data)
      else:
         if self.right:
            self.right.insert(data)
         else:
            self.right=Node(data)  

  

   def inorder_traversal(self):
      if self.left:
         self.left.inorder_traversal()
      print(self.data)
      if self.right:
         self.right.inorder_traversal()

   def preorder_traversal(self):
      print(self.data)
      if self.left:
         self.left.preorder_traversal()
      if self.right:
         self.right.preorder_traversal()

   def postorder_traversal(self):
      if self.left:
         self.left.postorder_traversal()
      if self.right:
         self.right.postorder_traversal()     
      print(self.data)
      

root = Node(20)
l=[17,28,32,16,23]
for i in l:
   root.insert(i)
print("Inorder traversal:")
root.inorder_traversal()
print("Preorder traversal:")
root.preorder_traversal()
print("Postorder traversal:")
root.postorder_traversal()


#######Question 4##########
class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(root: Node) -> None:

    if (not root):
        return

    if (not root.left and
        not root.right):
        print(root.data,
              end = " ")
        return

    if root.left:
        printLeafNodes(root.left)

    if root.right:
        printLeafNodes(root.right)
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(8)
root.right.left.left = Node(6)
root.right.left.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)
printLeafNodes(root)
 
########Question 5########

queue=[]
output=[]
def bfs(node,queue,graph):
    queue.append(node)
    output.append(node)
    while queue:
        item=queue.pop(0)
        print(item, end=' ')
        for i in graph[item]:
            if i not in output:
                queue.append(i)
                output.append(i)
graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print("\nFollowing is Breadth First Traversal: ")
bfs(0,queue,graph)


def dfs(node,visited,graph):
    if node not in visited:
        print("\n", node)
        visited.add(node)
        for i in graph[node]:
           dfs(i,visited,graph)
graph={5:[3,7],3:[2,4,5],7:[5,8],2:[3],4:[3,8],8:[4,7]}
visited=set()
result=dfs(5,visited,graph)
print(result)    

#########Question 6##########
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

def leftLeavesSum(root):

    res = 0
    if root is not None:

        if isLeaf(root.left):
            res += root.left.key
        else:

            res += leftLeavesSum(root.left)
 
        res += leftLeavesSum(root.right)
    return res

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)       
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))


##########Question 7#########
def SumNodes(l):

    leafNodeCount = pow(2, l - 1)

    vec = [[] for i in range(l)]

    for i in range(1, leafNodeCount + 1):
        vec[l - 1].append(i)

    for i in range(l - 2, -1, -1):
        k = 0

        while (k < len(vec[i + 1]) - 1):

            vec[i].append(vec[i + 1][k] +
                          vec[i + 1][k + 1])
            k += 2
 
    Sum = 0

    for i in range(l):
        for j in range(len(vec[i])):
            Sum += vec[i][j]
 
    return Sum

l = 3
print(SumNodes(l))

#########Question 8########
class getNode:
    def __init__(self, data):

        self.data = data
        self.left = self.right = None

def countSubtreesWithSumX(root, count, x):

    if (not root):
        return 0

    ls = countSubtreesWithSumX(root.left, count, x)

    rs = countSubtreesWithSumX(root.right, count, x)

    Sum = ls + rs + root.data

    if (Sum == x):
        count[0] += 1

    return Sum
 
def countSubtreesWithSumXUtil(root, x):

    if (not root):
        return 0
 
    count = [0]

    ls = countSubtreesWithSumX(root.left, count, x)

    rs = countSubtreesWithSumX(root.right, count, x)

    if ((ls + rs + root.data) == x):
        count[0] += 1

    return count[0]

root = getNode(5)
root.left = getNode(-10)
root.right = getNode(3)
root.left.left = getNode(9)
root.left.right = getNode(8)
root.right.left = getNode(-4)
root.right.right = getNode(7)
x = 7
print("Count =",countSubtreesWithSumXUtil(root, x))


#########Question 9##########
from collections import deque

class Node:
    def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None

def maxLevelSum(root):

    if (root == None):
        return 0

    result = root.data

    q = deque()
    q.append(root)
     
    while (len(q) > 0):

        count = len(q)

        sum = 0
        while (count > 0):

            temp = q.popleft()

            sum = sum + temp.data

            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
                 
            count -= 1   

        result = max(sum, result)
 
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)
print("Maximum level sum is", maxLevelSum(root))


######Question 10########
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):

    if (root == None):
        return

    if (isOdd):
        print(root.data, end = " ")
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.right = newNode(6)
root.right.left = newNode(7)
printOddNodes(root)
 
 
 
