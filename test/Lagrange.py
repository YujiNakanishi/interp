import numpy as np
import interp
import pandas as pd

N = 20

x = np.linspace(0., 4.*np.pi, N)
y = np.sin(x)
points = np.stack((x, y), axis = 1)
base = interp.Lagrange(points)


x_test = 2.*np.pi*np.random.rand(100)
y_test = base(x_test)

testdata = np.stack((x_test, y_test), axis = 1)
testdata = pd.DataFrame(testdata)
testdata.to_csv("test.csv")