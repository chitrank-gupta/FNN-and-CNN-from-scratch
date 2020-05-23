import nn
import numpy as np
import sys

from util import *
from visualize import *
from layers import *


# XTrain - List of training input Data
# YTrain - Corresponding list of training data labels
# XVal - List of validation input Data
# YVal - Corresponding list of validation data labels
# XTest - List of testing input Data
# YTest - Corresponding list of testing data labels

def taskSquare(draw):
	XTrain, YTrain, XVal, YVal, XTest, YTest = readSquare()
	# Create a NeuralNetwork object 'nn1' as follows with optimal parameters. For parameter definition, refer to nn.py file.
	# nn1 = nn.NeuralNetwork(out_nodes, alpha, batchSize, epochs)	
	# Add layers to neural network corresponding to inputs and outputs of given data
	# Eg. nn1.addLayer(FullyConnectedLayer(x,y))
	###############################################
	# TASK 2.1 - YOUR CODE HERE
	nn1=nn.NeuralNetwork(2,0.001,100,30)
	nn1.addLayer(FullyConnectedLayer(2,4,"relu"))
	# nn1.addLayer(FullyConnectedLayer(2,2,"relu"))
	# nn1.addLayer(FullyConnectedLayer(2,2,"relu"))
	nn1.addLayer(FullyConnectedLayer(4,2,"softmax"))

	# raise NotImplementedError
	###############################################
	nn1.train(XTrain, YTrain, XVal, YVal, 0, 1)
	pred, acc = nn1.validate(XTest, YTest)
	print('Test Accuracy ',acc)
	# Run script visualizeTruth.py to visualize ground truth. Run command 'python3 visualizeTruth.py 2'
	# Use drawSquare(XTest, pred) to visualize YOUR predictions.
	if draw:
		drawSquare(XTest, pred)
	return nn1, XTest, YTest


def taskSemiCircle(draw):
	XTrain, YTrain, XVal, YVal, XTest, YTest = readSemiCircle()
	# Create a NeuralNetwork object 'nn1' as follows with optimal parameters. For parameter definition, refer to nn.py file.
	# nn1 = nn.NeuralNetwork(out_nodes, alpha, batchSize, epochs)	
	# Add layers to neural network corresponding to inputs and outputs of given data
	# Eg. nn1.addLayer(FullyConnectedLayer(x,y))
	###############################################
	# TASK 2.2 - YOUR CODE HERE
	# raise NotImplementedError
	nn1=nn.NeuralNetwork(2,0.001,100,30)
	nn1.addLayer(FullyConnectedLayer(2,2,"relu"))
	# nn1.addLayer(FullyConnectedLayer(2,2,"relu"))
	# nn1.addLayer(FullyConnectedLayer(2,2,"relu"))
	nn1.addLayer(FullyConnectedLayer(2,2,"softmax"))
	# print("hello")

	###############################################
	nn1.train(XTrain, YTrain, XVal, YVal, False, True)
	pred, acc  = nn1.validate(XTest, YTest)
	print('Test Accuracy ',acc)
	# Run script visualizeTruth.py to visualize ground truth. Run command 'python3 visualizeTruth.py 4'
	# Use drawSemiCircle(XTest, pred) to vnisualize YOUR predictions.
	if draw:
		drawSemiCircle(XTest, pred)
	return nn1, XTest, YTest

def taskMnist():
	XTrain, YTrain, XVal, YVal, XTest, YTest = readMNIST()
	# Create a NeuralNetwork object 'nn1' as follows with optimal parameters. For parameter definition, refer to nn.py file.
	# nn1 = nn.NeuralNetwork(out_nodes, alpha, batchSize, epochs)	
	# Add layers to neural network corresponding to inputs and outputs of given data
	# Eg. nn1.addLayer(FullyConnectedLayer(x,y))
	###############################################
	# TASK 2.3 - YOUR CODE HERE
	# raise NotImplementedError
	nn1=nn.NeuralNetwork(10,0.001,100,10)
	# nn1.addLayer(FullyConnectedLayer(784,5,"relu"))
	# nn1.addLayer(FullyConnectedLayer(2,2,"relu"))
	# nn1.addLayer(FullyConnectedLayer(2,2,"relu"))
	nn1.addLayer(FullyConnectedLayer(784,10,"softmax"))
	
	###############################################
	nn1.train(XTrain, YTrain, XVal, YVal, False, True)
	pred, acc  = nn1.validate(XTest, YTest)
	print('Test Accuracy ',acc)
	return nn1, XTest, YTest

def taskCifar10():	
	XTrain, YTrain, XVal, YVal, XTest, YTest = readCIFAR10()
	f=1000
	XTrain = XTrain[0:5*f,:,:,:]
	XVal = XVal[0:f,:,:,:]
	XTest = XTest[0:f,:,:,:]
	YVal = YVal[0:f,:]
	YTest = YTest[0:f,:]
	YTrain = YTrain[0:5*f,:]
	
	modelName = 'model.npy'
	# # Create a NeuralNetwork object 'nn1' as follows with optimal parameters. For parameter definition, refer to nn.py file.
	# # nn1 = nn.NeuralNetwork(out_nodes, alpha, batchSize, epochs)	
	# # Add layers to neural network corresponding to inputs and outputs of given data
	# # Eg. nn1.addLayer(FullyConnectedLayer(x,y))
	# ###############################################
	# # TASK 2.4 - YOUR CODE HERE
	# raise NotImplementedError	
	nn1=nn.NeuralNetwork(10,0.001,10,33)
	nn1.addLayer(ConvolutionLayer([3,32,32],[12,12],8,4,"relu"))
	nn1.addLayer(AvgPoolingLayer([8,6,6], [2,2], 2))
	nn1.addLayer(FlattenLayer())
	# nn1.addLayer(FullyConnectedLayer(125,50,"relu"))
	nn1.addLayer(FullyConnectedLayer(72,10,"softmax"))

	###################################################
	return nn1,  XTest, YTest, modelName # UNCOMMENT THIS LINE WHILE SUBMISSION


	nn1.train(XTrain, YTrain, XVal, YVal, True, True, loadModel=0, saveModel=True, modelName=modelName)
	pred, acc = nn1.validate(XTest, YTest)
	print('Test Accuracy ',acc)