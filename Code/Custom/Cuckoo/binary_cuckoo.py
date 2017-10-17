import random
from math import exp
from levy_distribution import levy_dist
inf = float("inf")

number_nests = 3
Pa = 0.25 #loss param
step_size = 1 #alpha
num_iterations = 1000
dimension = 2 #num_params

def sigmoid(x):
	return 1/(1 + exp(-x))

def generate_new_nest():
	params = []
	for i in xrange(dimension):
		params.append(random.randint(0, 1))
	nest = [params, -inf]
	return nest

def sort_nests(nests):
	nests.sort(key=lambda tup: -tup[1]) # sort nest in decreasing order of accuracy

def get_accuracy(params):
	return 0.1 # TODO

best_nest = generate_new_nest()
nests = []

# create nests:
for i in xrange(number_nests):
	nests.append(generate_new_nest())

# iterations:
for it in xrange(num_iterations):
	for nest in nests:
		# create Z1', Z2' from Z1, Z2
		# train using Z1'
		# evaluate using Z2', get accuracy in acc
		acc = get_accuracy(nest[0])
		if acc > nest[1]:
			nest[1] = acc
			# for i in xrange(dimension):
			# 	nest'[0][i] = nest[0][i]
	sort_nests(nests)
	max_fit = nests[0][1]
	if max_fit > best_nest[1]:
		best_nest[1] = max_fit
		best_nest[0] = [xi for xi in nests[0][0]]

	worst_nest_index = int((1-Pa)*number_nests)
	for i in xrange(worst_nest_index, number_nests):
		nests[worst_nest_index] = generate_new_nest()
	
	sigma = random.uniform(0, 1)
	for nest in nests:
		for i in xrange(dimension):
			x = nest[0][i] + step_size*levy_dist(3)
			if(sigma < sigmoid(x)):
				nest[0][i] = 1
			else:
				nest[0][i] = 0

print best_nest