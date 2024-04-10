multiple = 3
no_of_times = 15
counter = 0
for index in range(3, 100):
	if(index % multiple == 0 and counter < 15):
		counter += 1
		print(index,end=" ")