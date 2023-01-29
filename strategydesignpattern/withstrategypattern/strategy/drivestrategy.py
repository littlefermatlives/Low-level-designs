import abc

class DriveStrategyInterface(abc.ABC):

    @abc.abstractmethod
    def drive(self):
        pass

class DriveStrategy(DriveStrategyInterface):

    def drive(self):
        pass