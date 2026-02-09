# Algorytm zamortyzowany oszczędza pamięć ale gdy zależy nam na szybkości (np ukłądy bezpieczeństwa w samochodzie działania programu w każdym momencie to warto zastosować inne rozw

class Stack:
    def __init__(self, n):
        self.S = [None]*n
        self.n = nself.elements = 0

    def push(self, x):
        # powiększ tablicę 2x jak rozmiar tab jest za mały
        self.S[self.elements] = x
        self.elements +=1

    def pop(self):
        # jak stos ma mniej niż 1/4 el to zmniejsz tab do 1/2 el
        self.elements -+1
        return self.S[self.elements]

    def is_empty(self):
        return self.elements == 0

    #def stack_size(self):
    #    return self.elements


