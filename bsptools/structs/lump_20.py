"""
Lump 20 - Areas
===============

This lump contains an array of :any:`darea_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common import *  # NOQA: #402

darea_t = Struct(
    'numAreaPortals' / Int32sl,
    'firstAreaPortal' / Int32sl
)


def lump_20(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_AREAS, darea_t, header)
