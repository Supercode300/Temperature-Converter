# Created by Supercode300 on 19/10/2026

def fconvc():
	varF = input("Enter Fahreneit Degrees: ")
	varF = int(varF)
	varC = float((varF-32)/1.8)
	print(f"Your Temperature is {varC}°C")

def cconvf():
	varC = input("Enter Celsius Degrees: ")
	varC = int(varC)
	varF = float((varC*1.8)+32)
	print(f"Your Temperature is {varF}°F")

def kconvf():
	varK = input("Enter Kelvin Degrees: ")
	varK = int(varK)
	varF = float(varK-273.15)*(9/5)+32
	print(f"Your Temperature is {varF}°F")

def fconvk():
	varF = input("Enter Fahreneit Degrees: ")
	varF = int(varF)
	varK = float(varF-32)*(5/9)+32
	print(f"Your Temperature is {varK}K")

def kconvc():
	varK = input("Enter Kelvin Degrees: ")
	varK = int(varK)
	varC = float(varK-273.15)
	print(f"Your Temperature is {varC}°C")

def cconvk():
	varC = input("Enter Celsius Degrees: ")
	varC = int(varC)
	varK = float(varC+273.15)
	print(f"Your Temperature is {varK}K")

print("Converter from Fahreneit to Celsius Degrees")

while True:
	try:
		var = input("Enter your degrees first (FC/CF/KF/FK/KC/CK): ")
		if var == "FC":
			fconvc()
		elif var == "CF":
			cconvf()
		elif var == "KF":
			kconvf()
		elif var == "FK":
			fconvk()
		elif var == "KC":
			kconvc()
		elif var == "CK":
			cconvk()
		else:
			print("It is not a valid selection. Try again")
	except KeyboardInterrupt:
		print("\nThanks")
		break
