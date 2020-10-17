from poker import Range

from poker.hand import Combo

import holdem_calc
import holdem_functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display import display, HTML

hero_odds = []
hero_range_odds = []

# my hand = King of spades and Jack of clubs
hero_hand = Combo('KsJc')
print(hero_hand)