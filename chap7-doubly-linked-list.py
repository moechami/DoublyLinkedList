class DNode:
    def __init__(self, ele=None):
        self.ele = ele
        self.left = None
        self.right = None


class DLinkedList:
    def __init__(self):
        self.header = DNode()
        self.trailer = DNode()
        self.header.right = self.trailer
        self.trailer.left = self.header

    def empty(self):
        return self.header.right == self.trailer and self.trailer.left == self.header

    def front(self):
        return self.header.right.ele

    def back(self):
        return self.trailer.left.ele

    def add(self, v, e):
        u = DNode(e)
        u.right = v
        u.left = v.left
        v.left.right = u
        v.left = u

    def add_front(self, e):
        self.add(self.header.right, e)

    def add_back(self, e):
        self.add(self.trailer, e)

    def remove(self, v):
        u = v.left
        w = v.right
        u.right = w
        w.left = u

    def remove_front(self):
        if not self.empty():
            self.remove(self.header.right)

    def remove_back(self):
        if not self.empty():
            self.remove(self.trailer.left)

    def find(self, element):
        # First we must create a variable named "current" to keep track of what element we are at in the linked list
        current = self.header.right
        # Then we must create a loop to iterate through the list and check to see if any of the elements match
        # Make sure the loop returns None if the element isn't found
        while current != self.trailer:
            if current.ele == element:
                return current
            current = current.right # iterate to the next element
        return None

    def insert_after(self, existing_element, new_element):
        # first create a variable to locate the existing element
        node = self.find(existing_element)
        # then use a conditional to check that the element exists, and if it does, add the new node to the right of it
        if node != None:
            self.add(node.right, new_element)
        else:
        # if the provided element hasn't been found, then print a suitable message
            print(f"Element {existing_element} is not found in this list.")

    def reverse(self):
        # create a "current" variable and assign it to the sentinel header node
        current = self.header
        # loop through the nodes
        while current != None:
            # change what the current nodes point to, to the opposite
            current.left, current.right = current.right, current.left
            current = current.left #after you swap, move on to the next node

        # this swaps the header and the trailer
        self.header, self.trailer = self.trailer, self.header

    def print_list(self):
        temp = self.header.right
        if temp == self.trailer:  # List is empty if header's right points to trailer
            print("List is empty")
            return

        while temp != self.trailer:
            print(temp.ele)
            temp = temp.right

if __name__ == "__main__":
    # Initialize a DLinkedList object
    list = DLinkedList()

    # Is list empty? Yes, because none of the elements have been inserted yet
    print(f"Is the list empty: {'True' if list.empty() else 'False'}")

    # Add Elements at front and back
    list.add_front("JFK")
    list.add_front("PVD")
    list.add_front("SFO")

    # Print Front and back elements in the list
    print(f"Front: {list.front()}")
    print(f"Back: {list.back()}")

    e = "PVD"
    # 1. todo list.find(e)
    list.find(e)

    # 2. todo insert after a given element
    # insert_after(e, "BWI")
    list.insert_after(e, "BWI")

   # Print all the elements
    print("List after adding BWI before PVD")
    list.print_list()
    print()

    # 3.todo reverse()
    print("Reversed List:")
    list.reverse()
    list.print_list()

    # Check if the list is empty now
    print(f"Is the list empty: {'True' if list.empty() else 'False'}")

    # Remove elements at front
    print("List before removing front")
    list.print_list()
    print()

    list.remove_front()
    print("List after removing front")
    list.print_list()

    # Remove elements at back
    list.remove_back()
    print("List after removing back")
    list.print_list()

    # Check if the list is empty now
    print(f"Is the list empty: {'True' if list.empty() else 'False'}")
