"""
Lump 62 - Phys Level
====================

This lump is not currently implemented. It will return the raw bytes.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common import *  # NOQA #402


def lump_62(header, profile=None):
    if header.filelen == 0:
        return lump_dud(LUMP_PHYSLEVEL, header)
    elif header.version == 0:
        return lump_bytes(LUMP_PHYSLEVEL, header)
    else:
        raise LumpVersionUnsupportedError(header.version)
