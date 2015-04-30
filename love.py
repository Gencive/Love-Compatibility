
from sys import argv, exit

if len(argv) != 3:
	print("0%");
	exit()

name1 = argv[1].lower();
name2 = argv[2].lower();


res = sum(map(ord, name1)) + sum(map(ord, name2))

res %= 100

print(str(res) + "%")
