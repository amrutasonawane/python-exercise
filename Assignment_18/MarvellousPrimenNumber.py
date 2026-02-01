def checkPrime(value):
	for i in range(2,(value//2)+1):
		if (value % i) == 0:
			return False
	return True
