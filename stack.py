def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()


stack = create_stack()
push(stack, str(10))
push(stack, str(30))
push(stack, str(23))
push(stack, str(65))
print("popped item: " + pop(stack))
print(str(stack))
