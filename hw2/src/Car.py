from src.Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, company, model, yearRelease) -> None:
        super().__init__(company, model, yearRelease)
        self.numWheels = 4

    def testDrive(self):
        self.speed = 60
    
    def park(self):
        self.speed = 0

    def __str__(self) -> str:
        return super().__str__()