## Deep Learning.
#### MY Notes
    --> The difference between cost function and loss function is that the loss funciton computes the error for a single training example; the cost function is the average of the loss function of the entire training set.
    
    # Symmetry problem
        * If the gradients are equal then weights are going to be updated by the same amount.
          The weights attached to the same neuron, continue to remain the same throughout the
          trianing. Its makes the hidden units symmetric and this problem is know as the 
          Symmetry Problem.
          
        * To break this we should initialize different random weights to the same neurons.
        
        * Never initailize weights to large values, same value for all nodes, zeros.
        
        * Initialization of weights from Uniform, standard normal distribution, Xavier inintailization.
        
    # Vanishing and exploding Gradient
    
        * If the derivatives are large then the gradient increases exponentially. --> Exploding Gradient
        * If the derivatives are small then the gradient decreases exponentially. --> Vanishing Gradient
                
                Learning rate is a small parameter.. Ranges from 0.1 to 10^-5, If gradient is very small, lets say 10^-6
                Then during gradient descent, the new weights will be
                
                    W_new = W_old - learning_rate * grad
                    
                Learning rate times gradient will be 10^-10 which is very tiny
                So W_new will be approximately equal to W_old itself. So after one epoch, we can see that there's no change
                in weights Which means that the model will still be as wrong as when we started training 
                So even after multiple epochs, you'll have nearly the same weights as you have started with
                In effect, because of extremely small gradients, our neural network has stopped learning.
                This is called the vanishing gradient problem
        
    # Drop out neuron
    
        * Neural network are prone to overfiting to their TRAINING DATA. To tackle this we randomly turn off neurons ( that is replace its output with 0 ) with some fixed probability.
        * Drop out ratio 0 < p < 1 
        * In test data all the neurons will connected.. all neuron are connected.
        * To choose best p value we need to do that hyper parameter optimization.
    
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
    
