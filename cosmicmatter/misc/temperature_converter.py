import os
import time

# The following program converts any
# F -> K, F -> C, K -> F, K -> C,
# C -> F, and C -> K
# Whereby:
# C = Celsius
# F = Fahrenheit
# K = Kelvin
# Written by Ira Bell
# Copyright (c) 2022 Space Elements

def celsius_input(celsius):
	fahrenheit = (celsius * 1.8) + 32
	fahrenheit_str = print(f"\t{fahrenheit} degrees Fahrenheit")
	kelvin = celsius + 273.15
	kelvin_str = print(f"\t{kelvin} degrees Kelvin")
	return fahrenheit, fahrenheit_str, kelvin, kelvin_str

def fahrenheit_input(fahrenheit):
	celsius = (fahrenheit - 32) * .5556
	celsius_str = print(f"\t{celsius} degrees Celsius")
	kelvin = ((fahrenheit - 32) * (5/9)) + 273.15
	kelvin_str = print(f"\t{kelvin} degrees Kelvin")
	return celsius, celsius_str, kelvin, kelvin_str

def kelvin_input(kelvin):
	celsius = kelvin - 273.15
	celsius_str = print(f"\t{celsius} degrees Celsius")
	fahrenheit = (kelvin * (9/5)) - 459.67
	fahrenheit_str = print(f"\t{fahrenheit} degrees Fahrenheit")
	return celsius, celsius_str, fahrenheit, fahrenheit_str

def float_test(examine):
    try:
        # Convert it into integer
        val = int(examine)
        print(f"\t{val} is an integer and acceptable to evaluate.")
    except ValueError:
        try:
            # Convert it into float
            val = float(examine)
            print(f"\n\t{val} is a float number and acceptable to evaluate.")
        except ValueError:
            print(f"\t{examine} is a string and not acceptable to evaluate.")
            print(f"\tThe program will reset in three seconds.")
            time.sleep(3)
            clear = lambda: os.system('cls')
            clear()
            main_program()

def main_program():
	while True:
		print(f"\nPlease input the temperature classification you would like to convert from [c, f, k] or 'q' to quit.")
		
		temperature_classification = input("\n>>> ")
		
		if temperature_classification == 'q' or temperature_classification == 'Q':
			quit()
		if temperature_classification == 'c' or temperature_classification == 'C':
			print("\nYou have selected Celsius.")
			celsius = input("Please enter the temperature in Celsius that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(celsius)
			print("\n...calculating...")
			print(f"\n{celsius} degrees Celsius converts to:")
			celsius_input(float(celsius))
		elif temperature_classification == 'f' or temperature_classification == 'F':
			print("\nYou have selected Fahrenheit.")
			fahrenheit = input("Please enter the temperature in Fahrenheit that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(fahrenheit)
			print("\n...calculating...")
			print(f"\n{fahrenheit} degrees Fahrenheit converts to:")
			fahrenheit_input(float(fahrenheit))
		elif temperature_classification == 'k' or temperature_classification == 'K':
			print("\nYou have selected Kelvin.")
			kelvin = input("Please enter the temperature in Kelvin that you would like to convert.\n>>> ")
			print("\n...inspecting...")
			float_test(kelvin)
			print("\n...calculating...")
			print(f"\n{kelvin} degrees Kelvin converts to:")
			kelvin_input(float(kelvin))
		else:
			clear = lambda: os.system('cls')
			clear()
		main_program()
	main_program()

# Run main program 

main_program()
	

