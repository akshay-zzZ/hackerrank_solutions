s = input()
if(s[8:] == "AM" and s[:] != '12:00:00AM'):
	if(s[:2]== '12'):
		b = int(s[:2]) * 0
		print('0' + str(b) + s[2:8])
	else:
		print(s[:8])
if(s[:] == '12:00:00AM' ):
	print("00:00:00")
if(s[:] == '12:00:00PM' ):
	print("12:00:00")
if(s[8:] == "PM" and s[:2] == '12'):
	print(s[:8])
if(s[8:] == "PM" and s[:2] != '12' ):
	a = int(s[:2]) +12
	print(str(a) + s[2:8])
    