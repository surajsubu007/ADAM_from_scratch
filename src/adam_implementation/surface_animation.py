""" This module is used for the purpose of animation of output plot."""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from adam_problem_statement import surface_function

def plot_2d_animation(figureNumber, rangeExtent, outputParameters,outputPath, saveAnimation):
	""" Animates the Output plot. """
	xMin = rangeExtent[0]
	xMax = rangeExtent[1]
	yMin = rangeExtent[2]
	yMax = rangeExtent[3]
	xList = outputParameters[2]
	yList = outputParameters[3]
	instanceValue = 50
	xMeshRange = np.linspace(xMin, xMax, instanceValue)
	yMeshRange = np.linspace(yMin, yMax, instanceValue)
	xGrid, yGrid = np.meshgrid(xMeshRange, yMeshRange)
	baseFigure = plt.figure(figureNumber)
	plt.axis()
	plt.imshow(surface_function(xGrid, yGrid), extent=[xMin, xMax, yMin, yMax], origin="lower")
	plt.colorbar()
	xCurve = []
	yCurve = []


	def _animate(i):
		xCurve.append(xList[i])
		yCurve.append(yList[i])
		pointerLocation = plt.scatter(xCurve, yCurve, c="w")
		return pointerLocation,


	surfaceAnimate = animation.FuncAnimation(baseFigure, _animate, frames=len(xList), blit=True, repeat=False)

	if saveAnimation is True:
		writerName = animation.writers['ffmpeg']
		writerType = writerName(fps=2, metadata=dict(artist='Me'), bitrate=1800)
		surfaceAnimate.save(os.path.join(outputPath,'Adam_output_animation.mp4'), writer=writerType)
