from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from builtins import int
from future import standard_library
standard_library.install_aliases()


from construct import *	 # NOQA: #402
from .constants import *  # NOQA: #402
from .common_struct import *  # NOQA: #402

lump_t = Struct(
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
    'version' / Int32sl,
    'uncompressedSize' / Int32sl
)

dplane_t = Struct(
    'normal' / Vector,
    'dist' / Float32l,
    'type' / Int32sl
)

dtexdata_t = Struct(
    'reflectivity' / Vector,  # RGB reflectivity
    'nameStringTableID' / Int32sl,  # index into TexdataStringTable
    'width' / Int32sl,
    'height' / Int32sl,
    'view_width' / Int32sl,
    'view_height' / Int32sl
)

dvis_t = Struct(
    'numclusters' / Int32sl,
    'bitofs' / Int32sl[8][2]
)

dnode_t = Struct(
    'planenum' / Int32sl,
    'children' / Int32sl[2],
    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],
    'firstface' / Int16ul,
    'numfaces' / Int16ul,
    'area' / Int16sl,
    'padding' / Int16sl,
)

texinfo_t = Struct(
    'textureVecsTexelsPerWorldUnits' / Float32l[2][4],
    'lightmapVecsLuxelsPerWorldUnits' / Float32l[2][4],
    'flags' / Int32sl,
    'texdata' / Int32sl,
)

dface_t = Struct(
    'planenum' / Int16ul,
    'side' / Byte,
    'onNode' / Byte,
    'firstedge' / Int32sl,
    'numedges' / Int16sl,
    'texinfo' / Int16sl,
    'dispinfo' / Int16sl,
    'surfaceFogVolumeID' / Int16sl,
    'styles' / Byte[4],
    'lightofs' / Int32sl,
    'area' / Float32l,
    'LightmapTextureMinsInLuxels' / Int32sl[2],
    'LightmapTextureSizeInLuxels' / Int32sl[2],
    'origFace' / Int32sl,
    'numPrims' / Int16ul,
    'firstPrimID' / Int16ul,
    'smoothingGroups' / Int32ul,
)

ColorRGBExp32 = Struct(
    'r' / Byte,
    'g' / Byte,
    'b' / Byte,
    'exponent' / Byte
)

CompressedLightCube = Struct(
    'm_color' / ColorRGBExp32[6]
)

doccluderdata_t = Struct(
    'flags' / Int32sl,
    'firstpoly' / Int32sl,
    'polycount' / Int32sl,
    'mins' / Vector,
    'maxs' / Vector,
    'area' / Int32sl,
)

doccluderpolydata_t = Struct(
    'firstvertexindex' / Int32sl,
    'vertexcount' / Int32sl,
    'planenum' / Int32sl,
)

doccluder_t = Struct(
    'count' / Int32sl,
    'data' / doccluderdata_t[this.count],
    'polyDataCount' / Int32sl,
    'polyData' / doccluderpolydata_t[this.polyDataCount],
    'vertexIndexCount' / Int32sl,
    'vertexIndices' / Int32sl[this.vertexIndexCount],
)

dfaceid_t = Struct(
    'hammerfaceid' / Int16ul
)

dedge_t = Struct(
    'v' / Int16ul[2]
)

emittype_t = Enum(
    Int32sl,
    emit_surface=0,
    emit_point=1,
    emit_spotlight=2,
    emit_skylight=3,
    emit_quakelight=4,
    emit_skyambient=5
)

dworldlight_t = Struct(
    'origin' / Vector,
    'intensity' / Vector,
    'normal' / Vector,
    'cluster' / Int32sl,
    'type' / emittype_t,
    'style' / Int32sl,
    'stopdot' / Float32l,
    'stopdot2' / Float32l,
    'exponent' / Float32l,
    'radius' / Float32l,
    'constant_attn' / Float32l,
    'linear_attn' / Float32l,
    'quadratic_attn' / Float32l,
    'flags' / Int32sl,
    'texinfo' / Int32sl,  # lump 2
    'owner' / Int32sl,  # lump 0
)

dbrush_t = Struct(
    'firstside' / Int32sl,
    'numsides' / Int32sl,
    'contents' / Int32sl,
)

dbrushside_t = Struct(
    'planenum' / Int32ul,
    'texinfo' / Int32sl,
    'dispinfo' / Int32sl,
    'bevel' / Int32sl
)

