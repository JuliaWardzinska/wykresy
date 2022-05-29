import numpy as np
#
# a= np.array([1, 2, 3])
# print(a)
#
# b= np.arange(1, 4, 10, dtype='float64')
# print(b)
# print(type(b))
# print(b.dtype)
# print(b.shape)  #rozmiar tablicy
# print(b.ndim) # ilu wymiarowa jest tablica
#
# c = np.array([[0,1], [2,4]])
# print(c)
# print(c.shape)
# print(c.ndim)


# zera = np.zeros((5, 5))
# print(zera)
#
# pusta= np.empty((2,2))
# print(pusta)
# pusta[1][1] =2
# print(pusta)
# b= np.linspace(1, 2, 5 , endpoint=False)
# print(b)

# c =np.indices((5,5))
# print(c)
#
# print(c[0][1][1])
#
# e, f = np.mgrid[0:3,0:3]
# print(e)
# print(f)

# g= np.diag([x for x in range(5)], k= -1)
# print(g)
#
# h= np.fromiter(range(5), dtype='int32')
# print(h)

marcin = b'Marcin'
# mar = np.frombuffer(marcin, dtype='S3') #dzeilniki .
# print(mar)

# mar_1 = np.array(list(marcin) , dtype='S1')
# print(mar_1)

# mar_2 = np.array(list(b'Marcin'))
# print(mar_2)
#
# a = np.ones((2, 2))
# b = np.ones((2, 2))
#
# c = a + b
# print(c)


# a= np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s= range(2, 7, 2)
# print(a[2:7:2])
#
# print(a[1:])
# print(a[2:5])

# a= np.arange(25) #tablica składająca się z 25 el.
# print(a)
#
# mat= a.reshape((5, 5))
# print(mat)
# print(mat[1:2]) # - tylko drugi wiersz chcemy z tej macierzy
# print(mat[:, 1:2]) # chcemy drugą kolumnę , pierwszy przecienk jest dla wierszy
# print(mat[2:5, 1:3])  # z macierzy 5na5 wycinamy i otrzymujemy 3na2
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(x)
#
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0,2]])
# y = x[rows, cols]
# print(y)import numpy as np
#
# a= np.array([1, 2, 3])
# print(a)
#
# b= np.arange(1, 4, 10, dtype='float64')
# print(b)
# print(type(b))
# print(b.dtype)
# print(b.shape)  #rozmiar tablicy
# print(b.ndim) # ilu wymiarowa jest tablica
#
# c = np.array([[0,1], [2,4]])
# print(c)
# print(c.shape)
# print(c.ndim)


# zera = np.zeros((5, 5))
# print(zera)
#
# pusta= np.empty((2,2))
# print(pusta)
# pusta[1][1] =2
# print(pusta)
# b= np.linspace(1, 2, 5 , endpoint=False)
# print(b)

# c =np.indices((5,5))
# print(c)
#
# print(c[0][1][1])
#
# e, f = np.mgrid[0:3,0:3]
# print(e)
# print(f)

# g= np.diag([x for x in range(5)], k= -1)
# print(g)
#
# h= np.fromiter(range(5), dtype='int32')
# print(h)

marcin = b'Marcin'
# mar = np.frombuffer(marcin, dtype='S3') #dzeilniki .
# print(mar)

# mar_1 = np.array(list(marcin) , dtype='S1')
# print(mar_1)

# mar_2 = np.array(list(b'Marcin'))
# print(mar_2)
#
# a = np.ones((2, 2))
# b = np.ones((2, 2))
#
# c = a + b
# print(c)


# a= np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s= range(2, 7, 2)
# print(a[2:7:2])
#
# print(a[1:])
# print(a[2:5])

# a= np.arange(25) #tablica składająca się z 25 el.
# print(a)
#
# mat= a.reshape((5, 5))
# print(mat)
# print(mat[1:2]) # - tylko drugi wiersz chcemy z tej macierzy
# print(mat[:, 1:2]) # chcemy drugą kolumnę , pierwszy przecienk jest dla wierszy
# print(mat[2:5, 1:3])  # z macierzy 5na5 wycinamy i otrzymujemy 3na2
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(x)

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0,2]])
y = x[rows, cols]
print(y)