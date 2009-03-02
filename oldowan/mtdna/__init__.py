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
except:
    from rCRS import rCRS
    from rCRS import rCRSlist
    from rCRS import rCRSplus
    from rCRS import rCRSplus_positions
