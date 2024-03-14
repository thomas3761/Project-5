from direct.showbase.ShowBase import ShowBase
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths
from panda3d.core import *
import math, random
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
from CollideObjectBase import PlacedObject

class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setScene()
        #self.SetCamera()

        self.planet1 = spaceJamClasses.Planet(self.loader, self.render, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "./Assets/Planets/Planet 1.jpg", Vec3(150, 5000, 67), 350)
        self.planet2 = spaceJamClasses.Planet(self.loader, self.render, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "./Assets/Planets/Planet 2.jpg", Vec3(7314, 1274, 976), 350)
        self.planet3 = spaceJamClasses.Planet(self.loader, self.render, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "./Assets/Planets/Planet 3.png", Vec3(11985, 1274, 1112), 350)
        self.planet4 = spaceJamClasses.Planet(self.loader, self.render, "./Assets/Planets/protoPlanet.x", self.render, "Planet4", "./Assets/Planets/Planet 4.jpg", Vec3(9067, 1274, 2378), 350)
        self.planet5 = spaceJamClasses.Planet(self.loader, self.render, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "./Assets/Planets/Planet 5.jpg", Vec3(1382, 1274, 4567), 350)
        self.planet6 = spaceJamClasses.Planet(self.loader, self.render, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "./Assets/Planets/Planet 6.png", Vec3(4502, 1274, 6478), 350)

        self.modelNode = spaceJamClasses.Spaceship(self.loader, self.render, "./Assets/Khan/Khan.x", self.render, "Spaceship", "./Assets/Khan/Khan.jpg", Vec3(400, 0, 0), 10, self.taskMgr, self.accept)

        self.universe = spaceJamClasses.Universe(self.loader, self.render, "./Assets/Universe/Universe.x", self.render, "Universe", "./Assets/Universe/space-galaxy.jpg", Vec3(0,0,0), 15000, Vec3(0, 0, 0), 0.9)  # Example values for colPositionVec and colRadius

        self.spaceStation = spaceJamClasses.SpaceStation(self.loader, self.render, "./Assets/SpaceStation1B/spaceStation.x", "./Assets/SpaceStation1B/SpaceStation1_Dif2.png", Vec3(1000, 5000, 80), 50)


        self.cTrav = CollisionTraverser()
        self.cTrav.traverse(self.render)
        self.pusher = CollisionHandlerPusher()
        self.pusher.addCollider(self.spaceship.collisionNede, self.spaceship.modelNode)
        self.cTrav.pusher.addCollider(self.spaceship.collisionNede, self.pusher)
        self.cTrav.showCollisions(self.render)

        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.DroneShowBase.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.DroneShowBase.droneCount)
            self.DrawCloudDefense(self.planet1, nickName)

        #self.DrawBaseballSeams(self.planet1, 10, 36)
        
        

        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.DroneShowBase.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.DroneShowBase.droneCount)
            #position = Vec3(0, 0, 0) this bricks Circle 
            self.DrawCloudDefense(self.planet1, nickName)

    def DrawCloudDefense(self, centralObject, droneName):
        # XY plane
        for theta in range(0, 360, 10):
            placeholder = self.render.attachNewNode('placeholder')
            posVec = Vec3(100.0 * math.cos(math.radians(theta)), 100.0 * math.sin(math.radians(theta)), 0.0)  # XY plane
            placeholder.setPos(posVec)

            # Load the drone model
            drone_model = self.loader.loadModel("Assets/DroneDefender/DroneDefender.obj")
            drone_model.reparentTo(placeholder)
            drone_model.setScale(3)

        # XZ plane
        for theta in range(0, 360, 10):
            placeholder = self.render.attachNewNode('placeholder')
            posVec = Vec3(100.0 * math.cos(math.radians(theta)), 0.0, 100.0 * math.sin(math.radians(theta)))  # XZ plane
            placeholder.setPos(posVec)

            # Load the drone model
            drone_model = self.loader.loadModel("Assets/DroneDefender/DroneDefender.obj")
            drone_model.reparentTo(placeholder)
            drone_model.setScale(3)

        # YZ plane
        for theta in range(0, 360, 10):
            placeholder = self.render.attachNewNode('placeholder')
            posVec = Vec3(0.0, 100.0 * math.cos(math.radians(theta)), 100.0 * math.sin(math.radians(theta)))  # YZ plane
            placeholder.setPos(posVec)

            # Load the drone model
            drone_model = self.loader.loadModel("Assets/DroneDefender/DroneDefender.obj")
            drone_model.reparentTo(placeholder)
            drone_model.setScale(3)

# this bricks Circle
    #def DrawBaseballSeams(self, centralObject, step, numSeams, radius=1): 
    #    for i in range(numSeams):
    #        position = defensePaths.BaseballSeams(step, numSeams, B=0.4) * radius
     #       self.DrawCloudDefense(centralObject, f"Drone_{i}", position)
#
 #   def DrawCloudDefense(self, centralObject, droneName, position):
  #      # Assuming this method places drones similar to the previous implementation
   #     placeholder = self.render.attachNewNode('placeholder')
    #    placeholder.setPos(position)
#
 #       drone_model = self.loader.loadModel("Assets/DroneDefender/DroneDefender.obj")
  #      drone_model.reparentTo(placeholder)
   #     drone_model.setScale(3)
            

    #def SetCamera(self):
    #    self.disableMouse()
    #    self.camera.reparentTo(self.spaceship.modelNode)
    #    self.camera.setFluidPos(0, 1, 0)



    def setScene(self):
        return

app = SpaceJam()
app.run()