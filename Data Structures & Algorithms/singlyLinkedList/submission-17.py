class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            else:
                i += 1
                curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        tmp = ListNode(val)
        if self.head != None:
            tmp.next = self.head
            self.head = tmp
        else:
            self.head = tmp
            self.tail = tmp


    def insertTail(self, val: int) -> None:
        tmp = ListNode(val)

        if self.head is None:
            self.head = tmp
            self.tail = self.head
        else:
            self.tail.next = tmp
            self.tail = tmp
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        if index == 0 and curr:
            self.head = curr.next
            return True
        while i != index-1 and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False

    def getValues(self) -> list[int]:
        curr = self.head
        val_arr = []
        while curr:
            val_arr.append(curr.val)
            curr = curr.next
        return val_arr
        