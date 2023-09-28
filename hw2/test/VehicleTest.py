import unittest
from src.Vehicle import Vehicle
from src.Car import Car
from src.Motorcycle import Motorcycle


class VehicleTest(unittest.TestCase):
    def car_create(self):
        return Car('test_company', 'test_model', 1999)
    
    def motorcycle_create(self):
        return Motorcycle('test_company', 'test_model', 1999)
    
    def test_car_is_subclass_vehicle(self):
        test_car = self.car_create()
        self.assertIsInstance(test_car, Vehicle)

    def test_car_numWheels(self):
        test_car = self.car_create()
        self.assertEqual(test_car.numWheels,4)

    def test_motorcycle_numWheels(self):
        test_motorcycle = self.motorcycle_create()
        self.assertEqual(test_motorcycle.numWheels,2)

    def test_motorcycle_testdrive(self):
        test_motorcycle = self.motorcycle_create()
        test_motorcycle.testDrive()
        self.assertEqual(test_motorcycle.speed,75)

    def test_car_testdrive(self):
        test_car = self.car_create()
        test_car.testDrive()
        self.assertEqual(test_car.speed,60)

    def test_motorcycle_park(self):
        test_motorcycle = self.motorcycle_create()
        test_motorcycle.testDrive()
        test_motorcycle.park()
        self.assertEqual(test_motorcycle.speed,0)

    def test_car_park(self):
        test_car = self.car_create()
        test_car.testDrive()
        test_car.park()
        self.assertEqual(test_car.speed,0)

if __name__ == '__main__':
    unittest.main()