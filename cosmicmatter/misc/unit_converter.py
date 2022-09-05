import os
import time

# The following program converts:
# (mi) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly
# 
# Whereby:
# mi = Miles
#  m = Meters
# km = Kilometers
# cm = Centimeters
# mm = Millimeters
# µm = Micrometers
# nm = Nanometers
# yd = Yards
# ft = Feet
# in = Inches
# NM = Nautical Miles
# ly = Light Year#
# pc = parsec
# kpc = Kiloparsec
# Mpc = megaparsec
# AU = Astronomical Unit
# Written by Ira Bell
# Copyright (c) 2022 Space Elements

def miles_input(miles):
	meters = (miles * 1609.34)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (miles * 1.60934)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (miles * 160934.4)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (miles * 16099344)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (miles * 1609344000)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (miles * 1609344000000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (miles * 1760)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (miles * 5280)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (miles * 63360)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (miles * 0.868976)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (miles * 1.70107795E-13)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (miles * 5.215528705E-14)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (miles * 5.215528705E-17)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (miles * 5.215528705E-20)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (miles * 1.075780017E-8)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def meters_input(meters):
	miles = (meters * 0.0006213712)
	miles_str = print(f"\t{miles} Miles (mi)")
	kilometers = (meters * 0.001)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (meters * 100)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (meters * 1000)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (meters * 1000000)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (meters * 1000000000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (meters * 1.0936132983)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (meters * 3.280839895)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (meters * 39.37007874)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (meters * 0.0005396118)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (meters * 1.057000834E-16)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (meters * 3.240779289E-17)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (meters * 3.240779289E-20)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (meters * 3.240779289E-23)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (meters * 6.684587122E-12)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str


def float_test(examine):
	str_test = str(examine)
	if 'e' in str_test.lower():
		print(f"\n\t{examine}: Detected an 'e' in the input, evaluating if input is scientific notation.")
		time.sleep(1)
		try:
			val = float(examine)
			print(f"\n\t{val} can be converted to a float number and is acceptable to evaluate.")
			time.sleep(1)
		except ValueError:
			print(f"\t{examine} is a string and not acceptable to evaluate.")
			print(f"\tThe program will reset in three seconds.")
			time.sleep(2)
			clear = lambda: os.system('cls')
			clear()
			main_program()
	else:
		try:
			val = int(examine)
			print(f"\n\t{val} appears to be an integer and acceptable to evaluate.")
			time.sleep(1)
		except ValueError:
				try:
					val = float(examine)
					print(f"\t{val} appears to be a float number and acceptable to evaluate.")
					time.sleep(1)
				except ValueError:
					print(f"\t{examine} is a string and not acceptable to evaluate.")
					print(f"\tThe program will reset in three seconds.")
					time.sleep(2)
					clear = lambda: os.system('cls')
					clear()
					main_program()


# mi = Miles
#  m = Meters
# km = Kilometers
# cm = Centimeters
# mm = Millimeters
# µm = Micrometers
# nm = Nanometers
# yd = Yards
# ft = Feet
# in = Inches
# NM = Nautical Miles
# ly = Light Year#
# pc = parsec
# kpc = Kiloparsec
# Mpc = megaparsec
# AU = Astronomical Unit

def main_program():
	while True:
		print(f"\nPlease input the unit classification you would like to convert from (note: this is cases sensitive)\n[mi, m, km, cm, mm, micrometers, nm, yd, ft, in, NM, ly, pc, kpc, Mpc, AU] or 'q' to quit.")
		
		unit_classification = input("\n>>> ")
		
		# User wants to quit
		if unit_classification == 'q' or unit_classification == 'Q' or unit_classification == 'quit' or unit_classification == 'QUIT':
			quit()
		# Miles
		if unit_classification == 'mi':
			print("\nYou have selected Miles.")
			miles = input("Please enter the distance in Miles that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(miles)
			print("\n...calculating...")
			print(f"\n{miles} Miles converts to:")
			miles_input(float(miles))
		elif unit_classification == 'm':
			print("\nYou have selected Meters.")
			meters = input("Please enter the distance in Meters that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(meters)
			print("\n...calculating...")
			print(f"\n{meters} Meters converts to:")
			meters_input(float(meters))
		# Kilometers
		elif unit_classification == 'km':
			print("\nYou have selected Kilometers.")
			kilometers = input("Please enter the distance in Kilometers that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Centimeters
		elif unit_classification == 'cm':
			print("\nYou have selected Centimeters.")
			centimeters = input("Please enter the distance in Centimeters that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(centimeters)
			print("\n...calculating...")
			print(f"\n{centimeters} Kilometers converts to:")
			centimeters_input(float(centimeters))
		# Millimeters
		elif unit_classification == 'mm':
			print("\nYou have selected Millimeters.")
			millimeters = input("Please enter the distance in Kilometers that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(millimeters)
			print("\n...calculating...")
			print(f"\n{millimeters} Kilometers converts to:")
			millimeters_input(float(millimeters))
		# Micrometers
		elif unit_classification == 'µm' or unit_classification == 'micrometers' or unit_classification == 'Micrometers' or unit_classification == 'MICROMETERS':
			print("\nYou have selected Micrometers.")
			kilometers = input("Please enter the distance in Kilometers that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Nanometers
		elif unit_classification == 'nm':
			print("\nYou have selected Nanometers.")
			nanometers = input("Please enter the distance in Nanometers that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(nanometers)
			print("\n...calculating...")
			print(f"\n{nanometers} Kilometers converts to:")
			kilometers_input(float(nanometers))
		# Yards
		elif unit_classification == 'yd':
			print("\nYou have selected Yards.")
			kilometers = input("Please enter the distance in Kilometers that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Feet
		elif unit_classification == 'ft':
			print("\nYou have selected Feet.")
			kilometers = input("Please enter the distance in Kilometers that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Inches
		elif unit_classification == 'in':
			print("\nYou have selected Inches.")
			kilometers = input("Please enter the distance in Kilometers that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Nautical Miles
		elif unit_classification == 'NM':
			print("\nYou have selected Nautical Miles.")
			kilometers = input("Please enter the distance in Nautical Miles that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Light Years
		elif unit_classification == 'ly':
			print("\nYou have selected Light Years.")
			kilometers = input("Please enter the distance in Light Years that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Parsecs
		elif unit_classification == 'pc':
			print("\nYou have selected Parsecs.")
			kilometers = input("Please enter the distance in Nautical Miles that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Kiloparsecs
		elif unit_classification == 'kpc':
			print("\nYou have selected Kiloparsecs.")
			kilometers = input("Please enter the distance in Nautical Miles that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		# Megaparsecs
		elif unit_classification == 'Mpc':
			print("\nYou have selected Megaparsecs.")
			kilometers = input("Please enter the distance in Nautical Miles that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		elif unit_classification == 'AU':
			print("\nYou have selected Astronomical Units.")
			kilometers = input("Please enter the distance in Nautical Miles that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:")
			kilometers_input(float(kilometers))
		else:
			clear = lambda: os.system('cls')
			clear()
		main_program()
	main_program()

# Run main program 

main_program()
	

