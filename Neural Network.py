import numpy as np 

def sigmoid(x):
        #Our Activation function: f(x) = 1/ (1+e^(-x))
    return 1/ (1+ np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward (self, inputs):
        #Weight inputs, add bias, then use the activation function
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

weights = np.array([0,1])
bias = 4
n = Neuron(weights, bias)

x = np.array([2,3])
print (n.feedforward(x))


class OurNeuralNetwork:
     #Neural Network with - 2 inputs, hidden layer with 2 neurons(h1 h2), output of 1 neuron (o1) each neuron has the same weights and bias
    def __init__(self):
        weights = np.array([0,1])
        bias = 0
    
        #The Neuron Class here is from the previous section
        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)
    
    def feedforward (self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        #The inputs for o1 are the outputs from h1 and h2
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1

network = OurNeuralNetwork()
x = np.array([2,3])
print(network.feedforward(x))
