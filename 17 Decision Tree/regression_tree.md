# Regression Tree

    * Squared Residual
        fixing a threshold resulted in better predictions over all;
    
    * Restrict lots of splits.
        lots of splits leads to (low biaas and high variance)
      
 ## Prune Regression Tree
     
    * cost complexity pruning
         calculate the sum of Squared Residuals for each tree.
     
    * Weakest Link Pruning
    
         Works by calculating a Tree score and a tree complexity penalty(no of leafs or terminal nodes in tree or sub-tree)
          
               Tree Score = sum of squared residual + alpha*T
               
               ** alpha tuning parameter that finds when using crossvalidation.
               
               
       -> choose tree structure which gives tree score = small.