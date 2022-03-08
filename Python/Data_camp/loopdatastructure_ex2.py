# Import numpy as np
import numpy as np

np_height = [74, 74, 72, 75, 75, 73]
np_baseball = [[ 74, 180],[ 74, 215],[ 72, 210],[ 75, 205],[ 75, 190],[ 73, 195]]

# For loop over np_height
for height in np_height :
    print(str(height) + " inches")

# For loop over np_baseball
for baseball in np.nditer(np_baseball) :
    print(baseball)