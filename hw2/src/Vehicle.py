from abc import ABC, abstractmethod, abstractproperty


class Vehicle(ABC):
    def __init__(self, company, model, yearRelease) -> None:
        self.company = company
        self.model = model
        self.yearRelease = yearRelease
        self.numWheels = 0
        self.speed = 0


    @abstractmethod
    def testDrive(self):
        pass

    @abstractmethod
    def park(self):
        pass

    def __str__(self) -> str:
        return f'Model = {self.model}, build company {self.company} from {self.yearRelease}'
