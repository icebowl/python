count = 0
while True:
	print(count," ",end="")
	count = count + 1
	if count % 10 == 0: print()
	if count > 100: break
print("count reached 100", count)


