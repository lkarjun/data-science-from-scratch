# Neural Network

    y = w1x1  + w2x2 + wnxn + bias
    z = Activation(y)
    
    * Activation 
   
        sigmoid
             
            y = sigma i=1 to n wixi + bias
            Activation (1/1+e^-y)
            
        ReLu ( Rectified Linear Unit)
        
            max(y, o)
        
        
        Leaky Relu
           
            max(0.01z, z)
        
        
        Tanh
        
        
        softmax
            
            * for multiclass classification problem we use softmax
        
        
        Threshold Activation
        
        
        softplus
         
        
        swish
         
        
        Elu
         
        
        PRelu
     
     * Rectified Linear Unit
     
        -> Relu will solve Vanishing gradient problem.
        
      
         
     
     * Derivatives 
     
         sigmoid  -->   g(z)  =   1/1+e^-z)
                         
                        g(z)*(1-g(z))
                     
         
         tanh    -->    g(z)  = 1-(tan(z))^2
         
         
         relu    -->    g'(z)  = 0 if z < 0
                                 1 if z > 0
     
     
     * Pros and cons of Activation functions
             
             sigmoid  --> only use when output is a binary classification.
             
             Tanh     --> pretty much strictly superior
             
             Relu     --> when output like house price predicition Relu is best option.
     
     
     
     * Hidden Layers
         
         The fact that in the training set the true values for nodes in the middle are not observed.
         that is, we don't see what they should be in the training set.
         
      
     