
# Ship Problem




## The Problem

The repo contains the surface mesh of the underwater hull of a ship. Mesh does not include any panels above the water level. The picture of the mesh is attached too. The mesh is composed of quadrilateral panels (but some could be triangles when two vertices of a panel coincide). The fourth line of the mesh file has the number of panels that make up the underwater hull. From the fifth line onwards, the x, y and z coordinates of the points in a panel are listed. Each consecutive set of 4 lines list the coordinates of the vertices of one panel. The  coordinates are given with respect to a frame of reference with origin at the water level. Note that the x-axis of the frame of reference points towards the front of the ship, y-axis points to the port side (towards the left side of a person standing at the origin and facing the front of the ship) and the z-axis points vertically up. Note that this is why all the vertices will have negative or zero z coordinates.

![Ship_image](https://github.com/satyvm/Python_ship_problem/blob/main/Underwater_Ship.png?raw=true)

Write a program to read in the mesh from the geometry file (extension .GDF) and calculate (a) the underwater surface area and (b) the waterplane area of the ship. You must write your code in Python and all of your code must be in a single file. Make sure that your code executes without error. Do not change the name of the geometry file. Your final code should read a geometry file named  "Underwater_Ship.GDF". Provide ample comments for me to understand your code. Try using numpy arrays rather than python lists for achieving the objective.

## The Solution

"solution.py" in the repo is the solution to the problem.