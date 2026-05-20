import os

arquivo = input("diga seu arquivo")
for root, dirs, files in os.walk("C:\\"):
	for file in files:
		if arquivo in file:
			print(f"achei : {root}\\{file}")
i = input("tecle enter")
os.system("cls")