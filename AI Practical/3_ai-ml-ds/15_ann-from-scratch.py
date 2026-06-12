import random                         # Import random module
import numpy as np                    # Import NumPy for matrix operations
import math                           # Import math functions

def calculate_sigmoid(x, b):          # Function to apply sigmoid activation
    sig = []                          # Store sigmoid outputs
    for i in range(b):                
        sigmoid = 1/(1+math.exp(-x[i][0]))  # Calculate sigmoid value
        sig.append(sigmoid)          
    return sig                        

class NeuralNetwork:
    def three_layer(self):            

        input = [[random.random() for _ in range(3)],     
                 [random.random() for _ in range(3)],      
                 [random.random() for _ in range(3)]]      

        w1 = [[random.random() for _ in range(3)],          
              [random.random() for _ in range(3)]]
        b1 = [random.random() for _ in range(2)]            

        w2 = [[random.random() for _ in range(2)],          
              [random.random() for _ in range(2)]]
        b2 = [random.random() for _ in range(2)]            
        w3 = [random.random() for _ in range(2)]            
        b3 = [random.random()]                       

        output1 = np.dot(input, np.array(w1).T) + b1       # Calculate first layer output
        output2 = np.dot(output1, np.array(w2).T) + b2     # Calculate second layer output
        output3 = np.dot(output2, np.array(w3).T) + b3     # Calculate final output

        print(output1)                                     
        print(output2)                                     
        print(output3)                                     

        sig1 = 1/(1+math.exp(-output3[0]))                 # Apply sigmoid to output 1
        sig2 = 1/(1+math.exp(-output3[1]))                 # Apply sigmoid to output 2
        sig3 = 1/(1+math.exp(-output3[2]))                 # Apply sigmoid to output 3

        print(f'Sigmoid: {sig1, sig2, sig3}')               

class NeuralNetworkLayer:
    def initialize_weights_bias(self, neurons, inputs):   # Initialize weights and biases
        self.weights = [[random.random() for _ in range(neurons)]   # Create random weights
                        for _ in range(inputs)]
        self.bias = [random.random() for _ in range(neurons)]       # Create random biases

    def feed_forward(self, input):                        # Perform forward propagation
        self.output = np.dot(input, self.weights) + self.bias   


input_layer = NeuralNetworkLayer()        # Create input layer object
hidden_layer = NeuralNetworkLayer()       # Create hidden layer object
output_layer = NeuralNetworkLayer()       # Create output layer object

input_layer.initialize_weights_bias(6, 8)   # Initialize input layer weights and biases
hidden_layer.initialize_weights_bias(3, 6)  # Initialize hidden layer weights and biases
output_layer.initialize_weights_bias(1, 3)  # Initialize output layer weights and biases

X = [[random.random() for _ in range(8)]    # Generate sample input data
     for _ in range(3)
    ]

input_layer.feed_forward(X)                 # Pass data through input layer
hidden_layer.feed_forward(input_layer.output)  # Pass output to hidden layer
output_layer.feed_forward(hidden_layer.output) # Pass output to output layer

print(calculate_sigmoid(output_layer.output, 3))  # Display final sigmoid predictions