from strategy.sportsdrivestrategy import SportsDriveStrategy
from vehicle import Vehicle

class OffRoadVehicle(Vehicle):

    def __init__(self):
        super().__init__(SportsDriveStrategy())