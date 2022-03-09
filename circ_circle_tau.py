#!/usr/bin/env python3
# Created by: Hunter Connolly
# March 8
# This program calculates the radius of a circle
# using tau and the radius received by the user

import constants


def main():
    # get the radius from the user (input)
    print("Today we will be calculating the radius of a circle using TAU!")
    radius = float(input("What is the radius of the circle? (cm): "))

    # calculate the circumference (process)
    circumference = constants.TAU * radius

    # display the circumference of the circle (output)
    print("")
    print("The circumference is: {} cm" .format(circumference))


if __name__ == "__main__":
    main()
