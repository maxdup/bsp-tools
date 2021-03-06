"""
Lump 43 - Texture Data String Data
==================================
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common import *  # NOQA: #402


def lump_43(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return Pointer(header.lump_t[LUMP_TEXDATA_STRING_DATA].fileofs,
                   RepeatUntil(lambda x, lst, ctx: len(lst) >=
                               header.lump_t[LUMP_TEXDATA_STRING_TABLE].filelen // Int32sl.sizeof(), CString("ascii")))
