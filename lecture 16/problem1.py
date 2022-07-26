def bubble_sort(L, func):
     for i in range ( len(L) - 1):
         for j in range(len(L) - 1 - i):  
             i1 = (len(L)-1) - (j + 1) 
             i2 = (len(L)-1) -  j  
             if func(L[i1], L[i2]):
                 if L[i1] > L[i2]:
                     L[i1], L[i2] = L[i2], L[i1]
     return L
def cmp_numbers(x1, x2):
     return x1 > x2
l=[ ]
L= ['Chris Terman','Tom Brady','Eric Grimson','Joseph Shin','Changbum Choi']
for i in L:
    x,y=i.split()
    l.append((y,x))
l.sort()
for i in l:
    print i[1]+" "+i[0]+' , ',
