import re

class StringСomplex:
    def __init__(self, comp_num):
        self._real = None
        self._img = None
        self.complex_number = comp_num

    @property
    def complex_number(self):
        return self.__complex_number

    @complex_number.setter
    def complex_number(self, comp_num='0'):
        #match = re.fullmatch(r'([+-]?\d*\.?\d+)i([+-]?\d*\.?\d+)', comp_num)
        if type(comp_num) != str:
            raise TypeError("Неверный тип данных")
        if (match := re.fullmatch(r'([+-]?\d*\.?\d+)i([+-]?\d*\.?\d+)', comp_num)):
            self.__complex_number = comp_num
            self._real = float(match.group(1)) if '.' in match.group(1) else int(match.group(1))
            self._img = float(match.group(2)) if '.' in match.group(2) else int(match.group(2))
        else:
            self.__complex_number = '0'
            self._real = 0
            self._img = 0

    def __str__(self):
        return self.complex_number

class ComplexNumber(StringСomplex):
    def __init__(self, comp_num):
        super().__init__(comp_num)

    def __str__(self):
        return f'{self._real} + {self._img}i' if self._img > 0 else f'{self._real} - {-1 * self._img}i'

    @property
    def real(self):
        return self._real

    @property
    def img(self):
        return self._img

    @staticmethod
    def convert_to_string(real, img):
        return f'{real}i{img}'

    def check(self, object):
        if not isinstance (object, ComplexNumber) and not isinstance (object, (int, float)):
            raise ArithmeticError("Операнд должен быть объектом класса ComplexNumber или числом")

    def __add__(self, other):
        self.check(other)
        if isinstance (other, (int, float)):
            self._real += other
            return self
        real = self._real + other._real
        img = self._img + other._img
        return ComplexNumber(self.convert_to_string(real, img))

    def __mul__(self, other):
        self.check(other)
        if isinstance (other, (int, float)):
            self._real *= other
            self._img *= other
            return self
        real = self._real * other._real - self._img * other._img
        img = self._img * other._real + other._img * self._real
        return ComplexNumber(self.convert_to_string(real, img))

    def __eq__(self, other):
        self.check(other)
        return self._real == other._real and self._img == other._img



lst = ['405i-45', '+23i+5', '-44i10', '405vb-45', '+-23i+5', '-4.4.i10']

def test_list_str(lst):
    return [str(StringСomplex(n)) for n in lst]

def test_list_coplex(lst):
    return [str(ComplexNumber(n)) for n in lst]

if __name__ == '__main__':
    print(test_list_str(lst))
    print(test_list_coplex(lst))
    st = StringСomplex('64.34i-34')
    print(st)
    s = ComplexNumber('+4.5l-78')
    print(s)
    s1 = ComplexNumber('3i2')
    s2 = ComplexNumber('1i7')
    s5 = ComplexNumber('+3i+2')
    s3 = s1 + s2
    s4 = ComplexNumber('1i1')
    print(s3.complex_number)
    print('Сложение', s3)
    print(s1 * s2)
    print('умножение',s4 * 2)
    print(s1 == s5)
    print(s1.img)

    z1 = 4+10j
    z2 = 2
    print(z1 * z2)
    print(type(z1), type(z2))