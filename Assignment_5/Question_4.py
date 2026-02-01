#Predict the output:
ba = bytearray([65, 66, 67]) 
ba[0] = 97
print(ba)
#Why is this allowed?
#bytearray(b'aBC')

#As bytearray is mutable, we can edit value under it