import numpy as np

def Sobel(I):
    H1 = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    
    H2 = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])
    H = [H1, H2]
    result = [x*0 for x in range(0, 25)]
    for h in range(len(H)):
        mid = H[h][1][1]
        right = H[h][1][2]
        left = H[h][1][0]
        up = H[h][0][1]
        down = H[h][2][1]
        r_up = H[h][0][2]
        r_down = H[h][2][2]
        l_up = H[h][0][0]
        l_down = H[h][2][0]
        G = []
        for r in range(0, 5):
            for c in range(0, 5):
                if(r == 0 and c == 0): # góc trái trên
                    i = I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                      i)
                elif(r == 4 and c == 0): # góc trái dưới
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                      i)
                elif(r == 0 and c == 4): # góc phải trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                elif(r == 4 and c == 4): #góc phải dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid}= ',
                          i)
                elif(r == 0 and c > 0 and c < 4): # cạnh trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r == 4 and c > 0 and c < 4): # cạnh dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                          i)
                elif(r > 0 and r < 4 and c == 0): # cạnh trái
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r > 0 and r < 4 and c == 4): # cạnh phải
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                else: # bên trong
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r-up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} +{I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}+ {I[r+1][c+1]}*{r_down}= ',
                          i)
                G.append(i)
        print(f'G{h+1} = ', G)
        for i in range(len(result)):
            if(G[i] > 0):
                result[i] += G[i]
            else:
                result[i] += (-G[i])
    print('G = ', result)

def Prewitt(I):
    H1 = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])
    
    H2 = np.array([[-1, -1, -1],
                   [0, 0, 0],
                   [1, 1, 1]])
    H = [H1, H2]
    result = [x*0 for x in range(0, 25)]
    for h in range(len(H)):
        mid = H[h][1][1]
        right = H[h][1][2]
        left = H[h][1][0]
        up = H[h][0][1]
        down = H[h][2][1]
        r_up = H[h][0][2]
        r_down = H[h][2][2]
        l_up = H[h][0][0]
        l_down = H[h][2][0]
        G = []
        for r in range(0, 5):
            for c in range(0, 5):
                if(r == 0 and c == 0): # góc trái trên
                    i = I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                      i)
                elif(r == 4 and c == 0): # góc trái dưới
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                      i)
                elif(r == 0 and c == 4): # góc phải trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                elif(r == 4 and c == 4): #góc phải dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid}= ',
                          i)
                elif(r == 0 and c > 0 and c < 4): # cạnh trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r == 4 and c > 0 and c < 4): # cạnh dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                          i)
                elif(r > 0 and r < 4 and c == 0): # cạnh trái
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r > 0 and r < 4 and c == 4): # cạnh phải
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                else: # bên trong
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r-up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} +{I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}+ {I[r+1][c+1]}*{r_down}= ',
                          i)
                G.append(i)
        print(f'G{h+1} = ', G)
        for i in range(len(result)):
            if(G[i] > 0):
                result[i] += G[i]
            else:
                result[i] += (-G[i])
    print('G = ', result)


def Kirsh(I):
    H1 = np.array([[-3, -3, -3],
                   [-3, 0, 5],
                   [-3, 5, 5]])
    
    H2 = np.array([[-3, -3, -3],
                   [-3, 0, -3],
                   [5, 5, 5]])
    
    H3 = np.array([[-3, -3, -3],
                   [5, 0, -3],
                   [5, 5, -3]])
    
    H4 = np.array([[5, -3, -3],
                   [5, 0, -3],
                   [5, -3, -3]])
    
    H5 = np.array([[5, 5, -3],
                   [5, 0, -3],
                   [-3, -3, -3]])
    
    H6 = np.array([[5, 5 ,5],
                   [-3, 0, -3],
                   [-3, -3, -3]])
    
    H7 = np.array([[-3, 5, 5],
                   [-3, 0, 5],
                   [-3, -3, -3]])
    
    H8 = np.array([[-3, -3, 5],
                   [-3, 0, 5],
                   [-3, -3, 5]])
    G_max = [x*0 for x in range(25)]
    H = [H1, H2, H3, H4, H5, H6, H7, H8]
    for h in range(len(H)):
        mid = H[h][1][1]
        right = H[h][1][2]
        left = H[h][1][0]
        up = H[h][0][1]
        down = H[h][2][1]
        r_up = H[h][0][2]
        r_down = H[h][2][2]
        l_up = H[h][0][0]
        l_down = H[h][2][0]
        G = []
        tong = 0
        for r in range(0, 5):
            for c in range(0, 5):
                if(r == 0 and c == 0): # góc trái trên
                    i = I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                      i)
                elif(r == 4 and c == 0): # góc trái dưới
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                      i)
                elif(r == 0 and c == 4): # góc phải trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                elif(r == 4 and c == 4): #góc phải dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid}= ',
                          i)
                elif(r == 0 and c > 0 and c < 4): # cạnh trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r == 4 and c > 0 and c < 4): # cạnh dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                          i)
                elif(r > 0 and r < 4 and c == 0): # cạnh trái
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r > 0 and r < 4 and c == 4): # cạnh phải
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                else: # bên trong
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r-up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} +{I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}+ {I[r+1][c+1]}*{r_down}= ',
                          i)
                G.append(i)
        print(f'G{h+1} = ', G)
        for i in range(len(G)):
            if(G[i] > 0):
                if(G_max[i] < G[i]):
                    G_max[i] = G[i]
            else:
                a = -G[i]
                if(G_max[i] < a):
                    G_max[i] = a
    print('G_max =', G_max)
