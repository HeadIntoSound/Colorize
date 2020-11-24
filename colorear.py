

class Model:
    """docstring for Model."""

    white = 16777215

    def __init__(self):

        self.value = ''

    def colorize(self, name):
        self.lista = self.chopper(name)
        self.lista = self.hexdrinker(self.lista)
        self.lista = self.group(self.lista)
        self.value = hex(self.sumar(self.lista))
        return '#' + self.value.replace('0x','')

    def chopper(self, s):
        return [char for char in s]

    def hexdrinker(self, c):
        for x in range(len(c)):
            c[x] = hex(ord(c[x]))
        return c

    def group(self, l):
        st = ['']
        i = 0
        j = 0
        for x in range(len(l)):
            st[i] += l[x].replace('0x','')
            j += 1
            if j==3:
                st.append('')
                i+=1
                j = 0
        if st[-1] == '':
            st.pop()
        return st

    def sumar(self, colores):
        suma = 0
        for x in range(len(colores)):
            suma += int(colores[x], 16)
        if suma > self.white:
            while suma > self.white:
                suma = self.recorte(suma)
        return suma

    def recorte(self, n):
        if n > self.white:
            n -= self.white
        return n

    def getComplement(self, c1):
        c1 = int(c1[1:],16)
        comp = '#' + (hex(self.white - c1)).replace('0x','')
        return comp
