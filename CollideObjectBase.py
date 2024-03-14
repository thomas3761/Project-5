from panda3d.core import PandaNode, Loader , NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3

class PlacedObject(PandaNode):

    def __init__(self, Loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        self.modelPath: NodePath = Loader.LoadModel(modelPath)

        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject Loader.LoadModel ("+ modelPath + ") did not return a proper PandaNodel!")
        
        self.ModelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)

class CollidableObject(PlacedObject):

    def __init__(self, Loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        super(CollidableObject, self).__init__(Loader, modelPath, parentNode, nodeName)

        self.collisionNode = self.modelNode.attachNewNode(CollisionNode(nodeName + '_cNode'))

class InverseSphereCollideObject(CollidableObject):

    def __init__(self, Loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super(InverseSphereCollideObject, self).__init__(Loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionCapsule(colPositionVec, colRadius))
        #self.collisionNode.show()

class CollisionCapsuleObject(CollidableObject):
    def __init__(self, Loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str,ax: float, ay: float, az: float, bx: float, by: float, bz: float, r: float):
        super(CollidableObject, self).__init__(Loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionCapsule(ax, ay, bx, by, bz, r))
        self.collisionNode.show()