#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
 pySEIMS
                             Python APIs for SEIMS
 Utility functions and classes of pySEIMS
                              -------------------
        author               : Liangjun Zhu
        copyright            : (C) 2018 by Lreis, IGSNRR, CAS
        email                : zlj@lreis.ac.cn
 ******************************************************************************
 *                                                                            *
 *   SEIMS is distributed for Research and/or Education only, any commercial  *
 *   purpose will be FORBIDDEN. SEIMS is an open-source project, but without  *
 *   ANY WARRANTY, WITHOUT even the implied warranty of MERCHANTABILITY or    *
 *   FITNESS for A PARTICULAR PURPOSE.                                        *
 *   See the GNU General Public License for more details.                     *
 *                                                                            *
 ******************************************************************************/
"""
__author__ = "SEIMS Team"
__version__ = "1.0"
__revision__ = "1.0.0"

# Global variables
UTIL_ZERO = 1.e-6
MINI_SLOPE = 0.0001
DEFAULT_NODATA = -9999.
SQ2 = 1.4142135623730951
PI = 3.141592653589793

from utility.io_plain_text import *
from utility.parse_config import *
from utility.timeseries_data import *
from utility.plot import *

