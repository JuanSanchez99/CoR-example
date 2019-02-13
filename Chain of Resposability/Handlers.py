import abc

class Handler(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def count(self, balance):
        pass

class FiftyPesos(Handler):
    value = 50
    res = 0

    def count(self, balance):
        if balance != 0:
            self.res = balance / self.value
            self.res = round(self.res)
            print('El banco te entrega ' + str(self.res) + ' billetes de cincuenta')
            balance = balance - (self.res * self.value)
        if self._successor is not None:
            self._successor.count(balance)

class TwentyPesos(Handler):
    value = 20
    res = 0

    def count(self, balance):
        if balance != 0:
            self.res = balance / self.value
            self.res = round(self.res)
            print('El banco te entrega ' + str(self.res) + ' billetes de veinte')
            balance = balance - (self.res * self.value)
        if self._successor is not None:
            self._successor.count(balance)

def main():
    veinte = TwentyPesos()
    cincuenta = FiftyPesos(veinte)
    cincuenta.count(520)


if __name__ == "__main__":
    main()
