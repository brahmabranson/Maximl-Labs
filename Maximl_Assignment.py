string = input()

def smallest_substring(string):
	w = set()
	w.add(string[0])
	i = 0
	j = 1
	result = 1
	while i<=j and j<len(string):
		if string[j] in w:
			w.remove(string[i])
			i+=1
		else:
			w.add(string[j])
			j+=1
		result = max(len(w),result)
	return result

print(smallest_substring(string))
