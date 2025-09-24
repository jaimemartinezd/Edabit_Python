# Print a downward half-pyramid pattern of stars

for i in range(5,0,-1):
    for x in range(i,0,-1):
        print('*', end=' ')
    print('\n')