from Mod10.Hissi import Hissi

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.alin = alin
        self.ylin = ylin
        self.lkm = lkm
        self.hissit= []
        for i in range(lkm):
            self.hissit.append(Hissi(self.alin, self.ylin))

    def aja_hissia(self, numero, siirtyma):
        if 1 <= numero <= self.lkm:
            self.hissit[numero - 1].siirry_kerrokseen(siirtyma)
        else:
            print("error")

    def palohalytys(self):
        print("palohalytys")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)