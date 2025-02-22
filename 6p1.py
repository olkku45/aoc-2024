import numpy as np

with open("6.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

rows = len(matrix)
cols = len(matrix[0])


def rotate_matrix(matrix):
    mlength = len(matrix)

    for i in range(mlength // 2):
        for j in range(i, mlength - i - 1):
            temp = matrix[i][j]

            # left to top
            matrix[i][j] = matrix[mlength - j - 1][i]
            # bottom to left
            matrix[mlength - j - 1][i] = matrix[mlength - i - 1][mlength - j - 1]
            # right to bottom
            matrix[mlength - i - 1][mlength - j - 1] = matrix[j][mlength - i - 1]
            # right to top
            matrix[j][mlength - i - 1] = temp
    
    return matrix


flag = False

while not flag:
    flag = False

    for x in range(1, rows):
        for y in range(cols):

            if matrix[x][y] == "^":

                if matrix[x - 1][y] == "#":
                    rotate_matrix(matrix)
                    continue

                matrix[x][y], matrix[x - 1][y] = matrix[x - 1][y], matrix[x][y]
                
                if matrix[x - 1][y] == ".":
                    matrix[x - 1][y] = "X"

                for sublist in matrix:
                    if sublist == matrix[0]:
                        if "^" in sublist:
                            matrix[x][y] = "X"
                            flag = True

        if flag == True:
            break
        
    for row in matrix:
        print("".join(row))
    print("\n" + "-"*20 + "\n") 



'''löydetään se 'view', jossa vartija on alempana, eli
listan toinen alkio, ja jos ensimmäinen alkio on piste,
niin vaihdetaan vartijan (nuolen) ja pisteen paikkaa. 
tämän jälkeen voisi tämän entisen vartijan paikan tilalle
laittaa ruksin X, merkkaamaan paikkaa, jossa vartija on
käynyt. entä jos tulee tilanne, että vartija menee 
reittiä, jossa on jo käynyt? luulisin, että näin ei voisi
käydä. 
joka loopin iteraatiolla löydetään paikka, jossa 
vartija on alempana, siis. sitten, jos tulee tilanne,
että vartijan edessä on este, eli risuaita '#', niin
silloin otetaan vartijan oikean puolinen alkio, ja
vaihdetaan vartijan paikka yhden oikealle, vain 
siinä tilanteessa, jos vartijan oikealla puolella on 
piste. vai voisiko tämän prosessin tehdä itseasiassa
niin, että otetaan koko tekstitiedosto matriisiksi. 
ja kun tulee #-este vastaan, niin käännetään matriisi 
myötäpäivään. tehdään kuitenkin tässä sama homma, että
vartijan ja pisteen paikka vaihdetaan, ja vaihdetun 
pisteen tilalle laitetaan ruksi. juu voisi tehdä homman
oikeastaan näin, tulee olemaan paljon helpompaa luulisin'''