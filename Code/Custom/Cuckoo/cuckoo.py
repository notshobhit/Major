import random
import math
from math import pi, sin, cos, exp
from levy_distribution import levy_walk


num_nests = 15
step_size = 1   #alpha
Pa = 0.25   # probability of throwing away eggs
num_params = 2

lower = [0]*num_params
upper = [5]*num_params

def objective_function(params):
	# l = 0
	# for x in params:
	# 	l += x*x
	# return l

	x, y = params
	m = 10
	t1 = sin(x*x/pi)**(2*m)
	t1 *= -sin(x)
	t2 = sin(2*y*y/pi)**(2*m)
	t2 *= -sin(y)

	return t1 + t2

	# x, y = params
	# t1 = -cos(x)*cos(y)*exp(-1*(x-pi)**2 - (y-pi)**2)
	# return t1

def generate_new_egg(num_params):
	params = []
	for j in xrange(num_params):
		params.append(random.uniform(0, 1)*(upper[j] - lower[j]) + lower[j])
	return (params, objective_function(params))

def sort_nests(nests):
	nests.sort(key=lambda tup: tup[1]) # sort with min value of objective function first

def params_permissible(params):
	for i in xrange(num_params):
		if params[i] < lower[i] and params[i] > upper[i]: return False
	return True

nests = []

for i in xrange(num_nests):
	nests.append(generate_new_egg(num_params))

sort_nests(nests)
print "Initial nest values: ", nests


max_iterations = 100000
best_nest = 0

Pc = int((1-Pa)*num_nests)
print Pc

for it in xrange(max_iterations):
	new_egg = nests[random.randint(0, Pc)]

	new_egg_params = levy_walk(new_egg[0], step_size)
	while not params_permissible(new_egg_params):
		new_egg_params = levy_walk(new_egg[0], step_size)

	new_egg = (new_egg_params, objective_function(new_egg_params))
	
	j = random.randint(0, num_nests-1)
	existing_egg = nests[j]

	if(new_egg[1] < existing_egg[1]):
		nests[j] = new_egg
	sort_nests(nests)

	bad_nest_start = int(num_nests - (num_nests*Pa))
	for ex in xrange(bad_nest_start, num_nests):
		nests[ex] = generate_new_egg(num_params)
	sort_nests(nests)

print "Best nest value: ", nests[0]