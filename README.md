This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Nearest Neighbor Classification file contains:
1.normalizeData = scales the data from 0 to 10 which gets rid of errors involving units
2.graphdata = graphs a scatter plot of the new scaled data
3.createTestCase = creates a random new point to classify
4.calculateDistanceArray = takes the distance between the new point and all of the scaled data
5.NegihborClassifier= finds the index of the closest point to the new point and classifies the new point based on the closest point.
6.graphTestCase= graphs the new point and shows its classification

Knearestnumber file contains:
kNearestNeighborClassifier = takes the distance between the new point and the other data points, compares it to k amount of closest data points to determine its classification

Kmeanscluster file contains:
1.select(K)= Creates k amounts of random points to become centroids
the function returns a point 
2.assign(centroids, hemoglobin, glucose)= Assigns the original data points to the centroids that it is closer to

3.update(assignments)= finds the mean of the points within each group of centroids and makes it the new centroid
4.iteration(assignments, newassignments)= repeats the steps until the new centroid and previous centroid values are the same.

All information required to use python code:

1.For knearestnumber, assign an odd number the variable K, the other data points near the new test case will help to determine its classification.
The number must be odd so there will never be a tie between two data points.
2.For Kmeanscluster, k is how many centroids are going to be in the graph. Assign a number to k.


k means clustering algorithm: 

1. pick 3 ks to be your centroids
2. assign values to the closest by using the Euclidean distance
3. find new centroids by taking avgerage of all points and making it the centroid
4. 