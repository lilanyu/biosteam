# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:43:39 2019

@author: yoelr
"""
from . import Facility
import biosteam as bst

__all__ = ('ProcessWaterCenter',)

cost = bst.units.decorators.cost

@cost('Makeup water flow rate', 'Makeup water pump',
      CE=551, kW=20*0.7457, cost=6864, S=155564, n=0.8, BM=3.1)
@cost('Process water flow rate', 'Process water pump',
      CE=551, kW=75*0.7457, cost=15292, S=518924, n=0.8, BM=3.1)
@cost('Process water flow rate', 'Tank',
      CE=522, cost=250e3, S=451555, n=0.7, BM=1.7)
class ProcessWaterCenter(Facility):
    """
    Parameters
    ----------
    ins
        [0] Recycle water
        
        [1] Make-up water
        
    outs
        [0] Process water
    
    """
    _N_ins = 2
    _N_outs = 1
    _units = {'Makeup water flow rate': 'kg/hr',
              'Process water flow rate': 'kg/hr'}
    def __init__(self, ID='', ins=None, outs=(),):
        Facility.__init__(self, ID, ins, outs)
        
    def _run(self):
        s_recycle, s_makeup = self._ins
        s_process, = self.outs
        process_water = s_process.molnet
        recycle_water = s_recycle.molnet
        process_loss = process_water - recycle_water
        makeup_water = process_loss if process_loss > 0 else 0
        wi = s_makeup.index('7732-18-5')
        s_makeup.mol[wi] = makeup_water
        Design = self._Design
        Design['Process water flow rate'] = process_water * 18.015
        Design['Makeup water flow rate'] = makeup_water * 18.015
        
        