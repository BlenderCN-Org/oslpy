from .osl_py_addin import ShaderOSLPY
from .osl_py_addin import OSLReload
import bpy
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem

bl_info = {
    "name": "OSLPY",
    "author": (
        "LazyDodo, "
     ),
    "version": (0, 0, 1, 1),
    "blender": (2, 7, 8),
    "location": "Nodes > Add nodes",
    "description": "OSL PY",
    "warning": "",
    "wiki_url": "",
    "category": "Node"}


class ExtraNodesCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return (context.space_data.tree_type == 'ShaderNodeTree' and
                context.scene.render.use_shading_nodes)


node_categories = [
    ExtraNodesCategory("SH_OSL_PY", "OslPY", items=[
        NodeItem("ShaderOSLPY"),
        ]),
    ]


def register():
    bpy.utils.register_class(ShaderOSLPY)
    bpy.utils.register_class(OSLReload)
    nodeitems_utils.register_node_categories("SH_OSL_PY", node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories("SH_OSL_PY")
    bpy.utils.unregister_class(ShaderOSLPY)
    bpy.utils.unregister_class(OSLReload)


if __name__ == "__main__":
    register()