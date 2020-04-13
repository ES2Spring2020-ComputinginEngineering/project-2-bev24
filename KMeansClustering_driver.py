#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions

centroids = select(10)
assignments = assign(centroids, hemoglobin, glucose)

newassignments = update(assignments)


K = 2
select(K)


    
def graphingKMeans(glucose, hemoglobin, assignments, centroids):
    plt.figure()
    for i in range(assignments.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignments==i],glucose[assignments==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()   
graphingKMeans(glucose, hemoglobin, assignments, centroids)
    