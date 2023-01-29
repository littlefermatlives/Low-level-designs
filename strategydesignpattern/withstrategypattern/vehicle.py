from strategy.drivestrategy import DriveStrategy


class Vehicle:

    drive_strategy_obj = DriveStrategy()

    def __init__(self, drive_obj):
        self.drive_strategy_obj = drive_obj

    def drive(self):
        self.drive_strategy_obj.drive()