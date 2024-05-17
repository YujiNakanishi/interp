import numpy as np

"""
Base class

Attributes:
    points -> <np:float:(N, 2)> set of (x_i, y_i), where i in [1, N]
    x_min(max) -> <float> min(max) of x

Note:
    (1) points should be sorted by x (x_i < x_{i+1}).
    (2) x_i should be unique (x_i != x_j)
"""
class Base:
    def __init__(self, points = None):
        if points is None:
            self.x_max = None; self.x_min = None
            self.points = None
        else:
            self.reset(points)
    
    def __len__(self):
        return 0 if self.points is None else len(self.points)
    
    def is_interp(self, X):
        """
        check X is in.
        Input: X -> <np:float:(N, )> N points
        Output: <np:bool:(N, )>
        """
        return (X >= self.x_min) * (X <= self.x_max)
    
    def assign(self, X):
        """
        assign the region
        Input: X -> <np:float:(N, )> N points
        Output: Index -> <tuple:int:(N, )> if X[i] \in {x[j], x[j+1]}, Index[i] == j
        """
        assert np.all(self.is_interp(X))
        Index = []
        for x in X:
            for idx, px in enumerate(self.points[:,0]):
                if x < px:
                    Index.append(idx-1)
                    break
        
        return tuple(Index)
    
    def sort_by_x(self, points):
        idx = np.argsort(points[:,0])
        return points[idx]

    def reset(self, points):
        """
        reset points
        * sort points by x
        * check whether points are unique or not
        * get x_min and x_max 
        """
        x_unique = np.unique(points[:,0])
        assert len(x_unique) == len(points)

        sorted_points = self.sort_by_x(points)
        self.x_min, self.x_max, self.points = sorted_points[0,0], sorted_points[-1, 0], sorted_points
        self.get_params()
    
    def add_points(self, new_points):
        new_points = np.concatenate((self.points, new_points.reshape((-1, 2))))
        self.reset(new_points)
    
    def remove_points(self, idx):
        points = np.delete(self.points, idx, axis = 0)
        self.reset(points)
    
    def get_params(self):
        pass

from interp import util
from interp.Line import Line
from interp.Spline import Spline_simple, BSpline
from interp.Lagrange import Lagrange