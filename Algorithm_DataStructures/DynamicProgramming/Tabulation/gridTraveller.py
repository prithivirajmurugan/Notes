def gridTraveler(m,n):
    table = [[0 for x in range(n+1)]for y in range(m+1)]
    table[1][1] = 1
    print(table[0][2])
    for i in range(0,m+1):
        for j in range(0,n+1):
            current_element = table[i][j]
            if(i+1<=m):
                table[i+1][j]+= current_element
            if(j+1<=n):
                table[i][j+1]+= current_element
    return table[m][n]

"""Tabulation recipe
Visualize the problem as a table
size the table based on the inputs
initialize the table with default values
seed the trivial answer into the table
iterate through the table
fill further position based on the current position

"""





print(gridTraveler(3,2))