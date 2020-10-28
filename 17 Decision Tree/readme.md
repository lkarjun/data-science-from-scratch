# Decision Tree

    * Gini Impurity test

        ## CALCULATE FOR EACH FEATURES INDEPENDENTLY and find least value

        left leaf ==  1 - (Probability of "YES")^2 - (Probability of "NO")^2

        right leaf ==  1 - (Probability of "YES")^2 - (Probability of "NO")^2

        =>  Total Gini impurity
                = weighted average of gini impurities for both right and left nodes
        
