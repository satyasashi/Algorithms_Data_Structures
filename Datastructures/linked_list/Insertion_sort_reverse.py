# A = [3,4,6,234,5,35,23,4,74,42,8,]
A = [5,3,4,7,2,8,6,9,1]



for j in range(1, len(A)):
	key = A[j]

	i = j -1

	while i > -1 and A[i] < key:
		A[i+1] = A[i]
		i = i - 1

	A[i+1] = key

print(A)




















# INSERTION SORT
"""Check if array has atleast 2 elements(Indexes - 0,1). Array having only 1 element
and SORTING it is MEANING LESS (Index - 0). """
A = [5,3,4,7,2,8,6,9,1]

for j in range(1, len(A)):
	key = A[j]

	print("\n Index or J: "+str(j))
	print("Key : "+str(key))
	
	# Insert A[j] into sorted sequence A[1....j-1]
	i = j - 1
	print("Taking 'i' as 'j - 1':"+str(i)+"\n")

	if A[i] < key:
		print("A["+str(i)+"] --> "+str(A[i])+" is NOT GREATER THAN "+str(key))
	else:
		while i > -1 and A[i] < key:
			print("While 'i' is > -1, and A["+str(i)+"] --> " +str(A[i]) + " > key  "+str(key))
			A[i+1] = A[i]
			print("A["+str(i)+"] is "+str(A[i])+ " And make A["+str(i+1)+"] is "+str(A[i+1]))
			i = i-1 # to avoid infinity loop.
			print("Now 'i' is reduced by ONE: "+str(i)+"\n")

	A[i+1] = key
	print("A["+str(i+1)+"] = "+str(key))
	print(A)
	print("==========================")


	# print("Making Key for next iteration. Array[nextElement] = "+str(A[i+1])+"\n")
