# Quint---Esolang
Python interpreter and specs for Quint, a 2Dimensional Cell-Based Esoteric Language.

  Hello! I am proud to present Quint, my minimal esoteric language. Quint is a simple esolang. Before you choose to play around and experiment, it is best to understand the structure of Quint. 
Quint consists of a 2D array of cells, 300 by 300 (can easily be increased, so don't worry about size constraints just yet), and a pointer that starts at (0,0). Each cell starts at 0, and goes up
to 255, after which it wraps around back to 0. To change a cells value, the pointer must be located at the selected cell, before two main operations can be applied: addition or subtraction. Whenever 
the prompt to print out the number at a cell is given, all the cells within the column are added up and the total is printed. Quint, although simple, is Turing Complete, which means that with enough 
time and resources, Quint can compute anything, albiet the actual coding would be a nightmare. Below are shown the keys that are used in Quint, everything else is ignored. 


Keys:
1 - Move Pointer Right
2 - Move Pointer Left
3 - Move Pointer Up
4 - Move Pointer Down
5 - Add 1 To The Cell The Selected Cell
6 - Subtract 1 To The Selected Cell
7 - The Start Of A While Loop (Only runs if the cell the selected cells value isn't 0)
8 - The End Of A While Loop
9 - Prints Out The Sum Of All The Digits In The Column At The Selected Cell
0 - Prints Out The ASCII Character That Corresponds To The Value In The Selected Cell
? - Get User Input Of An Integer
