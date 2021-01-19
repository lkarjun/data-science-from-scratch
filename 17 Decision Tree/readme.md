# Decision Tree

    * Entropy test 

	## It will take a bit more time as compared to Gini impurtity test
        id3 algorithm -> To select one feature as root.

        Entropy helps to measures the purity of split.

        -p(+) log2(p+) - p(-) log2(p-)
        p(+) / p(-) = % of +ve class / % of -ve class.
        
        entropy value always between 0 and 1

    * Information Gain 
	
	Gain(S, A) = h(s) - sigma v E val |Sv| h(sv)
					  ----
					   |S|
	If structure gives Highest infromation gain value. Then we can choose that structure for our decision tree.
        make sure that from top to till the end. it will go and compute what the very good or total entropy value.

    * Gini Impurity test
	
	## GINI Impurity is computionally efficient. This takes short period of execution.
        ## CALCULATE FOR EACH FEATURES INDEPENDENTLY and find least value
        ## Helps in feature selection.

        left leaf ==  1 - (Probability of "YES")^2 - (Probability of "NO")^2

        right leaf ==  1 - (Probability of "YES")^2 - (Probability of "NO")^2

        =>  Total Gini impurity
                = weighted average of gini impurities for both right and left nodes
        
	=> then look for lowest gini impurity value
		= then makes that as the root node
