from strategy.normaldrivestrategy import NormalDriveStrategy
from vehicle import Vehicle


class GoodsVehicle(Vehicle):

    def __init__(self):
        super().__init__(NormalDriveStrategy())