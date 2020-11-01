# Regression Tree

    * Squared Residual
        fixing a threshold resulted in better predictions over all;
    
    * Restrict lots of splits.
        lots of splits leads to (low biaas and high variance)
      
 ## Prune Regression Tree
     
     ### Removing leafs...
     
    * cost complexity pruning
         calculate the sum of Squared Residuals for each leaf.
     
    * Weakest Link Pruning
    
         Works by calculating a Tree score and a tree complexity penalty(no of leafs or terminal nodes in tree or sub-tree)
          
               Tree Score = sum of squared residual + alpha*T
               
               ** T is number of leafs.
               ** alpha tuning parameter that finds when using crossvalidation.
               
               
         -> choose tree structure which gives tree score = small.