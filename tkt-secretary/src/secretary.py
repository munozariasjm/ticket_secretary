
import numpy as np
import pandas as pd
from datetime import datetime
from typing import List

class SecretarySolver:
    def __init__(self, prices: List[int], dates: List[datetime]):

        self.prices = prices
        self.dates = dates
        self.dates_prices = pd.DataFrame({'date': dates, 'price': prices})

    def find_best_history(self):
        """
        Find the best value in the list of prices
        """
        return max(self.prices), self.dates[self.prices.index(max(self.prices))]



    def find_optimal_date(self):
        # Implement secretary problem solution
        return optimal_date
