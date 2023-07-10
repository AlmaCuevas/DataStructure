def top(stack_list: list) -> str:
    """
    :return: The value of top of the stack.
    """
    return stack_list[-1]

def push(stack_list: list, x):
    """
    :param stack_list:
    :param x:
    :return: Push x on top of the stack
    """
    return stack_list + [x]

# pop is delete and already exists
def pop(stack_list: list):
    return stack_list[:-1]
