import numpy as np

import time
start_time = time.time()

with open("6.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

rows = len(matrix)
cols = len(matrix[0])


def rotate_matrix(matrix):
    # thanks to https://stackoverflow.com/a/53251028
    # matrix rotation 90 degrees counter clockwise
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]


flag = False
first_move = True

while not flag:
    flag = False
    rotation = False

    for x in range(1, rows):
        for y in range(cols):

            if matrix[x][y] == "^":
                
                if matrix[x - 1][y] == "#":
                    matrix = rotate_matrix(matrix)
                    rotation = True
                    
                    for i in range(rows - 1): 
                        for j in range(cols - 1):  # n^4 time complexity is kinda bad tbh but whatever
                            if matrix[i][j] == "^" and matrix[i][j + 1] == ".":
                                matrix[i][j + 1] = "X"

                    continue

                if not rotation and not first_move:  # kind of crude fix, don't add "X" on the first move because then there is an extra X
                    if matrix[x + 1][y] == ".":
                        matrix[x + 1][y] = "X"

                matrix[x][y], matrix[x - 1][y] = matrix[x - 1][y], matrix[x][y]

                if "^" in matrix[0]:
                    col_index = matrix[0].index("^")
                    matrix[0][col_index] = "X"

                    if rows > 1 and matrix[1][col_index] == ".":
                        matrix[1][col_index] = "X"

                    flag = True

                first_move = False

        if flag == True:
            break
        
    '''for row in matrix:  # for debugging
        print("".join(row))
    print("\n" + "-"*20 + "\n")'''

position_counter = 0

for line in matrix:
    for character in line:
        if character == "X":
            position_counter += 1

print(position_counter)
print("--- %s seconds ---" % (time.time() - start_time))

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
'''for sublist in matrix:
    if sublist == matrix[0]:
        if "^" in sublist:
            matrix[x][y] = "X"
            flag = True'''
'''5158 too high'''