# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def forsearch(array, size, search):
    gasit = 0
    for i in range(size):
        if array[i] == search:
            if gasit==1:
               " print(",")"
            print("Valoarea cautata",search,"se afla la pozitia",i)
            gasit=1
    if gasit == 0:
        print("Valoarea ", search, " nu a fost gasita.")
    return -1

data = [1 , 2 , 2, 3, 4, 5, 2]
size = len(data)
value = 2
forsearch(data, size, value)
