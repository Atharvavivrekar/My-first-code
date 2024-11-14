# Write your code here :-)
#a = [[2, 4, 6, 8, 10], [5, 4, 3, 1, 2, ], [6, 8, 10, 7, 9,]]
#print(a)

#for record in a:
    #print(record)


#a = [[2, 4, 6, 8,],
#[5, 4, 3, 1, ],
#[6, 8, 9, 7,],
#[7, 4, 3, 9,]]

#for i in range(len(a)):
    #for j in range(len(a[i])):
        #print(a[i][j], end ="")
    #print()

#m = 4
#n = 5
#a = [[0 for x in range(n)] for x in range(m)]
#print(a)


#a = [[2, 4, 6, 7, 8], [3, 4, 2, 5, 1], [4, 8, 9, 2, 0]]
#a.append([5, 10, 15, 20, 25])
#print(a)

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[0].extend([12, 14, 16, 18])
print(a)

a[2].reverse()
print(a)




