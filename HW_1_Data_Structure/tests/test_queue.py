from queue import enqueue, dequeue

queue = []

# Enqueue
queue = enqueue(queue, 3)
queue = enqueue(queue, 4)
queue = enqueue(queue, 5)

assert queue == [3, 4, 5]

# Enqueue and Dequeue
queue = enqueue(queue, 'a')
queue = enqueue(queue, 'b')
queue = enqueue(queue, 'c')

queue = dequeue(queue)
queue = dequeue(queue)

assert queue == [5, 'a', 'b', 'c']

# Underflow
queue = dequeue(queue)
queue = dequeue(queue)
queue = dequeue(queue)
queue = dequeue(queue)
queue = dequeue(queue)
queue = dequeue(queue)

assert queue == []

print("---Queue works---")