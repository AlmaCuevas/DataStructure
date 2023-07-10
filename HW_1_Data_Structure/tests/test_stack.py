from stack import top, push, pop

stack_list = [1,2,3]

assert(push(stack_list, 3) == [1,2,3,3])
assert(pop(stack_list) == [1,2])
assert(top(stack_list) == 3)

print("---Stack works---")
