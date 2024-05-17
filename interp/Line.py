import interp

"""
class of linear interpolation

Attributes:
    a, b -> <np:float:(N-1, )> params of each subregion
"""
class Line(interp.Base):
    def get_params(self):
        self.b = (self.points[1:,1] - self.points[:-1,1]) / (self.points[1:,0] - self.points[:-1,0])
        self.a = self.points[:-1,0]

    
    def __call__(self, X):
        """
        Interpolation
        Input: X -> <np:float:(N, )> inputs
        Output: <np:float:(N, )> interpolated values
        """
        Index = self.assign(X)

        a = self.a[Index,]
        b = self.b[Index,]
        x = self.points[Index, 0]

        return a + b*(X - x)