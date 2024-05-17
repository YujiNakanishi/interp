import numpy as np
import interp
import sys

"""
class of Cubic spline interpolation which knots are same with points

Attributes:
    a, b, c, d -> <np:float:(N-1, )> params of each subregion
"""
class Spline_simple(interp.Base):
    def get_params(self):
        """
        calculate parameters (a, b, c, d) in each subregions
        """
        self.a = self.points[:-1,1]

        N = len(self.points)
        A = np.zeros((N, N)); b = np.zeros(N) # coeff matrix and source term for calc c
        A[0,0] = 1.; A[-1,-1] = 1. #B.C.

        delta_x = self.points[1:,0] - self.points[:-1,0]
        delta_y = self.points[1:,1] - self.points[:-1,1]
        for i in range(1, N-1):
            A[i,i-1] = delta_x[i-1]
            A[i,i] = 2.*(delta_x[i] + delta_x[i-1])
            A[i,i+1] = delta_x[i]

            b[i] = 3.*delta_y[i]/delta_x[i] - 3.*delta_y[i-1]/delta_x[i-1]
        
        self.c = np.linalg.solve(A, b)

        self.d = (self.c[1:] - self.c[:-1])/(3.*delta_x)
        self.b = delta_y/delta_x - delta_x*(self.c[1:] + 2.*self.c[:-1])/3.

        self.c = self.c[:-1]
    
    def __call__(self, X):
        Index = self.assign(X)

        a = self.a[Index, ]; b = self.b[Index, ]; c = self.c[Index, ]; d = self.d[Index, ]
        x = self.points[Index, 0]

        return a + b*(X - x) + c*(X - x)**2 + d*(X - x)**3


class BSpline(interp.Base):
    def __init__(self, points = None, xi = None, k = 3):
        self.xi = xi; self.k = k
        super().__init__(points)

    def get_params(self):
        n = len(self) # num of data
        A = np.zeros((n, n))
        s = self.points[:,1]

        for i in range(n):
            for j in range(n):
                A[i,j] = interp.util.b_spline_normal(self.points[i,0], self.xi, j, self.k)
        
        self.B = np.linalg.solve(A, s)
    
    def __call__(self, X):
        Y = []
        for x in X:
            y = np.sum([self.B[i]*interp.util.b_spline_normal(x, self.xi, i, self.k) for i in range(len(self.B))])
            Y.append(y)
        
        return np.array(Y)