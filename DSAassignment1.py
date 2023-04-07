####Question1### 
def find_pairs(array, target_sum):
        pairs = []
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                if array[i] + array[j] == target_sum:
                    pairs.append((array[i], array[j]))
        return pairs


array = [1, 2, 3, 4, 5, 6]
#array=input("Enter the list of numbers:").split(",")
target_sum = 7
pairs = find_pairs(array, target_sum)
print(pairs)


###Question2####
def reverse_array(array):
        start_index = 0
        end_index = len(array) - 1
        while start_index < end_index:
            # Swap the elements at the start and end indices
            array[start_index], array[end_index] = array[end_index], array[start_index]
            
            # Move the start and end indices towards each other
            start_index += 1
            end_index -= 1

array = [1, 2, 3, 4, 5, 6]
print("The array is:",array)
res=reverse_array(array)
print("The reversed array is:",array)


###Question 3#####
def is_rotation(str1, str2):
        if len(str1) != len(str2):
            return False
        
        str3 = str1 + str1
        if str2 in str3:
            return True
        else:
            return False
        
str1 = input("Enter the string")#"rotation"
str2 = input("Enter the reversed string:")#"tationro"
result = is_rotation(str1, str2)
if result is True:
     print("Strings are rotation of each other")
else:
    print("Strings are not rotation of each other")    



####Question 4#####
def find_non_repeated_char(string):
        char_count = {}
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char in string:
            if char_count[char] == 1:
                return char
        return None

string = input("Enter the string:")#"hello world"
result =find_non_repeated_char(string)
print("The first non repeated character is :",result)
            


####Question 5#####
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

N=int(input("Enter the number of disks:"))
tower_of_hanoi(N, 'A', 'B', 'C')



####Queston 6#####
class PostfixToPrefix:
    def __init__(self, postfix_expr):
        self.postfix_expr = postfix_expr
        self.stack = []
        
    def convert(self):
        for token in self.postfix_expr.split():
            if token.isdigit():
                self.stack.append(token)
            else:
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                self.stack.append(f"{token} {operand1} {operand2}")
        return self.stack[-1]

postfix_expr = "3 4 + 5 *"
converter = PostfixToPrefix(postfix_expr)
prefix_expr = converter.convert()
print(prefix_expr)


####Question 7#####

class PrefixToInfix:
    
    def __init__(self, expression):
        self.expression = expression
        
    def is_operand(self, char):
        return char.isalpha() or char.isdigit()
    
    def convert(self):
        stack = []
        for char in reversed(self.expression):
            if self.is_operand(char):
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append("(" + operand1 + char + operand2 + ")")
        return stack.pop()
prefix_expression = "**+abc+de"
converter = PrefixToInfix(prefix_expression)
infix_expression = converter.convert()
print(infix_expression) 



#####Question 8#####
class BracketChecker:
    
    def __init__(self, code_snippet):
        self.code_snippet = code_snippet
        
    def check_brackets(self):
        stack = []
        for char in self.code_snippet:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in [")", "}", "]"]:
                if not stack:
                    return False
                elif char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return not stack
    
code_snippet = "def my_function():\n\tif x == y:\n\t\tprint('x equals y')\n\telse:\n\t\tprint('x does not equal y')"
checker = BracketChecker(code_snippet)
brackets_closed = checker.check_brackets()
if brackets_closed:
    print("All brackets are closed")
else:
    print("There is a bracket mismatch")


#####Question 9#####
class Stack:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

class StackReverser:
    
    def __init__(self, stack):
        self.stack = stack
        
    def reverse_stack(self):
        reversed_stack = []
        while not self.stack.is_empty():
            reversed_stack.append(self.stack.pop())
        return reversed_stack
    
reverser = StackReverser(stack)
reversed_stack = reverser.reverse_stack()
print("The reversed stack is:",reversed_stack)


####Question 10#####
class Stack:
    
    def __init__(self):
        self.items = []
        self.min_items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        if len(self.min_items) == 0 or item <= self.min_items[-1]:
            self.min_items.append(item)
        
    def pop(self):
        if self.is_empty():
            return None
        item = self.items.pop()
        if item == self.min_items[-1]:
            self.min_items.pop()
        return item
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def smallest(self):
        if len(self.min_items) == 0:
            return None
        return self.min_items[-1]

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(8)
stack.push(1)
stack.push(4)

print("The smallest number in the stack is:",stack.smallest())










