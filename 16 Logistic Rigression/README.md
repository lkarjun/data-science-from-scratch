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


# Support Vector Machine
     
     * Points in right side of a line or plane its always == positive
     * Points in left side of a line or plane its always == negative

        wt x + b = -1  -> left side
        wt x + b = 1   -> right side


     *  Optimization function

          wt x + b = -1
          wt x + b = 1
          _____________

          wt  (x1 - x2) =   2      ----> we need to maximize this value...
         ----            -------
         ||w||            ||w||

        such that { 1: wt x + b >= 1,
                   -1: wt x + b <= -1}

                   Or

                   y* wt x + b

    *SVM
        convert 1d to 2d to get support vector classifier. to find we use kernels

        ->  Kernels finds svc in higher dimensions.
        finds relationships between each pair of observation used to find svc

        kernels = ['linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’]


    *softmax or support vector classifier

        -> Allow missclassification
        -> Allow Overlapping
        -> maybe high bias but sure that low variance
        
        crossvalidation help to get best soft margin.

        helps to determine the location of a threshold

        points in the margin -> support vectors

    *maximum margin classifier
        
        Are super sensitive to Outliers in the training data.