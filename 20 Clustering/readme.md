## Notes

Kmeans Clustering specifically tries to put the data into the number of cluster you tell it to.

Metrics used in Kmeans

    Eucliden distance is: 

        root of (x2 - x1)^2 + (y2 - y1)^2

    Manhatted metrics.

Input: K, set of points x1...xn
Placing Centroids c1...ck at random locations.
Repeat until Convergence:
    for each point x:
        * find nearest centroide cj   argmin D(x, c)
        * assign the point xi to cluster j

    for each cluster j = 1 ... K:
        * new centroid cj = mean of all points xi,
          assigned to cluster j in previos step.

    
1 Randomly choos k data points (seeds) to be the inital centroids.
2 Assign each data point to the closest centroid
3 Re-compute (update) the centroids using the current cluster memberships
4 if a convergence criterion is not met, go to step 2.

