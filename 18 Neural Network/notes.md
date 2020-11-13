# Neural Network

    y = w1x1  + w2x2 + wnxn + bias
    z = Activation(y)
    
    * Activation 
   
        sigmoid
             
            y = sigma i=1 to n wixi + bias
            Activation (1/1+e^-y)
            
        ReLu ( Rectified Linear Unit)
        
            max(y, o)
            
        softplus
        
        Threshold Activation
        
     
     
     * Hidden Layers
         
         The fact that in the training set the true values for nodes in the middle are not observed.
         that is, we don't see what they should be in the training set.