darea_t = Struct(
    'numareaportals' / Int32sl,
    'firstareaportal' / Int32sl
)

dareaportal_t = Struct(
    'm_PortalKey' / Int16ul,
    'otherarea' / Int16ul,
    'm_FirstClipPortalVert' / Int16ul,
    'm_nClipPortalVerts' / Int16ul,
    'planenum' / Int32sl
)

dleaf_t = Struct(
    'contents' / Int32sl,
    'cluster' / Int16sl,

    'area' / Int16sl,
    'flags' / Int16sl,

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],

    'firstleafface' / Int16ul,
    'numleaffaces' / Int16ul,

    'firstleafbrush' / Int16ul,
    'numleafbrushes' / Int16ul,
    'leafWaterDataID' / Int16sl
)

dleafambientlighting_t = Struct(
    'cube' / CompressedLightCube,
    'x' / Byte,
    'y' / Byte,
    'z' / Byte,
    'pad' / Byte
)

dleafambientindex_t = Struct(  # matches dleaf_t
    'ambientSampleCount' / Int16ul,
    'firstAmbientSample' / Int16ul
)

dleafwaterdata_t = Struct(
    'surfaceZ' / Float32l,
    'minZ' / Float32l,
    'surfaceTexInfoID' / Int16sl,
)

dcubemapsample_t = Struct(
    'origin' / Int32sl[3],
    'size' / Int32sl
)

dflagslump_t = Struct(
    'mLevelFalgs' / Int32ul,
)

doverlay_t = Struct(
    'nId' / Int32sl,
    'nTexInfo' / Int16sl,
    'm_nFaceCountAndRenderOrder' / Int16ul,
    'aFaces' / Int32sl[OVERLAY_BSP_FACE_COUNT],
    'flU' / Float32l[2],
    'flV' / Float32l[2],
    'vecUVPoints' / Vector[4],
    'vecOrigin' / Vector,
    'vecBasisNormal' / Vector
)

dwateroverlay_t = Struct(
    'nId' / Int32sl,
    'nTexInfo' / Int16sl,
    'm_nFaceCountAndRenderOrder' / Int16ul,
    'aFaces' / Int32sl[OVERLAY_BSP_FACE_COUNT],
    'flU' / Float32l[2],
    'flV' / Float32l[2],
    'vecUVPoints' / Vector[4],
    'vecOrigin' / Vector,
    'vecBasisNormal' / Vector
)

doverlayfade_t = Struct(
    'flFadeDistMinSq' / Float32l,
    'flFadeDistMaxSq' / Float32l
)

NeighborSpan = Enum(
    Int8sl,
    CORNER_TO_CORNER=0,
    CORNER_TO_MIDPOINT=1,
    MIDPOINT_TO_CORNER=2
)

NeighborOrientation = Enum(
    Int8sl,
    ORIENTATION_CCW_0=0,
    ORIENTATION_CCW_90=1,
    ORIENTATION_CCW_180=2,
    ORIENTATION_CCW_270=3
)


CDispSubNeighbor = Struct(
    # 'm_iNeighbor' / Int16ul,
    # 'm_NeighborOrientation' / NeighborOrientation,
    # 'm_Span' / NeighborSpan,
    # 'm_NeighborSpan' / NeighborSpan
    # The fields seem to be misordered, this is my best guess
    'm_Span' / NeighborSpan,
    'm_NeighborSpan' / NeighborSpan,
    'm_iNeighbor' / Int16ul,
    'padding' / Padding(1),
    'm_NeighborOrientation' / NeighborOrientation,
)

CDispNeighbor = Struct(
    'm_SubNeighbors' / CDispSubNeighbor[2],
)

CDispCornerNeighbors = Struct(
    'm_Neighbors' / Int16ul[MAX_DISP_CORNER_NEIGHBORS],
    'm_nNeighbors' / Int8ul
)

ddispinfo_t = Struct(
    'startPosition' / Vector,
    'm_iDispVertStart' / Int32sl,
    'm_iDispTriStart'/Int32sl,

    'power' / Int32sl,
    'minTess'/Int32sl,
    'smoothingAngle' / Float32l,
    'contents'/Int32sl,

    'm_iMapFace' / Int16ul,

    'm_iLightmapAlphaStart' / Int32sl,
    'm_iLightmapSamplePositionStart' / Int32sl,

    'm_EdgeNeighbors' / CDispNeighbor[4],
    'm_CornerNeighbors' / CDispCornerNeighbors[4],

    Padding(6),

    'm_AllowedVerts' / Int32ul[ALLOWEDVERTS_SIZE],
)

