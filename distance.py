def solve(r1, r2):
    
     x, y = sorted((r1, r2))
     if x[0] <= x[1] < y[0] and all( y[0] <= y[1] for y in (r1,r2)):
        return y[0] - x[1]
     return 0
 
