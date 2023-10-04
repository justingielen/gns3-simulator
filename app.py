#!/usr/bin/env python
# coding: utf-8

# In[18]:


# importing packages
import random
import numpy as np

# function for randomly placing a Node on the network
def placement(matrix,w):
    placed = False
    while placed == False:
        y = random.randint(0,w-1)
        x = random.randint(0,w-1)
        if matrix[y][x] != "N":
            matrix[y][x] = "N"
            placed = True
    return y, x

# function for getting user input for the width of their network
def get_width():
    w = input("Welcome to the GNS3 Simulator!\nWe will generate a hypothetical network based on your specifications. \n\n" +
              "Please enter the width 'w' of your network (between 2-13, result will be a 'w' x 'w' grid):\n")
    return w

# function for getting user input for the number of nodes in their network
def get_nodes():
    n = input("\nPlease enter the number of nodes 'N' in your network (ensure that N is less than w, they will be randomly placed and connected with electrons):\n")
    return n

# function to populate the rest of the initial grid - those spaces not filled with a Node - with blank space
def fill_grid(matrix,w):
    for y in range(0,w):
        for x in range(0,w):
            if matrix[y][x] != "N":
                matrix[y][x] = " "
                
# Function for generating a matrix
def simulate():
    # Getting user inputs for network sizes (width and number of nodes) - checking for only valid inputs
    width_chosen = False
    while not width_chosen:
        w = get_width()
        try:
            int(w)
        except:
            print("Please type an integer.")
        else:
            for i in range(2,14):
                if int(w) == i:
                    width_chosen = True
                    break
            if width_chosen == False:
                print("Please choose a number between 2 and 13.")
    nodes_chosen = False
    while not nodes_chosen:
        n = get_nodes()
        try:
            int(n)
        except:
            print("Please type a number.")
        else: 
            for i in range(1,int(w)):
                if int(n) == i:
                    nodes_chosen = True
                    break
            if nodes_chosen == False:
                print("Please choose a number less than the size of your network.")


    # Turning user inputs into integers
    w = int(w)
    n = int(n)

    # Creating initial, unconnected grid with user inputs & populating list of node placements to be used for making connections
    matrix = np.empty((w,w), dtype=str)
    positions = []
    for i in range(0,n):
        y, x = placement(matrix,w)
        positions.append([y,x])

    fill_grid(matrix,w)

    # Making connections between Nodes (N)'s with electrons (e)'s
    for i in range(0,len(positions)):
        try:
            # vertical electron path toward next index
            if positions[i][0] > positions[i+1][0]:
                for y in range(positions[i+1][0],positions[i][0]):
                    x = positions[i][1]
                    if matrix[y][x] != "N":
                        matrix[y][x] = "e"
            elif positions[i][0] < positions[i+1][0]:
                for y in range(positions[i][0],positions[i+1][0] + 1):
                    x = positions[i][1]
                    if matrix[y][x] != "N":
                        matrix[y][x] = "e"

            # horizontal electron path toward next index
            if positions[i][1] > positions[i+1][1]:
                for x in range(positions[i+1][1],positions[i][1] + 1):
                    y = positions[i+1][0]
                    if matrix[y][x] != "N":
                        matrix[y][x] = "e"
            elif positions[i][1] < positions[i+1][1]:
                for x in range(positions[i][1],positions[i+1][1]):
                    y = positions[i+1][0]
                    if matrix[y][x] != "N":
                        matrix[y][x] = "e"

        except:
            dub = 3
    print("\nGreat! Here is your hypothetical network:\n")
    print(matrix)
    
    end = False
    while not end:
        another = input("\nWould you like to create another one? (Y/N)")
        if another == "Y":
            print("\n")
            end = True
            simulate()
        elif another == "N":
            print("Sounds good. Thanks for trying out our application!")
            end = True
        else:
            print("Please type either Y or N.")

simulate()


# In[ ]:




