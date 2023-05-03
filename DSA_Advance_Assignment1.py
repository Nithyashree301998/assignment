#****** QUESTION 1 *********
class Node():
  def __init__(self,data):
     self.data = data
     self.next = None

class Linkedlist():
   def __init__(self):
     self.head = None
    
   def append(self,data):
     new_node = Node(data)
     h = self.head
     if self.head is None:
         self.head = new_node
         return
     else:
         while h.next!=None:
             h = h.next
         h.next = new_node

   def remove_zeros_from_linkedlist(self, head):
     stack = []
     curr = head
     list = []
     while (curr):
         if curr.data >= 0:
             stack.append(curr)
         else:
             temp = curr
             sum = temp.data
             flag = False
             while (len(stack) != 0):
                 temp2 = stack.pop()
                 sum += temp2.data
                 if sum == 0:
                     flag = True
                     list = []
                     break
                 elif sum > 0:
                     list.append(temp2)
             if not flag:
                 if len(list) > 0:
                     for i in range(len(list)):
                         stack.append(list.pop())
                 stack.append(temp)
         curr = curr.next
     return [i.data for i in stack]

if __name__ == "__main__":
 l = Linkedlist()

 l.append(4)
 l.append(6)
 l.append(-10)
 l.append(8)
 l.append(9)
 l.append(10)
 l.append(-19)
 l.append(10)
 l.append(-18)
 l.append(20)
 l.append(25)
 print(l.remove_zeros_from_linkedlist(l.head))


 #********* QUESTION 2 **********
 class LinkedList:
  
    
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
        
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        
        if next is not None:
            head.next = self.reverse(next, k)
  
       
        return prev
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
  
  

llist = LinkedList()
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 2)
  
print ("\nReversed Linked list")
llist.printList()



#******** QUESTION 3*********
class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
  
  
class LinkedList(object):
    def __init__(self):
        self.head = None
          
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
       
        self.head = new_node
          
    
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
              
    
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head
  
        
        while p_curr != None and q_curr != None:
  
           
            p_next = p_curr.next
            q_next = q_curr.next
  
            
            q_curr.next = p_next  
            p_curr.next = q_curr  
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr
  
  
  

llist1 = LinkedList()
llist2 = LinkedList()
  

  

llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)
  

for i in range(8, 3, -1):
    llist2.push(i)
  
print("First Linked List:")
llist1.printList()
  
print("Second Linked List:")
llist2.printList()
  

llist1.merge(p=llist1, q=llist2)
  
print("Modified first linked list:")
llist1.printList()
  
print("Modified second linked list:")
llist2.printList()




#********* QUESTION 4**********8
def getPairsCount(arr, n, sum):
    count = 0 
 
    
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))




#********* QUESTION 5 **********
def findDuplicates(arr, Len):
     
    ifPresent = False
 
   
    a1 = []
    for i in range(Len - 1):
        for j in range(i + 1, Len):
 
            
            if (arr[i] == arr[j]):
                if arr[i] in a1:
                    break
                 
                
                else:
                    a1.append(arr[i])
                    ifPresent = True
 
    
    if (ifPresent):
        print(a1, end = " ")
    else:
        print("No duplicates present in arrays:")
 

arr = [ 12, 11, 40, 12, 5, 6, 5, 12, 11 ]
n = len(arr)
 
findDuplicates(arr, n)

#********** QUESTION 6 *********
def get_largest(array,k):
    arr = array.sort()
    print("\n" ,array[k-1])
    
def get_smallest(array,k):
   
    arr = array.sort()
    print(array[-k])

l = [1,4,9,3,6,8]
get_largest(l,3)
get_smallest(l,2)


#********* QUESTION 7 *********
def move(arr):
  arr.sort()
 

arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
move(arr)
for i in arr:
    print(i , end = " ")


#********* QUESTION 8 *******
def createStack():
    stack = []
    return stack
 
def size(stack):
    return len(stack)
 

def isEmpty(stack):
    if size(stack) == 0:
        return true
 

def push(stack, item):
    stack.append(item)
 

def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
 

 
 
def reverse(string):
    n = len(string)
    stack = createStack()
 
   
    for i in range(0, n, 1):
        push(stack, string[i])
 
    string = ""
 
    
    for i in range(0, n, 1):
        string += pop(stack)
 
    return string
 
string = "GeeksQuiz"
string = reverse(string)
print("\nReversed string is " + string)


#******** QUESTION 9 *********
class Evaluate:
 
   
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
         
      
        self.array = []
 
    
    def isEmpty(self):
        return True if self.top == -1 else False
 
    
    def peek(self):
        return self.array[-1]
 
   
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    def evaluatePostfix(self, exp):
 
        
        for i in exp:
 
            
            if i.isdigit():
                self.push(i)
 
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
 
        return int(self.pop())
 
 
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
    print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))



#**********  QUESTION 10 *********
class Queue: 
    def __init__(self):
        self.s1 = []
        self.s2 = []
  
    def enQueue(self, x):
          

        while len(self.s1) != 0: 
            self.s2.append(self.s1[-1]) 
            self.s1.pop()
 
        self.s1.append(x) 
  
        while len(self.s2) != 0: 
            self.s1.append(self.s2[-1]) 
            self.s2.pop()
   
    def deQueue(self):
 
        if len(self.s1) == 0: 
            print("Q is Empty")

        x = self.s1[-1] 
        self.s1.pop() 
        return x
  
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
  
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())