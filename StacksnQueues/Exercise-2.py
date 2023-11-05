# Name : Anshu Kumar Singh
# Date : 05/11/23
# Title : Exercise 2 - 

'''
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing 
parenthesis in the correct order. For example, the string "((()))" has three pairs 
of balanced parentheses, so it is a balanced string. On the other hand, the string 
"(()))" has an imbalance, as the last two parentheses do not match, so it is not 
balanced.  Also, the string ")(" is not balanced because the close parenthesis needs 
to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is 
balanced, or False if it is not. In order to solve this problem, use a Stack data 
structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.
'''

from stack_main import Stack

def is_balanced_parentheses(parens):
    stack = Stack()
    for paren in parens:
        if paren == '(':
            stack.push(paren)
        elif paren == ')':
            if stack.is_empty() or stack.pop().value != '(':
                return False
    return stack.is_empty()


print("Enter a set of balanced parenthesis: ", end="")
parenthesis = input()

if is_balanced_parentheses(parenthesis):
    print("Good")
else:
    print("No these are not balanced!")



'''
I couldn't solve this one. I just kept thinking how it could be solved using stacks. 
All of my solutions were less efficient than if I hadn't used stacks. 

When I checked the solutions, I thought of this solution as a piece of art. Beautifully 
solved.
'''




