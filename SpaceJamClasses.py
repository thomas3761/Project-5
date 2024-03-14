from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.task.Task import TaskManager
from typing import Callable 
from CollideObjectBase import *
from direct.gui.OnscreenImage import OnscreenImage

class Planet(SphereCollideObject):

    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super().__init__(nodeName)

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.loader = loader
        self.render = render

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        #planets
        self.planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet1.reparentTo(self.render)
        self.planet1.setPos(150, 5000, 67)
        self.planet1.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 1.jpg")
        self.planet1.setTexture(tex, 1)

        self.planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet2.reparentTo(self.render)
        self.planet2.setPos(7314, 1274, 976)
        self.planet2.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 2.jpg")  
        self.planet2.setTexture(tex, 1)

        self.planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet3.reparentTo(self.render)
        self.planet3.setPos(11985, 1274, 1112)
        self.planet3.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 3.png")
        self.planet3.setTexture(tex, 1)

        self.planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet4.reparentTo(self.render)
        self.planet4.setPos(9067, 1274, 2378)
        self.planet4.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 4.jpg")
        self.planet4.setTexture(tex, 1)

        self.planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet5.reparentTo(self.render)
        self.planet5.setPos(1382, 1274, 4567)
        self.planet5.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 5.jpg")
        self.planet5.setTexture(tex, 1)

        self.planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet6.reparentTo(self.render)
        self.planet6.setPos(4502, 1274, 6478) 
        self.planet6.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 6.png")
        self.planet6.setTexture(tex, 1)

class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float,colPositionVec: Vec3, colRadius: float):
        super(InverseSphereCollideObject, self).__init__(loader, modelPath, parentNode, nodeName, colPositionVec, colRadius)
        
        # Set position and scale of the model node
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

        # Load the model, set its texture, and position it
        self.universe = loader.loadModel(modelPath)
        self.universe.reparentTo(render)
        self.universe.setPos(posVec)
        self.universe.setScale(scaleVec)
        self.universe.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.universe.setTexture(tex, 1)

        self.loader = loader
        self.render = render

        self.universe = loader.loadModel("./Assets/Universe/Universe.x")
        self.universe.reparentTo(render)
        self.universe.setScale(15000)
        tex = loader.loadTexture("./Assets/Universe/space-galaxy.jpg")
       
