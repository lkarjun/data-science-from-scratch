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
        
        softplus
        
        Threshold Activation
        
     
     
     * Pros and cons of Activation functions
             
             sigmoid  --> only use when output is a binary classification.
             
             Tanh     --> pretty much strictly superio
             
             Relu     --> 
     
     
     
     * Hidden Layers
         
         The fact that in the training set the true values for nodes in the middle are not observed.
         that is, we don't see what they should be in the training set.
         
      
     