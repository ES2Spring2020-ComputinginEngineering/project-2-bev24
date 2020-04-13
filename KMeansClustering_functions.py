#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

glucose, hemoglobin, classification = openckdfile()

def select(K):
    return np.random.random((K, 2))

def assign(centroids, hemoglobin, glucose):
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = centroids[i,1]
        h = centroids[i,0]
        distances[i] = np.sqrt((hemoglobin-h)**2+(glucose-g)**2) 
    assignments = np.argmin(distances, axis = 0)  
    return assignments

def update(assignments):
    newassignments = np.mean(assignments)
    return newassignments

def iteration(assignments, newassignments):
    while newassignments != assignments:
        assign(centroids, hemoglobin, glucose)
        update(assignments)
    if newassignments == assignments:
        return newassignments
        
centroids = select(10)
assignments = assign(centroids, hemoglobin, glucose)
assign(centroids, hemoglobin, glucose)

K = 2
select(K)

    
    
    
    
    
    
    
    
    