class Spaceship(PlacedObject):# / player
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float, taskManager: TaskManager, accept: Callable[[str, Callable], None]):
        super().__init__(loader, render, modelPath, parentNode, nodeName)
        
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.taskManager = taskManager
        self.loader = loader
        self.render = render
        self.accept = accept

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        self.modelNode.setP(100)

        self.reloadTime = .25
        self.missileDistance = 4000
        self.missileBay = 1
        self.taskManager.add(self.CheckIntervals, ' ChekMissiles', 34)


        self.setKeyBindings()

       # self.spaceship = self.loader.loadModel(".\Assets\Khan\Khan.x")
        self.modelNode.reparentTo(self.render)
        self.modelNode.setPos(0, 0, 0) 
        self.modelNode.setScale(10)
        #tex = self.loader.loadTexture(".\Assets\Khan\Khan.jpg")
        self.modelNode.setTexture(tex, 1)
        
    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'Forward-thrust')
        else: 
            self.taskManager.remove('Forward-thrust')

    def ApplyThrust(self, task):
        rate = 3
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
        
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'LeftTurn')
        else: 
            self.taskManager.remove('LeftTurn')

    def ApplyLeftTurn(self, task):
        # Half a degree every frame
        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
        
    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'RightTurn')
        else:
            self.taskManager.remove('RightTurn')

    def ApplyRightTurn(self, task):
        # Half a degree every frame
        rate = -0.5  
        self.modelNode.setH(self.modelNode.getH() + rate)  
        return Task.cont
        
    def MoveUp(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyMoveUp, 'MoveUp')
        else: 
            self.taskManager.remove('MoveUp')

    def ApplyMoveUp(self, task):
        # Half a degree every frame
        rate = 0.5  
        self.modelNode.setZ(self.modelNode.getZ() + rate)  
        return Task.cont
        
    def MoveDown(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyMoveDown, 'MoveDown')
        else: 
            self.taskManager.remove('MoveDown')

    def ApplyMoveDown(self, task):
        # Half a degree every frame
        rate = -0.5  
        self.modelNode.setZ(self.modelNode.getZ() + rate) 
        return Task.cont
        
    def RotateLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRotateLeft, 'RotateLeft')
        else: 
            self.taskManager.remove('RotateLeft')

    def ApplyRotateLeft(self, task):
        # Half a degree every frame
        rate = 0.5  
        self.modelNode.setP(self.modelNode.getP() + rate)  
        return Task.cont

    def RotateRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRotateRight, 'RotateRight')
        else:
            self.taskManager.remove('RotateRight')

    def ApplyRotateRight(self, task):
        # Half a degree every frame
        rate = -0.5  
        self.modelNode.setP(self.modelNode.getP() + rate) 
        return Task.cont
    
    def Fire(self):
        if self.missileBay:
            travRate = self.missileDistance
            aim = self.render.getRelativePoint(self.modelNode, Vec3.forward())
            aim.normalize()
            fireSolution = aim * travRate
            inFront =aim * 150
            travVec = fireSolution + self, modelNode.getPos()
            self.missileBay -= 1
            tag = 'Missile' + str(Missile.missileCount)
            posVec = self.modelNode.getPos() + inFront
            currentMissile = Missile(self.loader, './Assets/Phaser/Phaser.egg', self.render, tag, posVac, 4.0)
            Missile.Intervals[tag] = currentMissile.modelNode.posInterval(2.0, travVec, startPos = posVec, fuid = 1)
            Missile.Intervals[tag].staret()

        else:
            if not self.taskManager.hasTaskNamd('reloaad'):
                print('Initializing reload...')
                self.taskManager.doMethodLater(0,self.Reload, 'reload')
                return Task.cont
            
    def Reload(self, task):
        if task.time > self.reloadTime:
            self.missileBay += 1
        
            if self.missileBay > 1
            self.missileBay = 1

            print("Reload complete")
            return Task.done
        
        elif task.time <= self.reloadTime:
            print("Reload proceeding...")
            return Task.cont
            
    def setKeyBindings(self):  
        # All key Bindings for Spaceship move
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])

        # Keys for left and right
        self.accept('arrow_left', self.LeftTurn, [1])
        self.accept('arrow_left-up', self.LeftTurn, [0])
        self.accept('arrow_right', self.RightTurn, [1])
        self.accept('arrow_right-up', self.RightTurn, [0])

        # Keys for up and down
        self.accept('arrow_up', self.MoveUp, [1])
        self.accept('arrow_up-up', self.MoveUp, [0])
        self.accept('arrow_down', self.MoveDown, [1])
        self.accept('arrow_down-up', self.MoveDown, [0])

        # Keys for rotating left and right
        self.accept('a', self.RotateLeft, [1])
        self.accept('a-up', self.RotateLeft, [0])
        self.accept('d', self.RotateRight, [1])
        self.accept('d-up', self.RotateRight, [0])

        #f to fire 
        self.accept('f', self.fire)

    def checkIntervals(self, task):
        for i in Missile.Intervals:
            if not Missile.Intervals[i].isPlaying():
                Missile.cNodes[i].detachNode()
                Missile.fireModels[i].detachNode()
            del Missile.Intervals[i]
            del Missile.fireModels[i]
            del Missile.cNodes[i]
            del Missile.collisionSolids[i]

            print(1 + 'has reached the end of it fire solution.')
            break
            return Task.cont
        
    def EnableHud(self):
        self.Hud = OnscreenImage(image = "./Assets/Hud/Reticle3b.png", pos = Vec3 (0,0,0), scale = 0.1)
        self.hud.setTransparency(TransparencyAttrib.MAlpha)
        self.EnableHUd()

      
class SpaceStation(CollidableObject):
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10)

        self.station = loader.loadModel(modelPath)
        self.station.reparentTo(render)
        self.station.setPos(posVec)
        self.station.setScale(scaleVec)
        self.station.setName("SpaceStation")

        self.loader = loader
        self.render = render

        tex = loader.loadTexture(texPath)
        self.station.setTexture(tex, 1)
        
        self.station = loader.loadModel("./Assets/SpaceStation1B/spaceStation.x")
        self.station.reparentTo(render)
        self.station.setPos(1000, 5000, 80)
        self.station.setScale(50)
        tex = loader.loadTexture("./Assets/SpaceStation1B/SpaceStation1_Dif2.png")
        self.station.setTexture(tex, 1)

class Missile(SphereCollideObject):

    fireModels ={}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1):
        super(Missile, self).__init__(Loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
        
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)
        self.modelNode.setName(nodeName)

        Missile.missileCount += 1

        Missile.fireModels[nodeName] = self.modelNode
        Missile.cNodes[nodeName]=self.collisionNode
        Missile.collisionSolids[nodeName] = self.collisionNode.node().getsolid(0)
        Missile.cNodes[nodeName].show()

        print("Fire torpedo #" + str(Missile.missileCount))

class DroneShowBase():
    # # of Drone
    droneCount = 0