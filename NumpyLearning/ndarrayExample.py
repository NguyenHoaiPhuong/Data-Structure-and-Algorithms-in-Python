import numpy as np

# Constructed by Different Methods

###################################################
#       1. Constructed by an python object        #
###################################################
def arrayConstructedbyPythonObject():
    STR = ""

    print("****************** 1 ******************")

    # List
    L = [1, 2, 3]
    STR = "List: " + str(L)
    print(STR)
    a = np.array(L)
    STR = "Array: " + str(a)
    print(STR)

    print("****************** 2 ******************")

    # Tuple
    T = (1, "Akagi", 3)
    STR = "Tuple: " + str(T)
    print(STR)
    a = np.array(T)
    STR = "Array: " + str(a)
    print(STR)

    print("****************** 3 ******************")

    # Matrix constructed by 2 list
    LL = [ [1, 2], [3, 4] ]
    STR = "Double Lists: " + str(LL)
    print(STR)
    a = np.array(LL)
    STR = "Array: " + str(a)
    print(STR)

    print("****************** 4 ******************")

    # Matrix constructed by 2 arrays
    L1 = [1, 2]
    a1 = np.array(L1)
    L2 = [3, 4]
    a2 = np.array(L2)
    a = np.array([a1, a2])
    STR = "Array: " + str(a)
    print(STR)


###################################################
#       2. Constructed by an python object        #
#       plus (+) minimum dimensions               #
###################################################
def arrayConstructedbyPythonObjectPlusMinDim():
    a = np.array([1, 2, 3, 4])
    STR = "Array: " + str(a)
    print(STR)


###################################################
#       3. Constructed by an python object        #
#       plus (+) desired type                     #
###################################################
def arrayConstructedbyPythonObjectPlusDType():
    a = np.array( [1, 2, 3, 4], dtype=complex )
    STR = "Complex Array: " + str(a)
    print(STR)

    a = np.array([1, 2, 3, 4], dtype=float)
    STR = "Float Array: " + str(a)
    print(STR)

    a = np.array([1, 2, 3, 4], dtype=int)
    STR = "Integer Array: " + str(a)
    print(STR)

    a = np.array([1, 2, 3, 4], dtype=str)
    STR = "String Array: " + str(a)
    print(STR)

# arrayConstructedbyPythonObject()
# arrayConstructedbyPythonObjectPlusMinDim()
arrayConstructedbyPythonObjectPlusDType()