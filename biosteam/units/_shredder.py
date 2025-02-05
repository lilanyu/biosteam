# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:57:12 2019

@author: yoelr
"""
from .. import Unit
from .decorators import cost
from ._static import Static

@cost('Flow rate', units='kg/hr', cost=2.5e6,
      CE=567.3, n=0.6, S=500e3, kW=3000, BM=1.39)
class Shredder(Static):  pass