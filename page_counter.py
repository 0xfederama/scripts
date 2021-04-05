CURSOR_UP="\x1b[1A"
numpages = int(input("How many pages do you want to study? "))
digits = len(str(numpages))
for i in range(1, numpages+1):
	input()
	print(f"{CURSOR_UP}You studied {i:{digits}} pages, {numpages-i} left!")
print("DONE!")
