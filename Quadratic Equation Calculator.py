# Program to solve a quadratic equation with real coefficients

class Quadratic_Equation_Calc:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def execute(self):

        self.D = self.b**2 - 4*self.a*self.c
        self.root_D = self.D**0.5
        self.x1 = (-self.b + self.root_D)/2*self.a
        self.x2 = (-self.b - self.root_D)/2*self.a

        if 'j' in str(self.x1):
            self.x1_real = str(round(self.x1.real, 2))
            self.x1_imag = str(round(self.x1.imag, 2))
            self.x2_real = str(round(self.x2.real, 2))
            self.x2_imag = str(round(-self.x2.imag, 2))
            print('\n' + self.x1_real + ' + ' + self.x1_imag + 'i')
            print(self.x2_real + ' - ' + self.x2_imag + 'i\n')

        else:
            print("\n" + str(self.x1))
            print(str(self.x2) + "\n")
        
a = float(input("\nEnter coefficient of x^2 : "))
b = float(input("Enter coefficient of x : "))
c = float(input("Enter the constant term : "))

obj = Quadratic_Equation_Calc(a, b, c)
obj.execute()