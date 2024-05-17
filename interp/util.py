import numpy as np

def divided_difference(points, st, num):
    if num == 0:
        return points[st, 1]
    else:
        return (divided_difference(points, st+1, num - 1) - divided_difference(points, st, num - 1))/ (points[st+num, 0] - points[st, 0])

def truncated_power_function(X, m):
    return np.where(X > 0, X**m, 0.)

def b_spline(x, X, st, m):
    y = m*truncated_power_function(X - x, m-1)
    points = np.stack((X, y), axis = 1)
    return divided_difference(points, st, m)

def b_spline_normal(x, X, st, k):
    if x < X[st]:
        return 0.
    elif k == 1:
        return 1. if ((x >= X[st]) and (x < X[st+1])) else 0.
    else:
        return (X[st+k] - x)/(X[st+k] - X[st+1])*b_spline_normal(x, X, st+1, k-1) + \
                (x - X[st])/(X[st+k-1] - X[st])*b_spline_normal(x, X, st, k-1)

def n_spline(x, X, st, k):
    y = truncated_power_function(x-X, 2*k-1)
    points = np.stack((X, y), axis = 1)
    return divided_difference(points, st, k)