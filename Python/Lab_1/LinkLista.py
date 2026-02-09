class ListElement:  # klasa elementu kolejki
    def __init__(self, val=0, last=None):  # konstruktor musi zawierać referencję do lastego elementuw kolejce
        self.v = val
        self.next = None
        if last != None:  # je?li istnieje last:
            last.next = self  # ustawia, że następujący po nim jest

class List:  # klasa Kolejki
    def __init__(self):
        self.begin = None  # ustawia że nie ma elementu na początku, ani na końcu
        self.koniec = None

    def add(self, val):  # metoda adde do kolejki
        el = ListElement(val, self.koniec)  # tworzy element
        self.koniec = el  # ustawia go na koniec
        if self.begin == None:  # i jeżli początek jest pusty
            self.begin = self.koniec  # ustawia go na koniec

    def deleteFIFO(self):       # usuwa element z początku
        if self.begin != None:  # żeby nie odwoływać się do None
            self.begin = self.begin.next

        if self.begin == None:  # jeżli okazało się, że już nie ma elementów
            self.koniec = None  # usuwa element z początku kolejki

    def deleteLIFO(self):   # usuwa element z końca
        tmp = self.begin    # zapamiętuyjemy adres początku

        while self.begin.next.next != None:
            self.begin = self.begin.next

        self.begin.next = None  # usówamy ostatni element
        self.begin = tmp        # ustawiamy adres poczatku listy

    def deleteOrderByVal(self, val):
        tmp = self.begin
        flag = False

        while self.begin != None:
            if self.begin.v == val:
                flag = True  # is element deleted?

                if tmp == self.begin:
                    tmp = self.begin.next
                elif self.begin.next != None:
                    last.next = self.begin.next
                    self.begin = last
                else:
                    last.next = None

            last = self.begin
            self.begin = self.begin.next

        if flag == False:
            print("Given element's value does not exist")
        else:
            print(f'Element(s) {val} was deleted')

        self.begin = tmp

    def deleteMax(self):
        max = tmp = self.begin

        while self.begin.next != None:
            if max.next.v < self.begin.next.v:
                max = self.begin
            self.begin = self.begin.next

        if tmp.v > max.next.v and max.next != None:
            print(f'Max element {tmp.v} was deleted')
            tmp = tmp.next
        elif max.next != None:
            print(f'Max element {max.next.v} was deleted')
            max.next = max.next.next
        else:
            print(f'List is empty')

        self.begin = tmp

    def deleteMin(self):
        min = tmp = self.begin

        while self.begin.next != None:
            if min.next.v > self.begin.next.v:
                min = self.begin
            self.begin = self.begin.next

        if tmp.v < min.next.v and min.next != None:
            print(f'Min element {tmp.v} was deleted')
            tmp = tmp.next
        elif min.next != None:
            print(f'Min element {min.next.v} was deleted')
            min.next = min.next.next
        else:
            print(f'List is empty')

        self.begin = tmp

    def get(self):  # zwraca pierwszy element z kolejki
        if self.begin != None:
            return self.begin.v
        return None

    def isEmpty(self):  # sprawdza, czy jest pusta
        if self.begin != None:
            return False
        return True

    def printList(self):
        tmp = self.begin
        print("| ", end = '')
        while self.begin != None:
            print(f'{self.begin.v} | ', end = '')
            self.begin = self.begin.next

        print()
        self.begin = tmp

s = List()
s.add(1)
s.add(2)
s.add(2)
s.add(3)
s.add(3)
s.add(4)
s.add(5)

s.printList()

s.deleteOrderByVal(3)
s.printList()

s.deleteMax()
s.printList()

s.deleteMin()
s.printList()

print("FIFO")
s.deleteFIFO()
s.printList()

print("LIFO")
s.deleteLIFO()
s.printList()
