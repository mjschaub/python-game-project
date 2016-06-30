
maze = ([1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,0],
        [1,0,0,0,1],
        [1,0,1,0,1])
for row in range(5):
    for col, value in enumerate(maze[row]):
        #for col, value in row:
        #   print col, value
        print "coord: ", [row,col], "value: ", value
