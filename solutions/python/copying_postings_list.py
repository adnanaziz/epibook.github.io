# Copying_postings_list.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
from postings_list_prototype import ListNode


# @include
def copy_postings_list(L):
    if L is None:
        return None

    # Stage 1: Makes a copy of the original list without assigning the jump
    #          field, and creates the mapping for each node in the original
    #          list to the copied list.
    it = L
    while it:
        new_node = ListNode(it.data, it.next, None)
        it.next = new_node
        it = new_node.next

    # Stage 2: Assigns the jump field in the copied list.
    it = L
    while it:
        if it.jump:
            it.next.jump = it.jump.next
        it = it.next.next

    # Stage 3: Reverts the original list, and assigns the next field of
    #          the copied list.
    it = L
    new_list_head = it.next
    while it.next:
        temp = it.next
        it.next = temp.next
        it = temp
    return new_list_head
# @exclude


def check_postings_list_equal(a, b):
    while a and b:
        print(a.data, end=' ')
        assert a.data == b.data
        assert ((a.jump is None and b.jump is None) or
                (a.jump and b.jump and a.jump.data == b.jump.data))
        if a.jump:
            print(a.jump.data, end='')
        print()
        a = a.next
        b = b.next
    assert a is None and b is None


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 1000)
        L = curr = None
        for i in range(n):
            temp = ListNode(i, None)
            if L:
                curr.next = temp
                curr = temp
            else:
                curr = L = temp
            # Randomly assigned a jump node.
            jump_num = random.randint(0, i + 1)
            jump = L
            while jump_num:
                jump_num -= 1
                jump = jump.next
            temp.jump = jump

        copied = copy_postings_list(L)
        check_postings_list_equal(L, copied)


if __name__ == '__main__':
    main()