def Laplace(I):
    print('Nhập ma trận mặt nạ, enter để nhập thêm dòng!')
    r1 = input()
    r2 = input()
    r3 = input()
    l1 = r1.split()
    for x in range(len(l1)):
        l1[x] = int(l1[x])
    l2 = r2.split()
    for x in range(len(l2)):
        l2[x] = int(l2[x])
    l3 = r3.split()
    for x in range(len(l3)):
        l3[x] = int(l3[x])
    arr = np.array([l1, l2, l3])
    H = [arr]
    print(H)
    for h in range(len(H)):
        mid = H[h][1][1]
        right = H[h][1][2]
        left = H[h][1][0]
        up = H[h][0][1]
        down = H[h][2][1]
        r_up = H[h][0][2]
        r_down = H[h][2][2]
        l_up = H[h][0][0]
        l_down = H[h][2][0]
        G = []
        for r in range(0, 5):
            for c in range(0, 5):
                if(r == 0 and c == 0): # góc trái trên
                    i = I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                      i)
                elif(r == 4 and c == 0): # góc trái dưới
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                      i)
                elif(r == 0 and c == 4): # góc phải trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                elif(r == 4 and c == 4): #góc phải dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid}= ',
                          i)
                elif(r == 0 and c > 0 and c < 4): # cạnh trên
                    i = I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r == 4 and c > 0 and c < 4): # cạnh dưới
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r][c+1]}*{right}= ',
                          i)
                elif(r > 0 and r < 4 and c == 0): # cạnh trái
                    i = I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c]*mid + I[r][c+1]*right + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r_up} + {I[r][c]}*{mid} + {I[r][c+1]}*{right} + {I[r+1][c]}*{down} + {I[r+1][c+1]}*{r_down}= ',
                          i)
                elif(r > 0 and r < 4 and c == 4): # cạnh phải
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r][c-1]*left + I[r][c]*mid + I[r+1][c-1]*l_down + I[r+1][c]*down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}= ',
                          i)
                else: # bên trong
                    i = I[r-1][c-1]*l_up + I[r-1][c]*up + I[r-1][c+1]*r_up + I[r][c-1]*left + I[r][c]*mid + I[r][c+1]*right + I[r+1][c-1]*l_down + I[r+1][c]*down + I[r+1][c+1]*r_down
                    print(f'I({r},{c})= {I[r-1][c-1]}*{l_up} + {I[r-1][c]}*{up} + {I[r-1][c+1]}*{r-up} + {I[r][c-1]}*{left} + {I[r][c]}*{mid} +{I[r][c+1]}*{right} + {I[r+1][c-1]}*{l_down} + {I[r+1][c]}*{down}+ {I[r+1][c+1]}*{r_down}= ',
                          i)
                G.append(i)
        print(f'G{h+1} = ', G)
A = np.array([[4, 5, 3, 5, 1],
              [3, 5, 3, 6, 2],
              [4, 6, 7, 6, 7],
              [3, 3, 6, 7, 3],
              [2, 2, 3, 5, 5]])
#Sobel(A)
#Prewitt(A)
#Kirsh(A)
#Laplace(A)
