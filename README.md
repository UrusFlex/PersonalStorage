# Wave Pathfinding Algorithm

This code implements a pathfinding solution using the wave propagation algorithm (also known as Lee algorithm) to find the shortest path between two points in a grid. 

The grid is represented as a matrix of 0s and 1s, where 0 indicates a traversable cell and 1 represents an obstacle. The program reads this matrix from an Excel file named "Playing field.xlsx" using the openpyxl library.

The algorithm starts by prompting the user to input the starting and ending coordinates (converted to zero-based indices). It then initializes a wave matrix to track distances from the start point and uses a queue to systematically propagate through all reachable cells, moving in four possible directions (up, down, left, right). Each valid adjacent cell is marked with an incremented distance value until the end point is reached.

Once the end point is found, the program reconstructs the shortest path by backtracking from the destination to the start point, following the decreasing values in the wave matrix. Finally, it outputs the path length (number of steps) and the sequence of coordinates representing the shortest path. 
