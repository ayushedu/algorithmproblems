from mystack import MyStack

stack = MyStack()
input = [1,10,4,14,2]
print "Input:", input

for i in input:
    stack.push(i)

print "Stack top:", stack.peek()

ts = MyStack()

while(not stack.isEmpty()):
    top = stack.pop()
 
    while(not ts.isEmpty() and top > ts.peek()):
        stack.push(ts.pop())

    ts.push(top)

while(not ts.isEmpty()):
    print ts.pop()