CDispVert = Struct(
    'm_vVector' / Vector,
    'm_flDist' / Float32l,
    'm_flAlpha' / Float32l,
)

CDispTri = Struct(
    'm_uiTags' / Int16ul
)


dprimitive_type = Enum(
    Int8ul,
    PRIM_TRILIST=0,
    PRIM_TRISTRIP=1,
)

dprimitive_t = Struct(
    'type' / dprimitive_type,
    'firstIndex' / Int16ul,
    'indexCount' / Int16ul,
    'firstVert' / Int16ul,
    'vertCount' / Int16ul,
    Padding(1)
)

dprimvert_t = Struct(
    'pos' / Vector
)

dgamelump_t = Struct(
    'id' / PaddedString(4, "ascii"),
    'flags' / Int16ul,
    'version' / Int16ul,
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
)

dgamelumpheader_t = Struct(
    'lumpCount' / Int32sl,
    'gamelump' / dgamelump_t[this.lumpCount],
)

StaticPropV6_t = Struct(
    'm_Origin' / Vector,
    'm_Angles' / QAngle,

    'm_PropType' / Int16ul,
    'm_FirstLeaf' / Int16ul,
    'm_LeafCount' / Int16ul,
    'm_Solid' / Int8ul,
    'm_Flags' / Int32ul,
    'm_Skin' / Int32sl,

    'm_FadeMinDist' / Float32l,
    'm_FadeMaxDist' / Float32l,
    'm_LightingOrigin' / Vector,


    'm_nMinDXLevel' / Int16ul,
    'm_nMaxDXLevel' / Int16ul,
    Padding(1),

    #'m_Lighting' / Int32sl,
)

StaticPropV10_t = Struct(
    'Origin' / Vector,
    'Angles' / QAngle,

    'PropType' / Int16ul,
    'FirstLeaf' / Int16ul,
    'LeafCount' / Int16ul,
    'Solid' / Int8ul,
    'Flags' / Int32ul,
    'Skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,
    'LightingOrigin' / Vector,

    # v5+
    'ForcedFadeScale' / Float32l,

    # v6 only
    #'m_nMinDXLevel' / Int16ul,
    #'m_nMaxDXLevel' / Int16ul,

    'MinCPULevel' / Int8ul,
    'MaxCPULevel' / Int8ul,
    'MinGPULevel' / Int8ul,
    'MaxGPULevel' / Int8ul,

    # v7
    'DiffuseModulation' / color32,

    # v9-10
    'DisableX360' / Flag,
)

StaticPropDictLump_t = Struct(
    'count' / Int32sl,
    'names' / PaddedString(STATIC_PROP_NAME_LENGTH, 'ascii')[this.count]
)
StaticPropLeafDictLump_t = Struct(
    'count' / Int32sl,
    'leafs' / Int16ul[this.count]
)
StaticPropObjectDictLump_t = Struct(
    'count' / Int32sl,
    'object' / StaticPropV10_t[this.count]
)
StaticPropLightstylesDictLump_t = Struct(
    'count' / Int32sl,
    'lightstyles' / ColorRGBExp32[this.count]
)

StaticPropLump_t = Struct(
    'dict_lump' / StaticPropDictLump_t,
    'leaf_lump' / StaticPropLeafDictLump_t,
    'object_lump' / StaticPropObjectDictLump_t,
    'lightstyles_lump' / StaticPropLightstylesDictLump_t
)

DetailPropOrientation_t = Enum(
    Int8ul,
    DETAIL_PROP_ORIENT_NORMAL=0,
    DETAIL_PROP_ORIENT_SCREEN_ALIGNED=1,
    DETAIL_PROP_ORIENT_SCREEN_ALIGNED_VERTICAL=2,
)

DetailPropType_t = Enum(
    Int8ul,
    DETAIL_PROP_TYPE_MODEL=0,
    DETAIL_PROP_TYPE_SPRITE=1,
    DETAIL_PROP_TYPE_SHAPE_CROSS=2,
    DETAIL_PROP_TYPE_SHAPE_TRI=3,
)

