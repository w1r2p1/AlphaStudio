from abc import abstractmethod, ABCMeta

class QStrategy(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def initialization(self):

        raise NotImplementedError("Should implement initialization()")

    @abstractmethod
    def onTick(self):
        raise NotImplementedError("Should implement onTick()")

    @abstractmethod
    def onBar(self, qBar):

        raise NotImplementedError("Should implement onBar()")

    @abstractmethod
    def scheduler(self, qBar):
        raise NotImplementedError("Should implement scheduler()")

    @abstractmethod
    def onOrder(self):

        raise NotImplementedError("Should implement onOrder()")

    def runBackTest(self):
        pass

    def runSimulation(self):
        pass

    def runLiveStrategy(self):
        pass
