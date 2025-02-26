import numpy as np
import random
import time
start_time = time.time()

random_number = random.randint(1, 1000)

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
time_from_rotation = 0  # think of better name for this (maybe delete)
index = 0

while not flag:
    flag = False  # flag for checking whether guard has reached the top row
    rotation = False
    rotation_counter = 0

    for x in range(1, rows):  # x -> y, rows -> cols
        for y in range(cols):  # y -> x, cols -> rows

            if matrix[x][y] == "^":

                if matrix[x - 1][y] == "#":
                    matrix = rotate_matrix(matrix)
                    rotation = True
                    rotation_counter += 1
                    '''print(f"iter. rotation counter: {rotation_counter}")'''
                    continue

                else:
                    matrix[x][y], matrix[x - 1][y] = matrix[x - 1][y], matrix[x][y]
                    matrix[x][y] = "X"

                '''if time_from_rotation == 1 and rotation_counter != 2:
                    if matrix[x + 1][y + 1] == ".":
                        matrix[x + 1][y + 1] = "X"
                        time_from_rotation -= 1        

                else:
                    pass'''
                
                '''if rotation_counter == 1 and matrix[x + 1][y] != "X":
                    #matrix[x + 1][y] = "O"
                    if matrix[x][y + 1] == ".":
                        matrix[x][y + 1] = "X"'''

                # change guard's position forward
                '''matrix[x][y], matrix[x - 1][y] = matrix[x - 1][y], matrix[x][y]'''

                '''if not rotation and not first_move:  # kind of crude fix, don't add "X" on the first move because then there is an extra X
                    if matrix[x + 1][y] == ".":
                        matrix[x + 1][y] = "X"'''

                # if guard is at the top row
                if "^" in matrix[0]:
                    col_index = matrix[0].index("^")
                    matrix[0][col_index] = "X"

                    if rows > 1 and matrix[1][col_index] == ".":
                        matrix[1][col_index] = "X"
                    
                    '''if matrix[x + 1][y + 1] == ".":
                        matrix[x + 1][y + 1] = "X"'''

                    flag = True

                first_move = False

        # break loop after guard has gotten to the top row
        if flag == True:
            break
    
    index += 1

    if rotation:
        time_from_rotation += 1

    # DEBUG
    if index == random_number:  
        for row in matrix:
            print("".join(row))
        print("\n" + "-"*20 + "\n")

position_counter = 0

for line in matrix:
    for character in line:
        if character == "X":
            position_counter += 1

print(position_counter)
print("--- %s seconds ---" % (time.time() - start_time))


'''tässä on varmaan vikana se, että kun
käännytään, niin lisätään X myöhässä (vasta käännöksen jälkeen)
siihen paikkaan, ennen paikkaa, josta käännyttiin. voi
tulla joku rajatapaus, että on # heti kääntymisen jälkeen, 
jolloin käännytään heti edellisen käännön jälkeen
eli siis vain käännytään 180 astetta ympäri,
ja tällöin tulee lisättyä ylimääräinen X, kun ohjelma
laskee nämä kaksi käännöstä yhdeksi (syistä), jolloin
kun käännytään ympäri, niin lisätään X yhden askeleen
alas ja oikealle, jota ei pitäisi tietenkään tehdä, kun
vartija ei ole käynyt siinä paikassa.'''

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