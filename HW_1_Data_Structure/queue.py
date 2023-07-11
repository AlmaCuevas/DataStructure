# Simple interpretation from concept

from typing import List, Any

def enqueue(queue_list: list, x) -> List[Any]:
    """
    Insert operation. When an element is added, it takes place at the tail of the queue.
    :return: queue_list
    """
    return queue_list + [x]

def dequeue(queue_list: list) -> List[Any]:
    """
    Delete operation. The element dequeued is always the one at the head of the queue.
    :param queue_list:
    :param x:
    :return: queue_list
    """
    if len(queue_list) == 0:
        print("Nothing to dequeue")
    return queue_list[1:]
