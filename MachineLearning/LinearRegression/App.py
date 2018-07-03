import numpy as num
from scipy import stats
from matplotlib import pyplot as plt

################ Linear Regression, y = ax + b ##################
# https://www.mathsisfun.com/data/least-squares-regression.html #
#################################################################
def linearRegression(x,y):
    Slope = None
    Intercept = None

    lenX = len(x)
    lenY = len(y)
    if lenX != lenY:
        print("Error. Training Data Array Length mismatched.")
        return (Slope, Intercept)  # Array Length Mismatch
    if lenX == 1:
        print("Error. Training Data Array Length must be more than one.")
        return (Slope, Intercept)  # Array Length Mismatch
    sigX = 0
    sigY = 0
    sigX2 = 0
    sigXY = 0
    for i in range(0, lenX, 1):
        sigX += x[i]
        sigY += y[i]
        sigX2 += x[i] * x[i]
        sigXY += x[i] * y[i]
    try:
        Slope = (lenX * sigXY - sigX * sigY) / (lenX * sigX2 - sigX * sigX)
        Intercept = (sigY - Slope * sigX ) / lenX
    except ValueError:
        print("Least Square Regression Error.")
        return (None, None)
    return (Slope, Intercept)
########################################################################################

################# Home Price Prediction #################
# Training Data:                                        #
#   x: Size of the house (Area, meter square)           #
#   y: Price (thousand dollars)                         #
#########################################################
def house_price_predict():
    x = num.array([112, 345, 198, 305, 372, 550, 302, 420, 578])
    y = num.array([1120, 1523, 2102, 2230, 2600, 3200, 3409, 3689, 4460])

    plt.plot(x, y, 'ro', color='black')
    plt.xlabel('Size of house')
    plt.ylabel('Price')

    slope, intercept, r_val, p_val, std_err = stats.linregress(x, y)
    plt.plot(x, x * slope + intercept, color='red')

    (m, b) = linearRegression(x, y)
    if m is not None:
        plt.plot(x, m * x + b, color='blue')

    plt.plot()
    plt.show()

    #PREDICTION
    newX = 150
    newY = newX * slope + intercept
    print(newY)
########################################################################################

################# Human Weight Prediction ###################
# Training Data:                                            #
#   x: Height (cm)                                          #
#   y: Weight (kg)                                          #
#############################################################
def human_weight_predict():
    x = num.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183])
    y = num.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

    plt.plot(x, y, 'ro', color='black')
    plt.axis([140, 190, 45, 75])
    plt.xlabel('Height(cm)')
    plt.ylabel('Weight(kg)')

    slope, intercept, r_val, p_val, std_err = stats.linregress(x, y)
    plt.plot(x, x * slope + intercept, color='red')

    (m, b) = linearRegression(x, y)
    if m is not None:
        plt.plot(x, m*x+b, color='blue')

    plt.plot()
    plt.show()

def human_weight_prediction():
    # Height
    X = num.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]).T

    print(X.shape)


########################################################################################

################ Main Function ################
#house_price_predict()
#human_weight_predict()
human_weight_prediction()