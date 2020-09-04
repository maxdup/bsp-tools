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

DetailPropLightStyleLump_t = Struct(
    'm_Lighting' / ColorRGBExp32,
    'm_Style' / Int8ul,
)

DetailPropLightStylesLump_t = Struct(
    'count' / Int32sl,
    'styles' / DetailPropLightStyleLump_t[this.count]
)


def lump_tlpd(version):
    if version != 0:
        raise LumpVersionUnsupportedError(version)

    return lump_game('tlpd', DetailPropLightStylesLump_t)