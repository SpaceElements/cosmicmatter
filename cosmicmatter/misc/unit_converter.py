# Cosmic Matter - Unit Converter 
# by: Ira Bell       Version 0.1 
# Copyright (c) 2022 Space Elements

import os
import time

# The following program converts:
# (mi) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (m) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (km) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (cm) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (mm) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (µm) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (nm) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (yd) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (ft) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (in) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (NM) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (ly) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (pc) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (kpc) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (Mpc) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
# (AU) -> km, m, cm, mm, µm, nm, yd, ft, in, NM, ly, pc, kjpc, Mpc, AU
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
# ly = Light Years
# pc = parsec
# kpc = Kiloparsec
# Mpc = megaparsec
# AU = Astronomical Unit
# Written by Ira Bell
# Copyright (c) 2022 Space Elements

def miles_input(miles):
	meters = (miles * 1609.344)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (miles * 1.609344)
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
	nautical_miles = (miles * 0.8684210526)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (miles * 1.7010779502326E-13)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (miles * 5.2155287051488E-14)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (miles * 5.2155287051488E-17)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (miles * 5.2155287051488E-20)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (miles * 1.0757800178347E-8)
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
	inches = (meters * 39.3700787402)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (meters * 0.0005396118)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (meters * 1.0570008340247E-16)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (meters * 3.2407792896664E-17)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (meters * 3.2407792896664E-20)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (meters * 3.2407792896664E-23)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (meters * 6.6845871226706E-12)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def kilometers_input(kilometers):
	miles = (kilometers * 0.6213711922)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (kilometers * 1000)
	meters_str = print(f"\t{meters} Meters (m)")
	centimeters = (kilometers * 100000)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (kilometers * 1000000)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (kilometers * 1000000000)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (kilometers * 1000000000000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (kilometers * 1093.6132983377)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (kilometers * 3280.8398950131)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (kilometers * 39370.078740157)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (kilometers * 0.5396118248)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (kilometers * 1.0570008340247E-13)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (kilometers * 3.2407792896664E-14)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (kilometers * 3.2407792896664E-17)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (kilometers * 3.2407792896664E-20)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (kilometers * 6.6845871226706E-9)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def centimeters_input(centimeters):
	miles = (centimeters * 6.2137119223733E-6)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (centimeters * 0.01)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (centimeters * 1.00E-5)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	millimeters = (centimeters * 10)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (centimeters * 10000)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (centimeters * 10000000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (centimeters * 0.010936133)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (centimeters * 0.032808399)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (centimeters * 0.3937007874)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (centimeters * 5.3961182483769E-6)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (centimeters * 1.0570008340247E-18)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (centimeters * 3.2407792896664E-19)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (centimeters * 3.2407792896664E-22)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (centimeters * 3.2407792896664E-25)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (centimeters * 6.6845871226706E-14)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def millimeters_input(millimeters):
	miles = (millimeters * 6.2137119223733E-7)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (millimeters * 0.001)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (millimeters * 1.00E-6)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (millimeters * 0.1)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	micrometers = (millimeters * 1000)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (millimeters * 1000000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (millimeters * 0.0010936133)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (millimeters * 0.0032808399)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (millimeters * 0.0393700787)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (millimeters * 5.3961182483768E-7)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (millimeters * 1.0570008340247E-19)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (millimeters * 3.2407792896664E-20)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (millimeters * 3.2407792896664E-23)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (millimeters * 3.2407792896664E-26)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (millimeters * 6.6845871226706E-15)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def micrometers_input(micrometers):
	miles = (micrometers * 6.2137119223733E-10)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (micrometers * 1.00E-6)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (micrometers * 1.00E-9)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (micrometers * 0.0001)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (micrometers * 0.001)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	nanometers = (micrometers * 1000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (micrometers * 1.0936132983377E-6)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (micrometers * 3.2808398950131E-6)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (micrometers * 3.93701E-5)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (micrometers * 5.3961182483769E-10)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (micrometers * 1.0570008340247E-22)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (micrometers * 3.2407792896664E-23)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (micrometers * 3.2407792896664E-26)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (micrometers * 3.2407792896664E-29)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (micrometers * 6.6845871226706E-18)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def nanometers_input(nanometers):
	miles = (nanometers * 6.2137119223733E-13)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (nanometers * 1.00E-9)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (nanometers * 1.00E-12)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (nanometers * 1.00E-7)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (nanometers * 1.00E-6)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (nanometers * 0.001)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	yards = (nanometers * 1.0936132983377E-9)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (nanometers * 3.2808398950131E-9)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (nanometers * 3.9370078740157E-8)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (nanometers * 5.3961182483768E-13)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (nanometers * 1.0570008340247E-25)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (nanometers * 3.2407792896664E-26)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (nanometers * 3.2407792896664E-29)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (nanometers * 3.2407792896664E-32)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (nanometers * 6.6845871226706E-21)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def yards_input(yards):
	miles = (yards * 0.0005681818)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (yards * 0.9144)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (yards * 0.0009144)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (yards * 91.44)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (yards * 914.4)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (yards * 914400)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (yards * 914400000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	feet = (yards * 3)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (yards * 36)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (yards * 0.0004934211)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (yards * 9.6652156263218E-17)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (yards * 2.9633685824709E-17)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (yards * 2.9633685824709E-20)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (yards * 2.9633685824709E-23)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (yards * 6.11238646497E-12)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def feet_input(feet):
	miles = (feet * 0.0001893939)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (feet * 0.3048)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (feet * 0.0003048)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (feet * 30.48)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (feet * 304.8)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (feet * 304800)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (feet * 304800000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (feet * 0.3333333333)
	yards_str = print(f"\t{yards} Yards (yd)")
	inches = (feet * 12)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (feet * 0.0001644737)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (feet * 3.2217385421073E-17)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (feet * 9.8778952749031E-18)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (feet * 9.8778952749031E-21)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (feet * 9.8778952749031E-24)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (feet * 2.03746215499E-12)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def inches_input(inches):
	miles = (inches * 1.57828E-5)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (inches * 0.0254)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (inches * 2.54E-5)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (inches * 2.54)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (inches * 25.4)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (inches * 25400)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (inches * 25400000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (inches * 0.0277777778)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (inches * 0.0833333333)
	feet_str = print(f"\t{feet} Feet (ft)")
	nautical_miles = (inches * 1.37061E-5)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (inches * 2.6847821184227E-18)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (inches * 8.2315793957526E-19)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (inches * 8.2315793957526E-22)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (inches * 8.2315793957526E-25)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (inches * 1.6978851291583E-13)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def nautical_miles_input(nautical_miles):
	miles = (nautical_miles * 1.1515151515)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (nautical_miles * 1853.184)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (nautical_miles * 1.853184)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (nautical_miles * 185318.4)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (nautical_miles * 1853184)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (nautical_miles * 1853184000)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (nautical_miles * 1853184000000)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (nautical_miles * 2026.6666666667)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (nautical_miles * 6080)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (nautical_miles * 72960)
	inches_str = print(f"\t{inches} Inches (in)")
	light_years = (nautical_miles * 1.9588170336012E-13)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (nautical_miles * 6.0057603271411E-14)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (nautical_miles * 6.0057603271411E-17)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (nautical_miles * 6.0057603271411E-20)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (nautical_miles * 1.2387769902339E-8)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def light_years_input(light_years):
	miles = (light_years * 5878625373183.1)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (light_years * 9.46073047258E+15)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (light_years * 9460730472580)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (light_years * 9.46073047258E+17)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (light_years * 9.46073047258E+18)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (light_years * 9.46073047258E+21)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (light_years * 9.46073047258E+24)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (light_years * 1.0346380656802E+16)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (light_years * 3.1039141970407E+16)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (light_years * 3.7246970364488E+17)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (light_years * 5105122034606.4)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	parsecs = (light_years * 0.3066013938)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (light_years * 0.0003066014)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (light_years * 3.0660139380653E-7)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (light_years * 63241.077088066)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, parsecs_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def parsecs_input(parsecs):
	miles = (parsecs * 19173511575400)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (parsecs * 3.08567758128E+16)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (parsecs * 30856775812800)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (parsecs * 3.08567758128E+18)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (parsecs * 3.08567758128E+19)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (parsecs * 3.08567758128E+22)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (parsecs * 3.08567758128E+25)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (parsecs * 3.3745380372703E+16)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (parsecs * 1.0123614111811E+17)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (parsecs * 1.2148336934173E+18)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (parsecs * 16650681104952)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (parsecs * 3.2615637769)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	kiloparsecs = (parsecs * 0.001)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (parsecs * 1.00E-6)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (parsecs * 206264.80624538)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, kiloparsecs_str, megaparsecs_str, astronomical_units_str

def kiloparsecs_input(kiloparsecs):
	miles = (kiloparsecs * 1.91735115754E+16)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (kiloparsecs * 3.08567758128E+19)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (kiloparsecs * 3.08567758128E+16)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (kiloparsecs * 3.08567758128E+21)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (kiloparsecs * 3.08567758128E+22)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (kiloparsecs * 3.08567758128E+25)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (kiloparsecs * 3.08567758128E+28)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (kiloparsecs * 3.3745380372703E+19)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (kiloparsecs * 1.0123614111811E+20)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (kiloparsecs * 1.2148336934173E+21)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (kiloparsecs * 1.6650681104952E+16)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (kiloparsecs * 3261.5637769443)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (kiloparsecs * 1000)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	megaparsecs = (kiloparsecs * 0.001)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	astronomical_units = (kiloparsecs * 206264806.24538)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, megaparsecs_str, astronomical_units_str

def megaparsecs_input(megaparsecs):
	miles = (megaparsecs * 1.91735115754E+19)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (megaparsecs * 3.08567758128E+22)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (megaparsecs * 3.08567758128E+19)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (megaparsecs * 3.08567758128E+24)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (megaparsecs * 3.08567758128E+25)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (megaparsecs * 3.08567758128E+28)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (megaparsecs * 3.08567758128E+31)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (megaparsecs * 3.3745380372703E+22)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (megaparsecs * 1.0123614111811E+23)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (megaparsecs * 1.2148336934173E+24)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (megaparsecs * 1.6650681104952E+19)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (megaparsecs * 3261563.7769443)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (megaparsecs * 1000000)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (megaparsecs * 1000)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	astronomical_units = (megaparsecs * 206264806245.38)
	astronomical_units_str = print(f"\t{astronomical_units} Astronomical Units (AU)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, astronomical_units_str

def astronomical_units_input(astronomical_units):
	miles = (astronomical_units * 92955807.267433)
	miles_str = print(f"\t{miles} Miles (mi)")
	meters = (astronomical_units * 149597870691)
	meters_str = print(f"\t{meters} Meters (m)")
	kilometers = (astronomical_units * 149597870.691)
	kilometers_str = print(f"\t{kilometers} Kilometers (km)")
	centimeters = (astronomical_units * 14959787069100)
	centimeters_str = print(f"\t{centimeters} Centimeters (cm)")
	millimeters = (astronomical_units * 1.49597870691E+14)
	millimeters_str = print(f"\t{millimeters} Millimeters (mm)")
	micrometers = (astronomical_units * 1.49597870691E+17)
	micrometers_str = print(f"\t{micrometers} Micrometers (µm)")
	nanometers = (astronomical_units * 1.49597870691E+20)
	nanometers_str = print(f"\t{nanometers} Nanometers (nm)")
	yards = (astronomical_units * 163602220790.68)
	yards_str = print(f"\t{yards} Yards (yd)")
	feet = (astronomical_units * 490806662372.05)
	feet_str = print(f"\t{feet} Feet (ft)")
	inches = (astronomical_units * 5889679948464.6)
	inches_str = print(f"\t{inches} Inches (in)")
	nautical_miles = (astronomical_units * 80724779.995403)
	nautical_miles_str = print(f"\t{nautical_miles} Nautical Miles (NM)")
	light_years = (astronomical_units * 4.8481368111358E-6)
	light_years_str = print(f"\t{light_years} Light Years (ly)")
	parsecs = (astronomical_units * 4.8481368111358E-6)
	parsecs_str = print(f"\t{parsecs} Parsecs (pc)")
	kiloparsecs = (astronomical_units * 4.8481368111358E-9)
	kiloparsecs_str = print(f"\t{kiloparsecs} Kiloparsecs (kpc)")
	megaparsecs = (astronomical_units * 4.8481368111358E-12)
	megaparsecs_str = print(f"\t{megaparsecs} Megaparsecs (Mpc)")
	return miles_str, meters_str, kilometers_str, centimeters_str, millimeters_str, micrometers_str, nanometers_str, yards_str, feet_str, inches_str, nautical_miles_str, light_years_str, parsecs_str, kiloparsecs_str, megaparsecs_str

# Check whether the input is valid, and if so - whether it's an integer, scientific number or floating number
def float_test(examine):
	str_test = str(examine)
	if 'e' in str_test.lower():
		print(f"\n\t{examine}: Detected an 'e' in the input, evaluating if input is scientific notation.\n")
		time.sleep(1)
		try:
			val = float(examine)
			print(f"\n\t{examine} can be converted to a float or scientific number and is acceptable to evaluate: \n\t{val}")
			time.sleep(1)
		except ValueError:
			print(f"\t\n'{examine}' is a string and not acceptable to evaluate.\n")
			print(f"The program will reset in five seconds.")
			time.sleep(5)
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
					print(f"\t\n'{examine}' is a string and not acceptable to evaluate.\n")
					print(f"The program will reset in five seconds.")
					time.sleep(5)
					clear = lambda: os.system('cls')
					clear()
					main_program()

# Breaking out copyright/credit and allow for sub-routine
def main_program():
	print("-=-=   Cosmic Matter - Unit Converter     =-=-")
	print("-=-=   by: Ira Bell       Version 0.1     =-=-")
	print("-=-=   Copyright (c) 2022 Space Elements  =-=-")
	sub_program()

# Main sub-routine
def sub_program():
	
	while True:
		print(f"\nPlease input the unit classification you would like to convert from\n(note: this is case sensitive)\n\n[Options]:\n\n[mi, m, km, cm, mm, micrometers, nm, yd, ft, in, NM, ly, pc, \nkpc, Mpc, AU], 'cls' to clear screen or 'q' to quit.")
		
		unit_classification = input("\n>>> ")
		
		# User wants to quit
		if unit_classification == 'q' or unit_classification == 'Q' or unit_classification == 'quit' or unit_classification == 'QUIT':
			quit()
		# Miles
		if unit_classification == 'mi':
			print("\nYou have selected Miles.\n")
			miles = input("Please enter the distance in Miles that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(miles)
			print("\n...calculating...")
			print(f"\n{miles} Miles converts to:\n")
			miles_input(float(miles))
		elif unit_classification == 'm':
			print("\nYou have selected Meters.\n")
			meters = input("Please enter the distance in Meters that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(meters)
			print("\n...calculating...")
			print(f"\n{meters} Meters converts to:\n")
			meters_input(float(meters))
		# Kilometers
		elif unit_classification == 'km':
			print("\nYou have selected Kilometers.\n")
			kilometers = input("Please enter the distance in Kilometers that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(kilometers)
			print("\n...calculating...")
			print(f"\n{kilometers} Kilometers converts to:\n")
			kilometers_input(float(kilometers))
		# Centimeters
		elif unit_classification == 'cm':
			print("\nYou have selected Centimeters.\n")
			centimeters = input("Please enter the distance in Centimeters that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(centimeters)
			print("\n...calculating...")
			print(f"\n{centimeters} Centimeters converts to:\n")
			centimeters_input(float(centimeters))
		# Millimeters
		elif unit_classification == 'mm':
			print("\nYou have selected Millimeters.\n")
			millimeters = input("Please enter the distance in Kilometers that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(millimeters)
			print("\n...calculating...")
			print(f"\n{millimeters} Millimeters converts to:\n")
			millimeters_input(float(millimeters))
		# Micrometers
		elif unit_classification == 'µm' or unit_classification == 'micrometers' or unit_classification == 'Micrometers' or unit_classification == 'MICROMETERS':
			print("\nYou have selected Micrometers.\n")
			micrometers = input("Please enter the distance in Micrometers that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(micrometers)
			print("\n...calculating...")
			print(f"\n{micrometers} Micrometers converts to:\n")
			micrometers_input(float(micrometers))
		# Nanometers
		elif unit_classification == 'nm':
			print("\nYou have selected Nanometers.\n")
			nanometers = input("Please enter the distance in Nanometers that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(nanometers)
			print("\n...calculating...")
			print(f"\n{nanometers} Nanometers converts to:\n")
			nanometers_input(float(nanometers))
		# Yards
		elif unit_classification == 'yd':
			print("\nYou have selected Yards.\n")
			yards = input("Please enter the distance in Yards that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(yards)
			print("\n...calculating...")
			print(f"\n{yards} Yards converts to:\n")
			yards_input(float(yards))
		# Feet
		elif unit_classification == 'ft':
			print("\nYou have selected Feet.\n")
			feet = input("Please enter the distance in Feet that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(feet)
			print("\n...calculating...")
			print(f"\n{feet} Feet converts to:\n")
			feet_input(float(feet))
		# Inches
		elif unit_classification == 'in':
			print("\nYou have selected Inches.\n")
			inches = input("Please enter the distance in Inches that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(inches)
			print("\n...calculating...")
			print(f"\n{inches} Inches converts to:\n")
			inches_input(float(inches))
		# Nautical Miles
		elif unit_classification == 'NM':
			print("\nYou have selected Nautical Miles.\n")
			nautical_miles = input("Please enter the distance in Nautical Miles that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(nautical_miles)
			print("\n...calculating...")
			print(f"\n{nautical_miles} Nautical Miles converts to:\n")
			nautical_miles_input(float(nautical_miles))
		# Light Years
		elif unit_classification == 'ly':
			print("\nYou have selected Light Years.\n")
			light_years = input("Please enter the distance in Light Years that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(light_years)
			print("\n...calculating...")
			print(f"\n{light_years} Light Years converts to:\n")
			light_years_input(float(light_years))
		# Parsecs
		elif unit_classification == 'pc':
			print("\nYou have selected Parsecs.\n")
			parsecs = input("Please enter the distance in Parsecs that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(parsecs)
			print("\n...calculating...")
			print(f"\n{parsecs} Parsecs converts to:\n")
			parsecs_input(float(parsecs))
		# Kiloparsecs
		elif unit_classification == 'kpc':
			print("\nYou have selected Kiloparsecs.\n")
			kiloparsecs = input("Please enter the distance in Kiloparsecs that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(kiloparsecs)
			print("\n...calculating...")
			print(f"\n{kiloparsecs} Kiloparsecs converts to:\n")
			kiloparsecs_input(float(kiloparsecs))
		# Megaparsecs
		elif unit_classification == 'Mpc':
			print("\nYou have selected Megaparsecs.\n")
			megaparsecs = input("Please enter the distance in Megaparsecs that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(megaparsecs)
			print("\n...calculating...")
			print(f"\n{megaparsecs} Kilometers converts to:\n")
			megaparsecs_input(float(megaparsecs))
		# Astronomical Units
		elif unit_classification == 'AU':
			print("\nYou have selected Astronomical Units.\n")
			astronomical_units = input("Please enter the distance in Astronomical Units that you would like to convert.\n\n>>> ")
			print("\n...inspecting...")
			float_test(astronomical_units)
			print("\n...calculating...")
			print(f"\n{astronomical_units} Kilometers converts to:\n")
			astronomical_units_input(float(astronomical_units))
		else:
			clear = lambda: os.system('cls')
			clear()
			main_program()
		sub_program()
	sub_program()

# Run main program 
main_program()
	

