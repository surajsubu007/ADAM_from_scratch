""" This module has the function which plots the output in 2d"""
import os
import numpy as np
import matplotlib.pyplot as plt
from adam_problem_statement import surface_function

def output_plot_2d(figureNumber, rangeExtent, outputParameters,outputPath, savePlot):
	""" This function returns the 2D plot of the output."""
	xMin = rangeExtent[0]
	xMax = rangeExtent[1]
	yMin = rangeExtent[2]
	yMax = rangeExtent[3]
	xMinimumPoint = outputParameters[0]
	yMinimumPoint = outputParameters[1]
	xList = outputParameters[2]
	yList = outputParameters[3]

	instanceValue = 50
	xMeshRange = np.linspace(xMin, xMax, instanceValue)
	yMeshRange = np.linspace(yMin, yMax, instanceValue)
	xGrid, yGrid = np.meshgrid(xMeshRange, yMeshRange)
	plt.figure(figureNumber)
	plt.imshow(surface_function(xGrid, yGrid), extent=[xMin, xMax, yMin, yMax], origin="lower")
	plt.colorbar()

	# plotting the path
	plt.scatter(xList, yList, c="w")
	plt.scatter(xMinimumPoint, yMinimumPoint, c='r')
	if savePlot is True:
		plt.savefig(os.path.join(outputPath,'output_path.png'))
