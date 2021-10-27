
# Implementation of ADAM optimization




### Table of Contents


- [Description](#description)
- [How To Use](#how-to-use)
- [Pylint score](#Pylint-score)

---

## Description



Adam is an optimization algorithm that can be used instead of the classical stochastic gradient descent procedure to update network weights iterative based in training data.

Adam was presented by Diederik Kingma from OpenAI and Jimmy Ba from the University of Toronto in their 2015 ICLR paper (poster) titled “Adam: A Method for Stochastic Optimization“. I will quote liberally from their paper in this post, unless stated otherwise.

The algorithm is called Adam. It is not an acronym and is not written as “ADAM”.


[Back To The Top](#read-me-template)

---

## How To Use

### Run the surface_minimization code

The programe consists of Six parts, viz, surface_minimization, adam_problem_statement, adam_optimizer, surface_plot, surface_animation, path_2d_plot .

The main program, which is surface_minimization imports functions from the other five.

* The paths to the output file needs to be specified in the adam_input.json file in the IP/inputs/adam_implementation folder
  * note: the paths in the json file needs to be with "/"
* Run " surface_minimization.py " file by specifying the path to the adam_inputs.json file
* sample code to run the file : pyhton surface_minimization.py <path to adam_inputs.json file>\adam_inputs.json
* The inputs for the minimization parameters are given by the " adam_optimization_inputs.json" file, which is the inputs folder of dev, they can be changed according to the requirment.
* In order to save outputs of "plot_surface_3d", "plot_surface_2d", "output_plot_2d" and "plot_2d_animation" functions to your device, change the last attribute of the required functions as True. The first attribute of all these functions specifies the figure number of the plot.
* As the program is in process, the output of each called function will be displayed in via a popup window. Close the window to proceed with the next funciton output of the code.

### Pylint score


(base) C:\Users\Suraj\PycharmProjects\dev\src\adam_implementation>pylint --rcfile configFile.pylintrc surface_plot.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.26/10, +0.74)


(base) C:\Users\Suraj\PycharmProjects\dev\src\adam_implementation>pylint --rcfile configFile.pylintrc path_2d_plot.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.38/10, +0.62)


(base) C:\Users\Suraj\PycharmProjects\dev\src\adam_implementation>pylint --rcfile configFile.pylintrc surface_animation.py
************* Module surface_animation
surface_animation.py:31:0: R1707: Disallow trailing comma tuple (trailing-comma-tuple)

------------------------------------------------------------------
Your code has been rated at 9.69/10 (previous run: 9.23/10, +0.46)


(base) C:\Users\Suraj\PycharmProjects\dev\src\adam_implementation>pylint --rcfile configFile.pylintrc adam_problem_statement.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


(base) C:\Users\Suraj\PycharmProjects\dev\src\adam_implementation>pylint --rcfile configFile.pylintrc adam_optimizer.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


(base) C:\Users\Suraj\PycharmProjects\dev\src\adam_implementation>pylint --rcfile configFile.pylintrc surface_minimization.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


[Back To The Top](#read-me-template)