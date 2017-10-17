import random
from math import sin, cos, pi, log, pow


def levy_dist(mu):
	''' From the Harris Nature paper. '''
	# uniform distribution, in range [-0.5pi, 0.5pi]
	x = random.uniform(-0.5 * pi, 0.5 * pi)

	# y has a unit exponential distribution.
	y = -log(random.uniform(0.0, 1.0))

	a = sin( (mu - 1.0) * x ) / (pow(cos(x), (1.0 / (mu - 1.0))))
	b = pow( (cos((2.0 - mu) * x) / y), ((2.0 - mu) / (mu - 1.0)) )

	z = a * b
	return z

def levy_walk(egg_params, step_size):
	params = [i + step_size*levy_dist(3) for i in egg_params] # TODO: Clarify value of mu
	return params