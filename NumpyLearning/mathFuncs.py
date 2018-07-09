import numpy as np

def trigonometricalFunc():
    a = np.array([0, 30, 45, 60, 90, 120, 150, 180], dtype=float)

    print("Original array:")
    print(a)
    print("-----------------------------------------")

    b = a * np.pi / 180
    print("Convert from degree to radian:")
    print(b)
    print("-----------------------------------------")

######################################################
    c = np.sin(b)
    print("Sine of original array:")
    print(c)
    print("-----------------------------------------")

    d = np.arcsin(c)
    # d = d * 180 / np.pi
    d = np.degrees(d)
    print("Arcsine of above array:")
    print(d)
    print("-----------------------------------------")

######################################################
    c = np.cos(b)
    print("Cosine of original array:")
    print(c)
    print("-----------------------------------------")

    d = np.arccos(c)
    # d = d * 180 / np.pi
    d = np.degrees(d)
    print("Arccosine of above array:")
    print(d)
    print("-----------------------------------------")

######################################################
    c = np.tan(b)
    print("Tan of original array:")
    print(c)
    print("-----------------------------------------")

    d = np.arctan(c)
    #d = d * 180 / np.pi
    d = np.degrees(d)
    print("Arctan of above array:")
    print(d)
    print("-----------------------------------------")

def roundFunc():
    a = np.array([1.0, 5.55, 123, 0.567, 25.532])
    print('Original array:')
    print(a)
    print('--------------------------------------')

    print('After rounding:')
    print(np.around(a))
    print(np.around(a, decimals=1))
    print(np.around(a, decimals=-1))
    print('--------------------------------------')

    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print('Original array:')
    print(a)
    print('--------------------------------------')

    print('The floor modified array:')
    print(np.floor(a))  # The largest integer not greater than the input

    print('The ceil modified array:')
    print(np.ceil(a))  # The smallest integer greater than the input


#trigonometricalFunc()
roundFunc()
