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
    global g, nextg ,pos  
    
    # Create Karate club graph
    g=nx.karate_club_graph()
    
    # Pre-alculate node positions
    pos=nx.spring_layout(g)
    
    # Assign 0 or 1 randomly to the nodes’ state attribute
    for n in g.nodes(data=True):
        n[1]['state']=random.choice([0,1])
    
    # Create a duplicate copy of the network 
    nextg=g.copy()
    
    
def draw():
   

    #Visualisation 
    color_map = []
    for n in  g.nodes(data=True):
        if  n[1]['state']== 0:
            color_map.append('red')
        else: color_map.append('green')   
        
    # Draw the network     
    nx.draw(g,pos,node_color = color_map,with_labels=True)
   

def update():
    
    # List global variables
    # Define probabilities and graph
    global pi,pr,g
    
    # Infection probability
    pi=0.3
    # Recovery probability
    pr=0.7
    
    # Create list of the graph nodes
    li=[]
    for n in g.nodes():
        li.append(n) 
        
    # Create list of random neighbors   
    rn=[]
    random_node=random.choice(li)
    print('Random node: ', random_node, 'with state: ', g.nodes[random_node]['state'])
    p=random.uniform(0, 1)
 
    # Node is susceptible
    if g.nodes[random_node]['state']==0:
        
        for i in g.neighbors(random_node):
            rn.append(i)
        # Choose randomly one of its neighbors    
        random_neighbor=random.choice(rn)
        print('Random_neighbor: ', random_neighbor, 'with state: ', g.nodes[random_neighbor]['state'])
        # Neighbor is infected
        # Simulate the infection using pi
        if g.nodes[random_neighbor]['state']==1 and p>pi:
            g.nodes[random_node]['state']=1
    # Node is infected        
    else:
        # Simulate the recovery using pr
        if p>pr:
            g.nodes[random_node]['state']=0 
    
# update system states for one discrete time step
import pycxsimulator
pycxsimulator.GUI().start(func=[initialize,draw,update])