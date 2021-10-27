""" Takes inputs for the surface. """
import numpy as np


def surface_function(xValues, yValues):
	""" Reurns the function value with respect to values of x and y. """
	return (1 / 4) * xValues ** 2 + np.sin(yValues)


def x_gradient_z(xValues):
	""" Returns the gradient of the function z with respect to input x """
	return (1/2) * xValues


def y_gradient_z(yValues):
	""" Returns the gradient of the function z with respect to input y """
	return np.cos(yValues)
