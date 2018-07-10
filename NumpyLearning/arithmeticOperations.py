import numpy as np

# Test numpy add, subtract, multiply and divide
def arithmeticFunc():
    a = np.arange(0, 9, 1, dtype=float)
    a = a.reshape(3,3)
    print("First Array a:")
    print(a)

    b = np.array([10, 100, 1000]).reshape(3,1)

    print("Second Array b:")
    print(b)

    c = np.add(a, b)
    print("Add:")
    print(c)
    print("----------------------------")

    c = np.subtract(a, b)
    print("Subtract:")
    print(c)
    print("----------------------------")

    c = np.multiply(a, b)
    print("Multiply:")
    print(c)
    print("----------------------------")

    c = np.divide(a, b)
    print("Divide:")
    print(c)
    print("----------------------------")

# Test function numpy reciprocal (1/x)
def reciprocalFunc():
    a = np.array([1, 10, 100])
    print("Original array:")
    print(a)

    b = np.reciprocal(a)
    print("After Reciprocal (Integer):")
    print(b)

    print('-------------------------------------------')

    a = np.arange(1, 10, 1, dtype=float).reshape(3,3)
    print("Original array:")
    print(a)

    b = np.reciprocal(a)
    print("After Reciprocal (Integer):")
    print(b)

def powerFunc():
    a = np.arange(1, 10, 1, dtype=float).reshape(3, 3)
    print("Original array:")
    print(a)

    b = np.array([1,2,3]).reshape(3,1)
    c = np.power(a, b)
    print("After Power:")
    print(c)

def modFunc():
    a = np.arange(91, 100, 1, dtype=np.int).reshape(3, 3)
    print("Original array:")
    print(a)

    b = np.array([3, 5, 7]).reshape(3, 1)
    c = np.mod(a, b)
    print("After Mod:")
    print(c)

def complexFunc():
    a = np.array([-1+2j, 0.5, -5.6j, 1 + 1j]).reshape(4,1)
    print("Original array:")
    print(a)

    b = np.real(a)
    print("Real:")
    print(b)

    b = np.imag(a)
    print("Imagine:")
    print(b)

    b = np.angle(a)
    b = np.degrees(b)
    print("Angle:")
    print(b)

    b = np.absolute(a)
    print("Absolute:")
    print(b)

    b = np.conjugate(a)
    print("Conjugate:")
    print(b)

####################################################

#arithmeticFunc()
#reciprocalFunc()
#powerFunc()
#modFunc()
complexFunc()