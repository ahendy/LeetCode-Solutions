
def subsets(l, pos, sett, solution, size):
	if len(sett) == size:
		solution.append(sett)

	if pos == len(l):
		return

	subsets(l, pos+1, sett, solution, size)
	subsets(l, pos+1, sett + [l[pos]], solution, size)



if __name__ == '__main__':
	solution = []
	subsets(range(5), 0, [], solution, 3)
	print solution