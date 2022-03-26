from tkinter import TkVersion


class Control:
    def __init__(self):
        self._tv = None

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDow(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def enlazar(self, televisor):
        self._tv = televisor
        self._tv._control = self

    def gettv(self):
        return self._tv

    def settv(self, tv):
        self._tv = tv
