
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    head = None
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def insert_at_index(self, data, index):
        if index < 0:
            raise IndexError("Index out of range")
        elif index == 0:
            self.insert_at_start(data)
        else:
            current = self.head
            for _ in range(index-1):
                if current is None or current.next is None:
                    raise IndexError("Index out of range")
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def delete_at_start(self):
        if self.head is None:
            raise IndexError("List is empty")
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        elif index == 0:
            self.delete_at_start()
        else:
            current = self.head
            for _ in range(index-1):
                if current is None or current.next is None:
                    raise IndexError("Index out of range")
                current = current.next
            if current.next is None:
                current.next = None
            else:
                current.next = current.next.next

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        if current is None:
            return
        while current:
            yield current.data
            if current.next is None:
                return
            current = current.next


def main():
    linked_list = LinkedList()
    linked_list.insert_at_start(1)
    linked_list.insert_at_start(2)
    linked_list.insert_at_start(3)
    linked_list.insert_at_start(4)
    linked_list.insert_at_start(5)
    # linked_list.insert_at_index(55, 6)  # IndexError: Index out of range
    # linked_list.insert_at_index(-10, 55)  # IndexError: Index out of range
    print(linked_list)
    linked_list.insert_at_end(6)
    linked_list.insert_at_end(7)
    linked_list.insert_at_end(8)
    linked_list.insert_at_end(9)
    linked_list.insert_at_end(10)
    print(linked_list)
    linked_list.insert_at_index(0, 0)
    linked_list.insert_at_index(11, 11)
    linked_list.insert_at_index(100, 5)
    print(linked_list)
    print("length: ", len(linked_list))
    linked_list.delete_at_start()
    linked_list.delete_at_start()
    linked_list.delete_at_start()
    linked_list.delete_at_start()
    linked_list.delete_at_start()
    print(linked_list)
    linked_list.delete_at_end()
    linked_list.delete_at_end()
    linked_list.delete_at_end()
    linked_list.delete_at_end()
    linked_list.delete_at_end()
    print(linked_list)
    linked_list.delete_at_index(0)
    # linked_list.delete_at_index(3)  # IndexError: Index out of range
    linked_list.delete_at_index(2)
    print(linked_list)
    linked_list.delete_at_index(1)
    print(linked_list)
    linked_list.delete_at_index(0)
    print("empty", linked_list)
    print("length: ", len(linked_list))

    linked_list2 = LinkedList()
    linked_list2.insert_at_start(1)
    linked_list2.insert_at_start(2)
    linked_list2.insert_at_start(3)
    linked_list2.insert_at_start(4)
    linked_list2.insert_at_start(5)


    print("iterator", linked_list2)
    iterator = iter(linked_list2)
    # print(iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator))  # StopIteration


if __name__ == "__main__":
    main()
