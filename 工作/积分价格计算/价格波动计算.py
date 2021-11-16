import pandas as pd
import numpy as np

values = [1,2,3]

frequency = [3,4,2]

df = pd.DataFrame(np.repeat(values, frequency), columns=['data'])

df.mean()

