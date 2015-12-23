# cyclic-right-shift.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
from linked_list_prototype import ListNode


# @include
def cyclically_right_shift_list(L, k):
    if not L:
        return L

    # Computes the length of L and the tail.
    tail = L
    n = 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L

    tail.next = L  # Makes a cycle by connecting the tail to the head.
    steps_to_new_head = n - k
    new_tail = tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head
# @exclude


def main():
    L = ListNode(
        1, ListNode(
            2, ListNode(3, None)))
    result = cyclically_right_shift_list(L, 2)
    assert result.data == 2 and result.next.data == 3 and result.next.next.data == 1 and not result.next.next.next
    while result:
        print(result.data)
        result = result.next


if __name__ == '__main__':
    main()