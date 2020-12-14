## Notes

Kmeans Clustering specifically tries to put the data into the number of cluster you tell it to.
Example of centroid based algorithm

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


** Elbow method
     
   Repeat k = 1 to 20
   Find Wcss = sumation of i = 1 to n (ci + xi) ^2

   wcss ( With in cluster sum of square)

*** Kmeans is limited to linear cluster boundaries

![alt text](https://github.com/lkarjun/Data-Science-from-Scratch/blob/master/20%20Clustering/moon.png?raw=true)


## Hierarchical Clustering

    Mainly two type

        Alggomerative
        Divisivie

1   Make each input its own cluster of one. As long as there are multiple clusters remaining

2   find the two closest clusters and merge them.

3   Merge two points into one cluster which as min disatance

4   Repeat this process until all points in your dataset is exhausted.


## Validation Techinque

Inertia

        It is the mean squared distance between each instance and its
        closest centroid. 

Cohesion

    Measure the distance of one point in the same cluster.

Separation

    Measure of one point which is in one clusters that you measure with points in other cluster.


Silhouette clustering Validaiton.

        value ranges from [-1, 1]

        -1 clustering is wrong

         0 In different same (The distance between clusters is not significant.)

         1 Both clusters are far away

    1 = a(i) =   find out all distance with in cluster.
![alt text](https://github.com/lkarjun/Data-Science-from-Scratch/blob/master/20%20Clustering/formula1.png)

    2 = b(i) =   Consider another cluster. suppose we have 2 clusters
                 c1 and c2, the average distance between all clusters.

![alt text](https://github.com/lkarjun/Data-Science-from-Scratch/blob/master/20%20Clustering/formula2.png)

    3 = s(i) = if our clustering done properly ai << bi
               if not ai >> bi.
               if it 0 clustering is okay...

![alt text](https://github.com/lkarjun/Data-Science-from-Scratch/blob/master/20%20Clustering/formula3.png)



reference https://en.wikipedia.org/wiki/Silhouette_(clustering)#:~:text=The%20silhouette%20value%20is%20a,poorly%20matched%20to%20neighboring%20clusters