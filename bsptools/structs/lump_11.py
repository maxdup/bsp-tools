from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA: #402

dfaceid_t = Struct(
    'hammerfaceid' / Int16ul
)


def lump_11(version):
    if version != 0:
        raise LumpVersionUnsupportedError(version)
    return lump_array(LUMP_FACEIDS, dfaceid_t)