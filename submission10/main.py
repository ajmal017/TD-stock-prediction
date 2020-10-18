import sys
import numpy as np
import keras
from evaluate import Evaluate


# Initialize model
model = keras.models.load_model("model1")
val_arr = [] # Keep list of past 30 values

i = 0
for line in sys.stdin:
  row = line.split(',')
  row = np.array([float(x.strip()) for x in row])
  val = row[3] # Grab open value from previous day
  val_arr.append(val) # Append to end for now...
  if (len(val_arr) > 30):
    del val_arr[0] # Delete first element if have > 30 elements

  
  if (i < 30):
    print("HOLD", 0)
  else:
    x_input = np.array(val_arr)
    x_input = np.reshape(x_input, (-1, x_input.shape[0], 1))
    predicted_price = model.predict(x_input)
    choice, frac = Evaluate.evaluate(predicted_price, row[3]) # Send predicted price and prev close price
    print(choice, frac) # ('HOLD', 0.5)
  
  i += 1

