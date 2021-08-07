def test_push_pop_peek():
    stack = Stack()
    for i in range(1,10):
        stack.push(i)
    stack.push(10)
    assert stack.top.value == 10
    assert stack.pop() == 9
    assert stack.peek() == 9

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
