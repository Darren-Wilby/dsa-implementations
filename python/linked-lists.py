class SingleNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList(object):

    def __init__(self):
        """
        This constructor creates an empty singly linked list with a head node set to None
        and initialises the size of the list to 0.
        """
        self.head = None
        self.size = 0


    def get(self, index) -> int:
        """
        Retrieves the value of the node at the specified index in the linked list.
        If the provided index is invalid (less than 0 or greater than
        or equal to the list size), it returns -1.

        :param index: The index of the node to retrieve.
        :type index: int
        :return: The value of the node at the specified index or -1 if the index is invalid.
        :rtype: int

        Complexity:
            - Time:     O(n), where n is the index of the node to retrieve.
            - Space:    O(1)
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.val


    def addAtHead(self, val) -> None:
        """
        Inserts a new node with the specified value at the beginning of the
        linked list. After the insertion, the new node becomes the head of the list.

        :param val: The value to insert into the linked list.
        :type val: int
        :rtype: void

        Complexity:
            - Time:     O(1)
            - Space:    O(1)
        """
        node = SingleNode(val)
        node.next = self.head
        self.head = node

        self.size += 1


    def addAtTail(self, val) -> None:
        """
        Appends a new node with the specified value to the end of the linked
        list. If the list is empty, it creates the head node with the given value.

        :param val: The value to append to the linked list.
        :type val: int
        :rtype: void

        Complexity:
            - Time:     O(n), where n is the size of the linked list.
            - Space:    O(1)
        """
        curr = self.head
        if curr is None:
            self.head = SingleNode(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = SingleNode(val)

        self.size += 1


    def addAtIndex(self, index, val) -> None:
        """
        This method adds a new node with the specified value at the specified index
        in the linked list. If the provided index is less than 0, the node is added
        at the beginning of the list. If the index is greater than or equal to the
        list size, the node is not inserted.

        :param index: The index at which to insert the new node.
        :param val: The value to insert into the linked list.
        :type index: int
        :type val: int
        :rtype: void

        Complexity:
            - Time:     O(n), where n is the index at which the node is inserted.
            - Space:    O(1)
        """
        if index == 0:
            self.addAtHead(val)
        elif 0 < index <= self.size: 
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = SingleNode(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index) -> None:
        """
        Deletes the node at the specified index in the linked list if the index is valid.
        If the index is less than 0 or greater than or equal to the list size, no deletion occurs.

        :param index: The index of the node to delete.
        :type index: int
        :rtype: void

        Complexity:
            - Time:     O(n), where n is the index of the node to delete.
            - Space:    O(1)
        """
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

    def hasCycle(self) -> bool:
        """
        This method uses the Floyd's cycle-finding algorithm to determine whether
        there is an infinite cycle in the linked list.

        :rtype: bool

        Complexity:
            - Time:     O(n), where n is the number of nodes in the linked list.
            - Space:    O(1)
        """
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
    
    def detectCycle(self) -> [int, None]:
        """
        This method uses the Floyd's cycle-finding algorithm to detect and return the
        node where the cycle in the linked list starts. If there is no cycle, it returns
        None.

        :rtype: SingleNode or None

        Complexity:
            - Time:     O(n), where n is the number of nodes in the linked list.
            - Space:    O(1)
        """
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = self.head
                while True:
                    if slow == fast:
                        return slow
                    slow = slow.next
                    fast = fast.next
                
        return None
    
    def reverseList(self) -> any:
        """
        This method reverses the order of the nodes in the linked list and returns
        the new head of the reversed list.

        :rtype: SingleNode or None

        Complexity:
            - Time:     O(n), where n is the number of nodes in the linked list.
            - Space:    O(1)
        """
        prev = None
        
        while self.head:
            temp = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = temp
            
        return prev
    
    def removeElements(self, val: int) -> any:
        """
        This method goes through the linked list, removing all nodes that have a
        value equal to the provided 'val'. It does so by adjusting pointers accordingly
        to bypass nodes with the specified value.

        :param val: The value to remove from the linked list.
        :type val: int
        :return: The head of the modified linked list with 'val' removed or None if the linked list becomes empty.
        :rtype: SingleNode or None

        Complexity:
            - Time:     O(n), where n is the number of nodes in the linked list.
            - Space:    O(1)
        """
        dummy = SingleNode()
        prev = dummy
        prev.next = self.head
        
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        
        return dummy.next


    def oddEvenList(self) -> any:
        """
        Rearranges the linked list so that odd-indexed nodes precede even-indexed nodes.

        This method modifies the order of the linked list nodes, placing odd-indexed nodes
        first, followed by even-indexed nodes. It achieves this by separating the list into
        two parts: one for odd-indexed nodes and another for even-indexed nodes, and then
        recombining them in the desired order.

        Example:
            Consider a linked list  [1] -> [2] -> [3] -> [4] -> [5]. Calling oddEvenList() on this list
            would rearrange it to   [1] -> [3] -> [5] -> [2] -> [4].

        Returns:
            any: The head of the modified linked list, or None if the list is empty.

        Note:
            - This method modifies the original linked list structure.
            - If the list contains less than two nodes, it remains unchanged.

        Complexity:
            - Time:     O(n), where n is the number of nodes in the linked list. The method iterates through the list once.
            - Space:    O(1), as it only uses a constant amount of extra space for pointers.
        """
        if not self.head:
            return None
        
        odd = self.head
        even = self.head.next
        even_head = even
        
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return self.head


    def isPalindrome(self) -> bool:
        """
        Checks if the elements in the linked list form a palindrome.

        This method determines whether the elements in the single-linked list form a
        palindrome, meaning they read the same forwards and backwards. The function
        uses a two-pointer approach to find the middle of the list and reverses the
        second half of the list to compare it with the first half. The list is altered
        during the process.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.

        Note:
            This method modifies the linked list structure as it reverses the second
            half temporarily for comparison. Make sure to create a copy of the original
            list if you need to preserve the original structure.

        Example:
            Consider a single-linked list with values [1, 2, 3, 2, 1]. Calling
            isPalindrome() on this list would return True, as it forms a palindrome.

        Complexity:
        - Time:     O(n), where n is the number of elements in the linked list.
        - Space:    O(1), as it only uses a constant amount of extra space for pointers.
        """
        mid = end = self.head
        while end and end.next:
            mid = mid.next
            end = end.next.next
            
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        start = self.head
        while start and prev:
            if start.val != prev.val:
                return False
            start = start.next
            prev = prev.next
            
        return True