DetailSpriteLump_t = Struct(
    'm_UL' / Vector2D,
    'm_LR' / Vector2D,
    'm_TexUL' / Vector2D,
    'm_TexLR' / Vector2D,
)
DetailObjectLump_t = Struct(
    'm_Origin' / Vector,
    'm_Angles' / QAngle,
    'm_DetailModel' / Int16ul,
    'm_Leaf' / Int16ul,
    'm_Lighting' / ColorRGBExp32,
    'm_LightStyles' / Int32sl,
    'm_LightStyleCount' / Int8ul,
    'm_SwayAmount' / Int8ul,
    'm_ShapeAngle' / Int8ul,
    'm_ShapeSize' / Int8ul,
    'm_Orientation' / DetailPropOrientation_t,
    'm_Padding2' / Int8ul[3],
    'm_Type' / DetailPropType_t,
    'm_Padding3' / Int8ul[3],
    'm_flScale' / Float32l
)

DetailPropDictLump_t = Struct(
    'count' / Int32sl,
    'names' / PaddedString(DETAIL_NAME_LENGTH, 'ascii')[this.count]
)
DetailSpriteDictLump_t = Struct(
    'count' / Int32sl,
    'sprites' / DetailSpriteLump_t[this.count]
)
DetailObjectDictLump_t = Struct(
    'count' / Int32sl,
    'objects' / DetailObjectLump_t[this.count]
)

DetailPropLump_t = Struct(
    'dict_lump' / DetailPropDictLump_t,
    'sprites_lump' / DetailSpriteDictLump_t,
    'objects_lump' / DetailObjectDictLump_t,
)


DetailPropLightStyleLump_t = Struct(
    'm_Lighting' / ColorRGBExp32,
    'm_Style' / Int8ul,
)
DetailPropLightStylesLump_t = Struct(
    'count' / Int32sl,
    'styles' / DetailPropLightStyleLump_t[this.count]
)


