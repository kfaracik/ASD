class Node:
    def __init__(self):
        self.next = None
        self.val = None

    def add(L, value):
        while L.next != None and value > L.next.val:        #   Dodaje w posortowanej kolejności
            L = L.next
        tmp = L.next
        L.next = Node()
        L.next.next = tmp
        L.next.val = value

def printList(list):
    while list != None:
        print(list.val)
        list = list.next



begin = Node()

begin.add(2)
begin.add(5)
begin.add(1)
begin.add(4)
begin.add(7)

printList(begin)
