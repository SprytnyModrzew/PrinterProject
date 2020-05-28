InitialPermutation = \
[58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17,  9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7]

PermutedChoice1 = \
[57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4]

PermutedChoice2 = \
[14, 17, 11, 24, 1, 5,
3, 28, 15, 6, 21, 10,
23, 19, 12, 4, 26, 8,
16, 7, 27, 20, 13, 2,
41, 52, 31, 37, 47, 55,
30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53,
46, 42, 50, 36, 29, 32]

Expansion = \
[32,  1,  2,  3,  4,  5,
4,  5,  6,  7,  8,  9,
8,  9, 10, 11, 12, 13,
12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21,
20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29,
28, 29, 30, 31, 32,  1]

Permutation = \
[16,  7, 20, 21,
29, 12, 28, 17,
1, 15, 23, 26,
5, 18, 31, 10,
2,  8, 24, 14,
32, 27,  3,  9,
19, 13, 30,  6,
22, 11,  4, 25]

FinalPermutation = \
[40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41,  9, 49, 17, 57, 25]

Shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

S1 = \
[[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
[0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
[4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
[15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]]

S2 = \
[[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
[3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
[0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
[13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]]

S3 = \
[[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
[13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
[13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
[1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]]

S4 = \
[[7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
[13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
[10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
[3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]]

S5 = \
[[2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
[14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
[4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
[11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]]

S6 = \
[[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
[10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
[9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
[4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]]

S7 = \
[[4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
[13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
[1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
[6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]]

S8 = \
[[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
[1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
[7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
[2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]

key56bits = []
key48bits = []
Input = []
IPvalues = []
Left = []
Right = []
EXPvalues = []
XORvalues = []
Xvalues = []
X2values = []
Rvalues = []
Cyphervalues = []
Output = []


def initial():
    for j in range(0, 56):
        key56bits.append(0)
    for j in range(0, 17):
        key48bits.append([])
        for i in range(0, 48):
            key48bits[j].append(0)
    for j in range(0, 64):
        IPvalues.append(0)
        Output.append(0)
        Cyphervalues.append(0)
    for j in range(0, 17):
        Left.append([])
        Right.append([])
        for i in range(0, 32):
            Left[j].append(0)
            Right[j].append(0)
    for j in range(0, 48):
        EXPvalues.append(0)
        XORvalues.append(0)
    for j in range(0, 8):
        Xvalues.append([])
        for i in range(0, 6):
            Xvalues[j].append(0)
    for j in range(0, 32):
        Rvalues.append(0)
        X2values.append(0)


def key56to48(round, position, value):
    i = 0
    for i in range(0, 48):
        if PermutedChoice2[i] == position + 1:
            break
    key48bits[round][i] = value


def key64to56(position, value):
    i = 0
    for i in range(0, 56):
        if PermutedChoice1[i] == position + 1:
            break
    key56bits[i] = value


def key64to48(key):
    C = [[]]
    D = [[]]
    CD = []
    backup = []
    for i in range(0, 64):
        key64to56(i, key[i])
    for i in range(0, 56):
        if i < 28:
            C[0].append(key56bits[i])
        else:
            D[0].append(key56bits[i])
    for n in range(1, 17):
        shift = Shifts[n - 1]
        backup.append([])
        C.append([])
        D.append([])
        for i in range(0, shift):
            backup[n-1].append(C[n-1][i])
        for i in range(0, 28-shift):
            C[n].append(C[n-1][i+shift])
        k = 0
        for i in range(28-shift, 28):
            C[n].append(backup[n-1][k])
            k = k + 1
        for i in range(0, shift):
            backup[n-1][i] = D[n-1][i]
        for i in range(0, 28-shift):
            D[n].append(D[n-1][i+shift])
        k = 0
        for i in range(28-shift, 28):
            D[n].append(backup[n-1][k])
            k = k + 1
    for n in range(0, 17):
        CD.append([])
        for i in range(0, 28):
            CD[n].append(C[n][i])
        for i in range(28, 56):
            CD[n].append(D[n][i-28])
    for n in range(1, 17):
        for i in range(0, 56):
            key56to48(n, i, CD[n][i])


def create16keys():
    temp = 2984365175632145
    key = []
    mask = 0x8000000000000000
    for i in range(0, 64):
        if mask & temp > 0:
            key.append(1)
        else:
            key.append(0)
        mask = mask >> 1
    key64to48(key)


def read(text_to_encrypt):
    temp = bytes(text_to_encrypt, "utf-8")
    temp = list(temp)
    if len(temp) % 8 != 0:
        for i in range(0, 8 - len(temp) % 8):
            temp.append(0)
    for i in range(0, len(temp)):
        mask = 0x80
        for j in range(0, 8):
            if mask & temp[i] > 0:
                Input.append(1)
            else:
                Input.append(0)
            mask = mask >> 1


def IP_function(position, value):
    i = 0
    for i in range(0, 64):
        if InitialPermutation[i] == position + 1:
            break
    IPvalues[i] = value


def EXP_function(position, value):
    for i in range(0, 48):
        if Expansion[i] == position + 1:
            EXPvalues[i] = value


def F1_function(i):
    b = []
    for j in range(0, 6):
        b.append(Xvalues[i][j])
    r = b[0] * 2 + b[5]
    c = 8 * b[1] + 4 * b[2] + 2 * b[3] + b[4]
    if i == 0:
        return S1[r][c]
    elif i == 1:
        return S2[r][c]
    elif i == 2:
        return S3[r][c]
    elif i == 3:
        return S4[r][c]
    elif i == 4:
        return S5[r][c]
    elif i == 5:
        return S6[r][c]
    elif i == 6:
        return S7[r][c]
    elif i == 7:
        return S8[r][c]


def Sbox():
    k = 0
    for i in range(0, 8):
        for j in range(0, 6):
            Xvalues[i][j] = XORvalues[k]
            k = k + 1
    k = 0
    for i in range(0, 8):
        temp = F1_function(i)
        mask = 0x8
        for j in range(0, 4):
            if mask & temp > 0:
                X2values[k] = 1
            else:
                X2values[k] = 0
            mask = mask >> 1
            k = k + 1

def Pbox(position, value):
    i = 0
    for i in range(0, 32):
        if Permutation[i] == position + 1:
            break
    Rvalues[i] = value


def cypher(round, mode):
    for i in range(0, 32):
        EXP_function(i, Right[round-1][i])
    for i in range(0, 48):
        if mode == 0:
            XORvalues[i] = EXPvalues[i] ^ key48bits[round][i]
        else:
            XORvalues[i] = EXPvalues[i] ^ key48bits[17 - round][i]
    Sbox()
    for i in range(0, 32):
        Pbox(i, X2values[i])
    for i in range(0, 32):
        Right[round][i] = Left[round-1][i] ^ Rvalues[i]


def FP_function(position, value):
    i = 0
    for i in range(0, 64):
        if FinalPermutation[i] == position + 1:
            break
    Output[i] = value


def encryption(tab):
    file = open("passwd.txt", "ab")
    for i in range(0, 64):
        IP_function(i, tab[i])
    for i in range(0, 32):
        Left[0][i] = IPvalues[i]
    for i in range(32, 64):
        Right[0][i-32] = IPvalues[i]
    for j in range(1, 17):
        cypher(j, 0)
        for i in range(0, 32):
            Left[j][i] = Right[j-1][i]
    for i in range(0, 64):
        if i < 32:
            Cyphervalues[i] = Right[16][i]
        else:
            Cyphervalues[i] = Left[16][i-32]
        FP_function(i, Cyphervalues[i])
    temp = []
    for i in range(0, 8):
        val = 0
        for j in range(0, 8):
            if Output[i * 8 + j] == 1:
                val = val + 2 ** (7 - j)
        temp.append(val)
    temp = bytes(temp)
    file.write(temp)
    file.close()


def decryption(tab):
    for i in range(0, 64):
        IP_function(i, tab[i])
    for i in range(0, 32):
        Left[0][i] = IPvalues[i]
    for i in range(32, 64):
        Right[0][i-32] = IPvalues[i]
    for j in range(1, 17):
        cypher(j, 1)
        for i in range(0, 32):
            Left[j][i] = Right[j-1][i]
    for i in range(0, 64):
        if i < 32:
            Cyphervalues[i] = Right[16][i]
        else:
            Cyphervalues[i] = Left[16][i-32]
        FP_function(i, Cyphervalues[i])
    temp = []
    for i in range(0, 8):
        val = 0
        for j in range(0, 8):
            if Output[i * 8 + j] == 1:
                val = val + 2 ** (7 - j)
        if val != 0:
            temp.append(val)
    temp = bytes(temp)
    temp = temp.decode("utf-8")
    return temp


def encrypt(text_to_encrypt):
    read(text_to_encrypt)
    temp = []
    file = open("passwd.txt", "w")
    file.close()
    for i in range(0, 64):
        temp.append(Input[i])
    for i in range(0, int(len(Input)/64)):
        for j in range(0, 64):
            temp[j] = Input[i*64 + j]
        encryption(temp)


def decrypt():
    file = open("passwd.txt", "rb")
    temp = file.read()
    file.close()
    output = ""
    for i in range(0, int(len(temp)/8)):
        tab = []
        for j in range(0, 8):
            mask = 0x80
            for n in range(0, 8):
                if temp[j + i*8] & mask > 0:
                    tab.append(1)
                else:
                    tab.append(0)
                mask = mask >> 1
        output = output + decryption(tab)
    return output
