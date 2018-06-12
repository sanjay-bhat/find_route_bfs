README
======

find-route calculates optimal distance between two vertices by also taking into accont thier weights. In this case the vertices are cities and weights are distances between them and we use BSF in an attempt to find shortest route between any 2 given cities provided a path exists.

Files included
--------------
1. romania.py - Contains the details on converting the text containing vertices and their respective distances into graph.
2. find_route.py - Find the optimal path between destination 1 and destination 2, i.e: source and destination, using BSF
3. input1.txt - File containing vertices and their respective distances

Steps to run the code
---------------------
1. Place the files [1], [2] and [3] in desired directory and change permissions of all the 3 files from existing (0644) permissions to -rwxrwxrwx, i.e: 0777.
2. Open terminal.
3. Traverse to the directory where the files are held using 'cd'.
4. Invoke the code using the following command, '[san @ubuntu]$ python find_route.py input1.txt Berlin Munich' and hit enter to find the BFS shortest path between Berlin and Munich.
5. Change input1.txt file and cities following it as per need.
