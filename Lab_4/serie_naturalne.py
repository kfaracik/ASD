# wykorzystanie posortowanych już serii naturalnych może usprawnić działanie mergeSort

def findNaturalSeries(t, series):   # O(n)
    seriesCounter = 1
    series[0] = seriesCounter
    for i in range(1, len(t)):
        if t[i] > t[i-1]:
            series[i] = seriesCounter
        else:
            seriesCounter+=1
            series[i] = seriesCounter

def section(series, series_to_find):
    if series_to_find > series[len(series)-1]:  # spr czy podana liczba nie przekracza dopuszczlnej
        return -1

    begin = -1
    for i in range(len(series)):
        if series[i] == series_to_find and begin == -1:
            begin = i
        elif series[i] != series[begin] and begin != -1:
            return begin, i - 1     # i-1 = koniec przedziału

t = [1,2,4, 3,5,7, 6, 1]
series = [0]*len(t)

findNaturalSeries(t, series)
print(series)

begin, end = section(series, 3)
print(begin, end)
