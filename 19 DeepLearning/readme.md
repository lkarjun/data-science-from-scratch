## Deep Learning.
    
    --> The difference between cost function and loss function is that the loss funciton computes the error for a single training example; the cost function is the average of the loss function of the entire training set.
    
    # Symmetry problem
        * If the gradients are equal then weights are going to be updated by the same amount.
          The weights attached to the same neuron, continue to remain the same throughout the
          trianing. Its makes the hidden units symmetric and this problem is know as the 
          Symmetry Problem.
          
        * To break this we should initialize different random weights to the same neurons.
        
        * Never initailize weights to large values, same value for all nodes, zeros.
        
        * Initialization of weights from Uniform, standard normal distribution, Xavier inintailization.
        
      
    # The Neuron
    
        * inputs ===> Neuron ===> Output signal
            output values may be continous, binary, categorical.
             * if it's a categorical variable the important thing to remember here is that, in that case, the ouput value won't be just one, it'll be seversl output values, because these will be your dummy variables, which will be representing your categories.
            
         
         * weights are crucial to ai neural networks working.
           weights are how neural networks learn. by adjusting the weights, the neural network decides in every single case, what signal is importants and what signals are not to certain neurons.
            
    * Deep Learing uses more more Hidden Neurons
 
    * Updating weights with optimizers through backpropogation.
    * finding best learning rate by hyper parameter tuninig
    
    
        
        
        
    # Vanishing Gradient 
    
        * Derivative of sigmoide will be specifically between 0 to 0.25
    