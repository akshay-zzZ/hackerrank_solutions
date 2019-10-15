import random
def ran_list(n):
	s = [0]*n*7473
	for i in range(n):
		s[i]=random.random()
	return s
print((ran_list(8)))