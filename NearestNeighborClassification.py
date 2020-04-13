#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random
import math

# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

#normalizing data


def normalizeData(glucose,hemoglobin,classification):
    hemoglobin= (hemoglobin-3.1)/(17.8-3.1)
    hemoglobin_scaled = hemoglobin
    glucose= (glucose - 70)/(490-70)
    glucose_scaled = glucose
    return glucose_scaled, hemoglobin_scaled
    
normalizeData(glucose,hemoglobin,classification)
glucose_scaled, hemoglobin_scaled = normalizeData(glucose,hemoglobin,classification)


def graphdata(glucose_scaled, hemoglobin_scaled, classification):
    plt.figure()
    plt.title('scaled graph')
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
    plt.legend()
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.show()


def createTestCase():
    newhemoglobin= np.random.rand(1)
    newglucose= np.random.rand(1)
    return newhemoglobin, newglucose

createTestCase()
newhemoglobin, newglucose = createTestCase()

def calculateDistanceArray(newglucose,newhemoglobin,glucose,hemoglobin):
    distance = np.zeros(len(hemoglobin))
    for i in range(len(hemoglobin)):
        distance[i] =math.sqrt((newhemoglobin-hemoglobin_scaled[i])**(2)+(newglucose-glucose_scaled[i])**(2))
    return distance

distance = calculateDistanceArray(newglucose,newhemoglobin,glucose,hemoglobin)
    
def NegihborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distancearray= calculateDistanceArray(newglucose,newhemoglobin,glucose,hemoglobin)
    min_index = distancearray.min
    min_index = np.argmin(distancearray)
    nearest_class = classification[min_index]
    return nearest_class

nearest_class = NegihborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin,classification,nearest_class):
    plt.figure()
    plt.title('scaled graph with test case')
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
    if nearest_class == 1:
        plt.plot(newhemoglobin, newglucose, "k.", markersize =15, label= "Test Case")
    if nearest_class == 0:
        plt.plot(newhemoglobin, newglucose, "r.", markersize =15, label= "Test Case")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin,classification,nearest_class)   

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose,hemoglobin,classification):
    distancearray= calculateDistanceArray(newglucose,newhemoglobin,glucose,hemoglobin)
    sorted_indices = np.argsort(distancearray)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    median = np.median(k_classifications)
    return median

k = 3 
kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose,hemoglobin,classification)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    