# Example
from model import DINEOF3

fpath = "E:\\data\\satellite\\OLCI\\L2b_SPM\\"

# Some 3D numpy tensor with shape [number of points, 3], 
# where 2nd dimension is coordinates (e.g. latitude, longitude, day)
X_train = [numberofpoints, 3]
# 1D numpy array with values of some investigated object. Has shape: [number of points].
y_train = [numberofpoints]

# Some test data
X_test = ...
y_test = ...

# DINEOF3 models inherits from the sklearn BaseEstimator, 
# so you may use it inside Grid Search routines etc.
d = DINEOF3(...)

d.fit(X, y)

y_pred = d.predict(X_test)  # Get predictions
score = d.score(X_test, y_test)  # Calculate score
