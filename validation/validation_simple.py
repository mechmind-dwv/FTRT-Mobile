import numpy as np

ftrt = np.array([2.31, 2.47, 1.21, 1.37, 2.58])
kp = np.array([9, 9, 6, 7, 9])

corr = np.corrcoef(ftrt, kp)[0,1]

print("Correlacion FTRT vs Kp:", round(corr, 3))
