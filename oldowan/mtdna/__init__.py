"""This is the oldowan.mtdna package."""

import os
version_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION'))
version = version_file.read().strip()
version_file.close()

__all__ = ['rCRS', 
           'rCRSplus',
           'rCRSplus_positions',
           'rCRSlist']

try:
    from oldowan.mtdna.rCRS import rCRS
    from oldowan.mtdna.rCRS import rCRSlist
    from oldowan.mtdna.rCRS import rCRSplus
    from oldowan.mtdna.rCRS import rCRSplus_positions
    from oldowan.mtdna.rCRS import HVR1_indices
    from oldowan.mtdna.rCRS import HVR2_indices
    from oldowan.mtdna.rCRS import HVR1and2_indices
    from oldowan.mtdna.rCRS import HVR1to2_indices
    from oldowan.mtdna.rCRS import coding_indices
    from oldowan.mtdna.rCRS import all_indices
except:
    from rCRS import rCRS
    from rCRS import rCRSlist
    from rCRS import rCRSplus
    from rCRS import rCRSplus_positions
    from rCRS import HVR1_indices
    from rCRS import HVR2_indices
    from rCRS import HVR1and2_indices
    from rCRS import HVR1to2_indices
    from rCRS import coding_indices
    from rCRS import all_indices
