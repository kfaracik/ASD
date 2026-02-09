# wydajny jeśli często zmieniamy rozmiar stosu
# zużywa 2x więcej pamięci niż stack_tab (bo organizacja danych - wskaźniki)

class Node:
    def __init__(self):
        self.next = None
        self.val = None

class Stack:
    def __init__(self):
        self.top = Node()   # wartownik

    def push(self, x):
        N = Node()
        N.val = x
        N.next = self.top
        self.top = N

    def pop(self):
        N = self.top.next
        self.top.next = N.next
        return N.val

    def is_empty(self):
        return self.top.next == None