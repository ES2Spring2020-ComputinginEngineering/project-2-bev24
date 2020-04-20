#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import matplotlib.pyplot as plt
import numpy as np
k=2
glucose, hemoglobin, classification = kmc.openckdfile()

glucose_scaled, hemoglobin_scaled = kmc.normalizeData(glucose,hemoglobin,classification)

centroids = kmc.select(k) 
assignments = kmc.assign(centroids, hemoglobin_scaled, glucose_scaled)

centroids = kmc.update(assignments,k, hemoglobin_scaled,glucose_scaled)


def graphingKMeans(glucose_scaled, hemoglobin_scaled, assignments, centroids):
    plt.figure()
    for i in range(assignments.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin_scaled[assignments==i],glucose_scaled[assignments==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()   
graphingKMeans(glucose_scaled, hemoglobin_scaled, assignments, centroids)
