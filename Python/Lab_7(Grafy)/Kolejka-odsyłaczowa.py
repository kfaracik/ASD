class QueueElement:
    def __init__(self, val=0, last=None):  # konstruktor musi zawierać referencję do lastego elementuw kolejce
        self.v = val
        self.next = None
        if last != None:  # je?li istnieje last:
            last.next = self  # ustawia, że następujący po nim jest

class Queue:  # klasa Kolejki
    def __init__(self):
        self.begin = None  # ustawia że nie ma elementu na początku, ani na końcu
        self.koniec = None

    def add(self, val):  # metoda adde do kolejki
        el = QueueElement(val, self.koniec)  # tworzy element
        self.koniec = el  # ustawia go na koniec
        if self.begin == None:  # i jeżli początek jest pusty
            self.begin = self.koniec  # ustawia go na koniec

    def delete(self):  # usuwa element z początku
        if self.begin != None:  # żeby nie odwoływać się do None
            self.begin = self.begin.next

        if self.begin == None:  # jeżli okazało się, że już nie ma elementów
            self.koniec = None  # usuwa element z końca kolejki

    def get(self):  # zwraca pierwszy element z kolejki
        if self.begin != None:
            result = self.begin.v
            self.delete()
            return result
        return None

    def isEmpty(self):  # sprawdza, czy jest pusta
        if self.begin != None:
            return False
        return True


s = Queue()
print("Dodaj 1")
s.add(1)
print("Dodaj 2")
s.add(2)
print("Dodaj 3")
s.add(3)

print(s.get())
print(s.get())

print("Jest pusty: " + str(s.isEmpty()))

print(s.get())
print("Jest pusty: " + str(s.isEmpty()))
