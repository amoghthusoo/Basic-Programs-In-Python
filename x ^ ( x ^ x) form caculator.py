# Program to calculate x ^ (x ^ x) form

class Exponent:

    def __init__(self, base, exponent, boolean):
        self.base = base
        self.exponent = exponent
        self.result = 1
        self.boolean = boolean

    def pow(self):
        for self.i in range(1, self.exponent + 1):
            self.result *= self.base
            
            if self.boolean:
                self.per = (self.i/self.exponent)*100
                self.per = round(self.per, 2)
                self.per = str(self.per)

                if self.per[-2] == '.':
                    self.per += '0'

                stat = str(self.i) + ' - ' + self.per + ' %'
                print(stat)
            
        return self.result

n = int(input("\nEnter num : "))
print()


obj_1 = Exponent(n, n, False)
out_1 = obj_1.pow()

obj_2 = Exponent(n, out_1, True)
out_2 = obj_2.pow()

with open('data_python.txt', 'w') as f:
    f.write(str(out_2))

print('\nCalculation Completed!')
print('Result stored in data_python.txt\n')
