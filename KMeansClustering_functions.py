#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

glucose, hemoglobin, classification = openckdfile()

def normalizeData(glucose,hemoglobin,classification):
    hemoglobin= (hemoglobin-3.1)/(17.8-3.1)
    hemoglobin_scaled = hemoglobin
    glucose= (glucose - 70)/(490-70)
    glucose_scaled = glucose
    return glucose_scaled, hemoglobin_scaled

glucose_scaled, hemoglobin_scaled =normalizeData(glucose,hemoglobin,classification)

def select(K):
    return np.random.random((K, 2))

def assign(centroids, hemoglobin_scaled, glucose_scaled):
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = centroids[i,1]
        h = centroids[i,0]
        distances[i] = np.sqrt((hemoglobin_scaled-h)**2+(glucose_scaled-g)**2) 
    assignments = np.argmin(distances, axis = 0)  
    return assignments


def update(assignments,k, hemoglobin_scaled,glucose_scaled):
    new_centroids = np.zeros((k,2))
    for i in range(k):
        allhemocluster = hemoglobin_scaled[assignments == i]
        new_centroids[i,0] = np.mean(allhemocluster)
        allglucosecluster = glucose_scaled[assignments == i]
        new_centroids[i,1] = np.mean(allglucosecluster)
    return new_centroids

def iteration(k, new_centroids,centroids):
    while True:
        assignments = assign(centroids, hemoglobin_scaled, glucose_scaled)  
        new_centroids = update(assignments,k, hemoglobin_scaled,glucose_scaled)
        if np.array_equal(centroids, new_centroids):
            break
        centroids = new_centroids 
    return centroids
    
    
    
    
    
    
    
    
    