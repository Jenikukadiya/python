import numpy as np
tableau = np.array[
    [-5,-4,0,0,0,0,0],
    [6,4,1,0,0,0,24],
    [1,2,0,1,0,0,6],
    [-1,1,0,0,1,0,1],
    [0,1,0,0,0,1,2]
]


iteration = 1

while True :
    print("\n iteration ", iteration)
    print(tableau)

    z_row = tableau[0,:-1]
    if np.all(z_row>=0):
        print("\noptimal solution reached .")
        break
    pivot_col=np.argmin(z_row)
    print("entering vriable : column ",pivot_col)

    ratios=[]
    for i in range(1,len(tableau)):
        if tableau[i,pivot_col]>0:
            ratios.append(tableau[i,-1]/tableau[i,pivot_col])
        else:
            ratios.append(np.inf)

    pivot_row=np.argmin(ratios)+1
    print("leaving variable : row ",pivot_row)

    pivot_element = tableau[pivot_row,pivot_col]
    print("pivot element ",pivot_element)

    tableau[pivot_row,:]=tableau[pivot_row,:]/pivot_element

    for i in range(len(tableau)):
        if i !=pivot_row:
            factor=tableau[i,pivot_col]
            tableau[i,:]=tableau[i,:]-factor*tableau[pivot_row,:]

iteration +=1

print("\nfinal tableau")
print(tableau)


rows = tableau.shape[0]

x1 = x2 = 0

for i in range(1, rows):   # start from 1 to skip Z-row
    if tableau[i][0] == 1:
        x1 = tableau[i][-1]
    if tableau[i][1] == 1:
        x2 = tableau[i][-1]

print("\nOptimal Solution:")
print("x1 =", x1)
print("x2 =", x2)
print("Maximum Z =", tableau[0][-1])








