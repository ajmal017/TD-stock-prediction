import numpy as np
import pandas as pd
import random

class Evaluate:
  @staticmethod
  def evaluate(predicted_open_price, close_price_prev):
    # Need to make it more likely to sell
    if (random.random() < 0.15):
      return 'SELL', 0.8
    
    if (predicted_open_price > close_price_prev * 1.2):
      # Price increased, return 'BUY'
      frac = 1.0 - (close_price_prev/predicted_open_price) # 2/10 # 1 -.2
      if (frac > 1):
        frac = 1.0
      elif (frac < 0):
        frac = 0.01
      return 'BUY', frac[0][0]
    elif (predicted_open_price < close_price_prev):
      frac = 1 - (close_price_prev/predicted_open_price) # 10 -> 2  2/10=1 -.2
      if (frac > 1):
        frac = 1.0
      elif (frac <= 0):
        frac = 0.01
      return 'SELL', frac
    else:
      return 'HOLD', 0.0

