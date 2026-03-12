import numpy as np
M= 1000 

tableau=np.array([
    [-5,-4,0,0,M,0],
    [6,4,-1,0,1,24],
    [1,2,0,1,0,6]
],dtype=float)

iteration=1 

tableau[0] = tableau[0] - M * tableau[1]
while True:
    print("\n iteration",iteration)
    print(tableau)

    z_row=tableau[0, :-1]

    if np.all(z_row>=0):
        print("\n optimal solution reached ")
        break

    pivot_col=np.argmin(z_row)
    print("entering variable : column ",pivot_col)

    ratios =[]
    for i in range(1,len(tableau)):
        if tableau[i,pivot_col]>0:
            ratios.append(tableau[i,-1]/tableau[i,pivot_col])
        else:
            ratios.append(np.inf)

    if all(r == np.inf for r in ratios):
        print("Problem is Unbounded")
        break

    pivot_row = np.argmin(ratios) + 1
    print("leaving variale : row ",pivot_row)

    pivot_element=tableau[pivot_row,pivot_col]
    print("pivot element :",pivot_element)

    tableau[pivot_row, :]=tableau[pivot_row,:]/pivot_element

    for i in range(len(tableau)):
        if i !=pivot_row:
            factor=tableau[i,pivot_col]
            tableau[i,:]=tableau[i,:]-factor * tableau[pivot_row,:]

    iteration +=1

print("\n final tableau:")
print(tableau)

#extract solution 
rows=tableau.shape[0]

x1=x2=0

for i in range(1, rows):
     if tableau[i][0]==1:
         x1=tableau[i][-1]
     if tableau[i][1] == 1:
         x2=tableau[i][-1]

print("\n optimal solution :")
print("x1=",x1)
print("x2=",x2)
print("maximum z=",tableau[0][-1])
