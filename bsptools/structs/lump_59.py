"""
Lump 59 - Map Flags
===================

This lump contains an array of :any:`flags_t`.
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
from bsptools.structs.common import *  # NOQA #402

flags_t = Struct('levelFlags' / Int32ul)


def lump_59(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_struct(LUMP_MAP_FLAGS, flags_t, header)
