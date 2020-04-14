#Proszę zaproponować algorytm, który mając na wejściu dwa słowa, x i y, składające się z małych liter alfabetu łacińskiego sprawdzi, czy słowa te są anagramami (czyli zawierają tyle samo, tych samych liter).

def count(word, map, tab):
    for i in range(0,len(word)):
        for j in range(len(tab)):
            if word[i] == tab[j]:
                map[j] +=1

def compare(map1, map2):
    for i in range(len(map1)):
        if map1[i] != map2[i]:
            print("Words are differents")
            return 0
    print("Words are same")

tab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
map1 = [0]*len(tab)
map2 = [0]*len(tab)

word1 = "ala"
word2 = "ola"

count(word1, map1, tab)
count(word2, map2, tab)

compare(map1, map2)

