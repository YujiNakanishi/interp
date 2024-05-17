import interp

class Lagrange(interp.Base):
    def poly(self, i, x):
        N = len(self)
        
        P = 1.
        for j in range(N):
            if j != i:
                P *= (x - self.points[j, 0])
        
        return P
    
    def get_params(self):
        self.p = [self.points[i, 1]/self.poly(i, self.points[i, 0]) for i in range(len(self))]
    
    def __call__(self, X):
        L = 0.
        for i in range(len(self)):
            L += self.poly(i, X)*self.p[i]
        
        return L