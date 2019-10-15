def count_sub(string,sub):
	count = 0
	for i in range(len(string)):
		if(string[i:i+len(sub)] == sub):
			count += 1
	return count

if __name__ == '__main__':
	string = input().strip()
	sub = input().strip()
	count = count_sub(string,sub)
	print(count)