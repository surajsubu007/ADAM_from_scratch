""" Takes in values for ADAM optimization and the optimized values."""
import numpy as np
from adam_problem_statement import surface_function, x_gradient_z, y_gradient_z


def adam(xInitial, yInitial, precisionValue, learningRate):
	""" This funtion is used for optimization. """
	# create empty lists where the updated values of x and y will be appended during each iteration
	xList, yList, zList = [xInitial], [yInitial], [surface_function(xInitial, yInitial)]

	# initialize the gradient descent with the momentum and the rmsprop values
	momentXgradient = 0
	rmsXgradient = 0
	momentYgradient = 0
	rmsYgradient = 0
	betaOne = 0.9
	betaTwo = 0.999
	epsilonValue = 1e-8

	iteratorCount = 0
	xPrevious = 0
	yPrevious = 0

	while abs(xInitial - xPrevious) > precisionValue and abs(yInitial - yPrevious) > precisionValue:
		iteratorCount += 1

		# for x

		# change the value of x
		xPrevious = xInitial

		# get the derivative of the old value of function with the old value of x
		xGradient = x_gradient_z(xPrevious)

		# momentum gradient descent
		momentXgradient = betaOne * momentXgradient + (1 - betaOne) * xGradient

		# rms prop value of the derivative using beta 2
		rmsXgradient = betaTwo * rmsXgradient + (1 - betaTwo) * (xGradient ** 2)

		# bias correction values
		momentXupdate = momentXgradient / (1 - (betaOne ** 2))
		rmsXupdate = rmsXgradient / (1 - (betaTwo ** 2))

		# updating the value of x_new
		xInitial = xPrevious - (learningRate / (np.sqrt(rmsXupdate) + epsilonValue)) * momentXupdate

		# for y
		# change the value of y
		yPrevious = yInitial

		# get the derivative of the old value of function with the old value of y
		yGradient = y_gradient_z(yPrevious)

		# momentum gradient descent
		momentYgradient = betaOne * momentYgradient + (1 - betaOne) * yGradient

		# rms prop value of the derivative using beta 2
		rmsYgradient = betaTwo * rmsYgradient + (1 - betaTwo) * (yGradient ** 2)

		# bias correction values
		momentYupdate = momentYgradient / (1 - (betaOne ** 2))
		rmsYupdate = rmsYgradient / (1 - (betaTwo ** 2))

		# updating the value of x_new
		yInitial = yPrevious - (learningRate / (np.sqrt(rmsYupdate) + epsilonValue)) * momentYupdate

		xList.append(xInitial)
		yList.append(yInitial)

		zList.append(surface_function(xInitial, yInitial))

	return xInitial, yInitial, xList, yList, zList