bsp_t = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'lump_t' / lump_t[HEADER_LUMPS],
    'mapRevision' / Int32sl,

    # 0 Entities
    'lump_0' / Lazy(Pointer(this.lump_t[0].fileofs, CString("ascii"))),

    # 1 Planes
    'lump_1' / Lazy(Pointer(this.lump_t[1].fileofs,
                            dplane_t[this.lump_t[1].filelen // dplane_t.sizeof()])),
    # 2 Texture Data
    'lump_2' / Lazy(Pointer(this.lump_t[2].fileofs,
                            dtexdata_t[this.lump_t[2].filelen // dtexdata_t.sizeof()])),
    # 3 Vertexes
    'lump_3' / Lazy(Pointer(this.lump_t[3].fileofs,
                            Vector[this.lump_t[3].filelen // Vector.sizeof()])),
    # 4 Visibility
    # 'lump_4' / TODO

    # 5 Nodes
    'lump_5' / Lazy(Pointer(this.lump_t[5].fileofs,
                            dnode_t[this.lump_t[5].filelen // dnode_t.sizeof()])),
    # 6 Texture Info
    'lump_6' / Lazy(Pointer(this.lump_t[6].fileofs,
                            texinfo_t[this.lump_t[6].filelen // texinfo_t.sizeof()])),
    # 7 Faces
    'lump_7' / Lazy(Pointer(this.lump_t[7].fileofs,
                            dface_t[this.lump_t[7].filelen // dface_t.sizeof()])),
    # 8 Lightmaps
    'lump_8' / Lazy(Pointer(this.lump_t[8].fileofs,
                            ColorRGBExp32[this.lump_t[8].filelen // ColorRGBExp32.sizeof()])),
    # 9 Occlusion
    'lump_9' / Lazy(Pointer(this.lump_t[9].fileofs, doccluder_t)),

    # 10 leafs
    'lump_10' / Lazy(Pointer(this.lump_t[10].fileofs,
                             dleaf_t[this.lump_t[10].filelen // dleaf_t.sizeof()])),
    # 11 FaceIds
    'lump_11' / Lazy(Pointer(this.lump_t[11].fileofs,
                             dfaceid_t[this.lump_t[11].filelen // dfaceid_t.sizeof()])),
    # 12 Edges
    'lump_12' / Lazy(Pointer(this.lump_t[12].fileofs,
                             dedge_t[this.lump_t[12].filelen // dedge_t.sizeof()])),
    # 13 Surfedges
    'lump_13' / Lazy(Pointer(this.lump_t[13].fileofs,
                             Int32sl[this.lump_t[13].filelen // Int32sl.sizeof()])),
    # 14 Models
    'lump_14' / Lazy(Pointer(this.lump_t[14].fileofs,
                             Int32sl[this.lump_t[14].filelen // Int32sl.sizeof()])),
    # 15 Worldlights
    'lump_15' / Lazy(Pointer(this.lump_t[15].fileofs,
                             dworldlight_t[this.lump_t[15].filelen // dworldlight_t.sizeof()])),
    # 16 Leaf Faces
    'lump_16' / Lazy(Pointer(this.lump_t[16].fileofs,
                             Int16ul[this.lump_t[16].filelen // Int16ul.sizeof()])),
    # 17 Leaf Brushes
    'lump_17' / Lazy(Pointer(this.lump_t[17].fileofs,
                             Int16ul[this.lump_t[17].filelen // Int16ul.sizeof()])),
    # 18 Brushes
    'lump_18' / Lazy(Pointer(this.lump_t[18].fileofs,
                             dbrush_t[this.lump_t[18].filelen // dbrush_t.sizeof()])),
    # 19 Brush Sides
    'lump_19' / Lazy(Pointer(this.lump_t[19].fileofs,
                             dbrushside_t[this.lump_t[19].filelen // dbrushside_t.sizeof()])),
    # 20 Areas
    'lump_20' / Lazy(Pointer(this.lump_t[20].fileofs,
                             darea_t[this.lump_t[20].filelen // darea_t.sizeof()])),
    # 21 Areaportals
    'lump_21' / Lazy(Pointer(this.lump_t[21].fileofs,
                             dareaportal_t[this.lump_t[21].filelen // dareaportal_t.sizeof()])),
    # 22 unused
    # 23 unused
    # 24 unused
    # 25 unused
    # 26 Disp Info
    'lump_26' / Lazy(Pointer(this.lump_t[26].fileofs,
                             ddispinfo_t[this.lump_t[26].filelen // ddispinfo_t.sizeof()])),
    # 27 Original Faces
    'lump_27' / Lazy(Pointer(this.lump_t[27].fileofs,
                             dface_t[this.lump_t[27].filelen // dface_t.sizeof()])),
    # 28 Phys Disp
    'lump_28' / Lazy(Pointer(this.lump_t[28].fileofs,
                             Byte[this.lump_t[28].filelen // Byte.sizeof()])),
    # 29 Phys Collide
    'lump_29' / Lazy(Pointer(this.lump_t[29].fileofs,
                             Byte[this.lump_t[29].filelen // Byte.sizeof()])),
    # 30 Vert Normals
    'lump_30' / Lazy(Pointer(this.lump_t[30].fileofs,
                             Vector[this.lump_t[30].filelen // Vector.sizeof()])),
    # 31 Vert Normal Indices
    'lump_31' / Lazy(Pointer(this.lump_t[31].fileofs,
                             Int16ul[this.lump_t[31].filelen // Int16ul.sizeof()])),
    # 32 unused


    # 33 Disp Verts
    'lump_33' / Lazy(Pointer(this.lump_t[33].fileofs,
                             CDispVert[this.lump_t[33].filelen // CDispVert.sizeof()])),
    # 34 Disp Lightmap Sample Pos
    'lump_34' / Lazy(Pointer(this.lump_t[34].fileofs,
                             Int8ul[this.lump_t[34].filelen // Int8ul.sizeof()])),
    # 35 Game Lump
    'lump_35' / Lazy(Pointer(this.lump_t[35].fileofs, dgamelumpheader_t)),

    # 36 Leaf Water Data
    'lump_36' / Lazy(Pointer(this.lump_t[36].fileofs,
                             dleafwaterdata_t[this.lump_t[36].filelen // dleafwaterdata_t.sizeof()])),
    # 37 Primitives
    'lump_37' / Lazy(Pointer(this.lump_t[37].fileofs,
                             dprimitive_t[this.lump_t[37].filelen // dprimitive_t.sizeof()])),
    # 38 Prim Verts
    'lump_38' / Lazy(Pointer(this.lump_t[38].fileofs,
                             dprimvert_t[this.lump_t[38].filelen // dprimvert_t.sizeof()])),
    # 39 Prim Indices
    'lump_39' / Lazy(Pointer(this.lump_t[39].fileofs,
                             Int16ul[this.lump_t[39].filelen // Int16ul.sizeof()])),
    # 40 PakFile
    'lump_40' / Lazy(Pointer(this.lump_t[40].fileofs,
                             Bytes(this.lump_t[40].filelen // Byte.sizeof()))),
    # 41 Clip Portal Verts
    'lump_41' / Lazy(Pointer(this.lump_t[41].fileofs,
                             Vector[this.lump_t[41].filelen // Vector.sizeof()])),
    # 42 Cubemaps
    'lump_42' / Lazy(Pointer(this.lump_t[42].fileofs,
                             dcubemapsample_t[this.lump_t[42].filelen // dcubemapsample_t.sizeof()])),
    # 43 Texture String Data
    'lump_43' / Lazy(Pointer(this.lump_t[43].fileofs,
                             RepeatUntil(lambda x, lst, ctx: len(lst) >=
                                         ctx.lump_t[44].filelen // Int32sl.sizeof(), CString("ascii")))),
    # 44 Texture String Table
    'lump_44' / Lazy(Pointer(this.lump_t[44].fileofs,
                             Int32sl[this.lump_t[44].filelen // Int32sl.sizeof()])),
    # 45 Overlays
    'lump_45' / Lazy(Pointer(this.lump_t[45].fileofs,
                             doverlay_t[this.lump_t[45].filelen // doverlay_t.sizeof()])),
    # 46 Leaf Min Dist to Water
    'lump_46' / Lazy(Pointer(this.lump_t[46].fileofs,
                             Int16ul[this.lump_t[46].filelen // Int16ul.sizeof()])),
    # 47 Face Macro Texture Info
    'lump_47' / Lazy(Pointer(this.lump_t[47].fileofs,
                             Int16ul[this.lump_t[47].filelen // Int16ul.sizeof()])),
    # 48 Disp Triangles
    'lump_48' / Lazy(Pointer(this.lump_t[48].fileofs,
                             CDispTri[this.lump_t[48].filelen // CDispTri.sizeof()])),
    # 49 Phys Collide Surface

    # 50 Water Overlays
    'lump_50' / Lazy(Pointer(this.lump_t[50].fileofs,
                             dwateroverlay_t[this.lump_t[50].filelen // dwateroverlay_t.sizeof()])),
    # 51 Leaf Ambient Index HDR
    'lump_51' / Lazy(Pointer(this.lump_t[51].fileofs,
                             dleafambientindex_t[this.lump_t[52].filelen // dleafambientindex_t.sizeof()])),
    # 52 Leaf Ambient Index
    'lump_52' / Lazy(Pointer(this.lump_t[52].fileofs,
                             dleafambientindex_t[this.lump_t[53].filelen // dleafambientindex_t.sizeof()])),
    # 53 Lightmaps HDR
    'lump_53' / Lazy(Pointer(this.lump_t[53].fileofs,
                             ColorRGBExp32[this.lump_t[53].filelen // ColorRGBExp32.sizeof()])),
    # 54 Worldlights HDR
    'lump_54' / Lazy(Pointer(this.lump_t[54].fileofs,
                             dworldlight_t[this.lump_t[54].filelen // dworldlight_t.sizeof()])),
    # 55 Leaf Ambient Samples HDR
    'lump_55' / Lazy(Pointer(this.lump_t[55].fileofs,
                             dleafambientlighting_t[this.lump_t[55].filelen // dleafambientlighting_t.sizeof()])),
    # 56 Leaf Ambient Samples
    'lump_56' / Lazy(Pointer(this.lump_t[56].fileofs,
                             dleafambientlighting_t[this.lump_t[56].filelen // dleafambientlighting_t.sizeof()])),
    # 57 XZIP PakFile

    # 58 Faces HDR
    'lump_58' / Lazy(Pointer(this.lump_t[58].fileofs,
                             dface_t[this.lump_t[58].filelen // dface_t.sizeof()])),
    # 59 Map Flags
    'lump_59' / Lazy(Pointer(this.lump_t[59].fileofs,
                             'mLevelFalgs' / Int32ul)),
    # 60 Overlay Fades
    'lump_60' / Lazy(Pointer(this.lump_t[60].fileofs,
                             doverlayfade_t[this.lump_t[60].filelen // doverlayfade_t.sizeof()])),

    # 61 Overlay System Levels
    # 62 Phys Level
    # 63 Disp Multiblend

)
