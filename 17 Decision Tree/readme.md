# Decision Tree

    * Entropy test 

        id3 algorithm -> To select one feature as root.

        Entropy helps to measures the purity of split.

        -p(+) log2(p+) - p(-) log2(p-)
        p(+) / p(-) = % of +ve class / % of -ve class.
        
    * Information Gain 

        make sure that from top to till the end. it will go and compute what the very good or total entropy value.

    * Gini Impurity test

        ## CALCULATE FOR EACH FEATURES INDEPENDENTLY and find least value
        ## Helps in feature selection.

        left leaf ==  1 - (Probability of "YES")^2 - (Probability of "NO")^2

        right leaf ==  1 - (Probability of "YES")^2 - (Probability of "NO")^2

        =>  Total Gini impurity
                = weighted average of gini impurities for both right and left nodes
        
