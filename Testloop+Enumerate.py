#การเรียงลำดับชุดข้อมูล Enumerate

print('----Loop in Dictionary----')

friend2 = {'Nine':'คุณนาย',
            'Jame':'คุณเจม',
            'Yai':'คุณใหญ่'}

for f in friend2:
	print(f)

for k,v in friend2.items():
	print('Key:',k)
	print('Value:',v)

for f in friend2.keys():
	print(f)

for f in friend2.values():
	print(f)

for i,f in enumerate(friend2):
	print(i,f)