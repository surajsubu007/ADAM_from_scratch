""" This module gives the 2d and 3d plots of the surface function"""
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from adam_problem_statement import surface_function



def plot_surface_3d(figureNumber, rangeExtent,outputPath, savePlot):
	""" This function gives the 3D surface plot of the function."""
	xMin = rangeExtent[0]
	xMax = rangeExtent[1]
	yMin = rangeExtent[2]
	yMax = rangeExtent[3]
	instanceValue = 50
	xMeshRange = np.linspace(xMin, xMax, instanceValue)
	yMeshRange = np.linspace(yMin, yMax, instanceValue)
	xMesh, yMesh = np.meshgrid(xMeshRange, yMeshRange)  # generate the grid
	surfaceFunction = surface_function(xMesh, yMesh)

	# plotting the surface
	surfacePlot = plt.figure(figureNumber)
	axes = Axes3D(surfacePlot)
	axes.plot_surface(xMesh, yMesh, surfaceFunction, rstride=1, cstride=1, cmap="viridis")
	if savePlot is True:
		plt.savefig(os.path.join(outputPath,'surface_3d'))



def plot_surface_2d(figureNumber, rangeExtent,outputPath, savePlot):
	""" This function gives the 2D projection of the surface plot """
	xMin = rangeExtent[0]
	xMax = rangeExtent[1]
	yMin = rangeExtent[2]
	yMax = rangeExtent[3]
	instanceValue = 50
	xMeshRange = np.linspace(xMin, xMax, instanceValue)
	yMeshRange = np.linspace(yMin, yMax, instanceValue)
	xGrid, yGrid = np.meshgrid(xMeshRange, yMeshRange)
	plt.figure(figureNumber)
	plt.imshow(surface_function(xGrid, yGrid), extent=[xMin, xMax, yMin, yMax], origin="lower")
	plt.colorbar()
	if savePlot is True:
		plt.savefig(os.path.join(outputPath,'surface_2d'))

