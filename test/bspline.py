import numpy as np
import interp
import pandas as pd

points = np.array([
    [-3., 7.],
    [-1., 11.],
    [0., 26.],
    [3., 56.],
    [4., 29.]
])

xi = np.array([-5., -4., -3., -1., 2., 4., 6., 7.])
base = interp.BSpline(points, xi)

x_test = np.linspace(-3., 4., 100)
y_test = base(x_test)

testdata = np.stack((x_test, y_test), axis = 1)
testdata = pd.DataFrame(testdata)
testdata.to_csv("test.csv")