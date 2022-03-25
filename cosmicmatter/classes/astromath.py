import math
"""
Common Astro Math Formulas used throughout the application
"""

class AstroMath:
    '''
    This class contains all the functions related to the math involved.
    '''
    def __init__(self, *args, **kwargs) -> None:
        pass

    def luminosityOfStar(brightness, distance) -> float:
        '''
        Calculates the luminosity of a star.
        :param brightness: The brightness of the star.
        :param distance: The distance of the star.
        :return: The luminosity of the star.
        '''
        luminosity = brightness * 12.57 * pow(distance, 2)
        return luminosity

    def areaOfSquare(distance) -> float:
        '''
        Calculates the area of a square.
        :param distance: The length of the side of the square.
        :return: The area of the square.
        '''
        return pow(distance, 2)

    def areaOfCircle(radius) -> float:
        '''
        Calculates the area of a circle.
        :param radius: The radius of the circle.
        :return: The area of the circle.
        '''
        return math.pi * pow(radius, 2)

    def circumferanceOfCircle(radius) -> float:
        '''
        Calculates the circumferance of a circle.
        :param radius: The radius of the circle.
        :return: The circumferance of the circle.
        '''
        return 2 * math.pi * radius