#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
# Import necessary modules

import matplotlib
matplotlib.use('TkAgg')
import pylab as PL
import matplotlib.pyplot as plt 

import networkx as nx
import random

# Define model parameters
def initialize():

    # List global variables: network, the next network (the network of the next step) and node position
    global g, nextg, pos 
    
    # Create Karate club graph
    g=nx.karate_club_graph()
    
    # Pre-alculate node positions
    pos=nx.spring_layout(g)
    print("Node Position")
    
    # Assign 0 or 1 randomly to the nodes’ state attribute
    for n in g.nodes(data=True):
        n[1]['state']=random.choice([0,1])
    
    for n in g.nodes(data=True):
        print(n[1]['state'])
    
    # Create a duplicate copy of the network 
    nextg=g.copy()
    
    
def draw():

    # Visualization
    color_map = []
    labels={1,2,3}
    for n in  g.nodes(data=True):
        if  n[1]['state']== 0:
            color_map.append('red')
        else: color_map.append('green')  
    
    # Draw the network    
    nx.draw(g,pos,node_color = color_map,with_labels=True)
    
    
def update():
    
    # List global variables
    global state1, g, nextg
    state1=[]
    
    # Loop on the network nodes.
    for n in g.nodes(data=True):
        if n[1]['state']== 1:
            state1.append(n[0])
    print(state1)
    
    # Loop on the neighbors of each node
    for n in g.nodes:
        x=set(g.neighbors(n))
        print("Neighbors of", n)
        print(x)
        print("Number of local neighbors of", n)
        print(len(x))
        
        print("Neighbors with state 1 of", n)
        count=0
        for y in x:
            for z in state1:
                if y == z:
                    count=count+1
                    print(y)
                    
        print("State of", n, "is:", g.nodes[1]['state'])
        
        print("Number of neighbors with state 1 of", n)
        if(g.nodes[1]['state'])==1:
            
            print(count+1)
        else:
            print(count)
        
        # Calculate a state ratio to indicate an aggregated state of the local neighborhood
        print("State ratio of", n)
        state_ratio=(count+1)/len(x)
        print(state_ratio)
        
        # Update the states of the network nodes following a threshold of 0.5
        if state_ratio>0.5:
            
            nextg.nodes[1]['state']=1
            print("Updated state of",n, "is:", nextg.nodes[1]['state'])
        elif state_ratio<0.5:
            
            nextg.nodes[1]['state']=0
            print("Updated state of",n, "is:", nextg.nodes[1]['state'])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        elif state_ratio==0.5:
            
            nextg.nodes[1]['state']=random.choice([0,1])
            print("Updated state of",n, "is:", nextg.nodes[1]['state'])
         
        g=nextg.copy()


# Update system states for one discrete time step
import pycxsimulator
pycxsimulator.GUI().start(func=[initialize,draw,update])
