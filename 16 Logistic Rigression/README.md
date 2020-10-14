# Naive Bayes 
    * Assumtion
        - conditional independence of feature

# K-Nearest neighbors
    * Assumtion
        - neighbourhood of a point is same as a point

# Logistic Regression

    argMax E i = 1 to n Sigmoid(yiwTxi)

    ### Assumtion
        -> Almost linearly separable
    
    ### Goodness
        minimum len(misclassified) must be low  OR
        maximum len(classified) must be high

        i,e yi*wTxi  >  0

        Find optimal w*....?

        argMax E i=1 to n (yiwTxi)
    
        **change / vary (w) 
        _________________________

    ### yi E { -1 , +1}
    ### distance of a point 
        * di = w^Txi + b / ||w||; w is normal to plane, if ||w|| is unit vector
          then di = w^T xi + b
        
        * if wTxi > 0 then:
           yi = +1
        
        * if wTxi < 0 then:
           yi = -1
    
    ### Decision surface in Logistic Regression is Line / plane

    ###  CASE I
        yi * wT * xi > 0 => correctly classifiying points
        if yi = +1 -> +ve point
            wTxi > 0  => classifier is saying its a +ve point
    ### CASE II
        yi * wT * xi > 0
        if yi = -1 -> -ve point
            wTxi < 0     => -ve * -ve == +ve
    ***
        For both +ve and -ve points 
            yi wT xi > 0  => The Logistic is correctly classifiying the points
    
    ### CASE III
        yi*wTxi < 0
        if yi = +1 (+ve point)
            wTxi < 0  => xi is -ve class

        '''True class point is +1 and classified as -v 
            misclassified'''
        
    ### CASE IV
        yi*wTxi > 0
        if yi = -1 ==> -ve
            wTxi > 0  => xi is +ve point
        
        '''misclassified True point is -1 and classified as +v'''