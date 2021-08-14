def test_PseudoQueue:
    queue = PseudoQueue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 4
    assert queue.dequeue() == 6
