""" This module takes in the surface to be minimized and finds the point of minimum. """
import os
import json
import re
import sys
from adam_optimizer import adam
from surface_animation import plot_2d_animation
from path_2d_plot import output_plot_2d
from surface_plot import plot_surface_3d, plot_surface_2d


delimiters = r"\\", "/", "\\", "//"
regexPattern = '|'.join(map(re.escape, delimiters))
opArg = re.split(regexPattern, sys.argv[1])
opDict = {}
opDir = ""
opCount = 0
for e in opArg:
    opCount += 1
    opDict["key{}".format(opCount)] = e
    if e == opArg[-1]:
        opDir = opDir + opDict["key{}".format(opCount)]
    else:
        opDir = opDir + opDict["key{}".format(opCount)] + os.path.sep

opDir = os.path.abspath(opDir)

# inputParameters = "C:/Users/Suraj/PycharmProjects/dev/inputs/adam_implementation/adam_optimization_inputs.json"
# if os.path.exists(opDir):
with open(opDir, 'r') as f:
	json_obj = json.load(f)
learningRate = json_obj['learningRate']
xInitial = json_obj['xInitial']
yInitial = json_obj['yInitial']
precisionValue = json_obj['precision']
xMin = json_obj['xMinimumRange']
yMin = json_obj['yMinimumRange']
xMax = json_obj['xMaximumRange']
yMax = json_obj['yMaximumRange']
outputPath = json_obj["outputPath"]

rangeExtent = [xMin, xMax, yMin, yMax]

# creating the 3D surface
plot_surface_3d(1, rangeExtent, outputPath, True)

# plotting the 2D projection
plot_surface_2d(2, rangeExtent, outputPath, True)

# implementing adam optimization to find the minimum
xMinimumPoint, yMinimumPoint, xList, yList, zList = adam(xInitial, yInitial, precisionValue, learningRate)
outputParameters = [xMinimumPoint, yMinimumPoint, xList, yList, zList]
print('x_min:', xMinimumPoint, 'y_min:', yMinimumPoint)

# Show the function in 2D

output_plot_2d(3, rangeExtent, outputParameters, outputPath, True)


# Animation

plot_2d_animation(4, rangeExtent, outputParameters, outputPath, True)
