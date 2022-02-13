# Program to run a Non-GUI StopWatch

from time import sleep

class StopWatch:

    def __init__(self):
        self.s = 0
        self.m = 0
        self.h = 0

    def execute(self):

        dummy = input("\nPress any key to continue!")
        print("\n00 : 00 : 00")
        
        while True:

            
            sleep(1)
            self.s += 1
            if self.s == 60:
                self.s = 0
                self.m += 1
            if self.m == 60:
                self.m = 0
                self.h += 1
            
            self.s_str = str(self.s)
            self.m_str = str(self.m)
            self.h_str = str(self.h)

            if len(self.s_str) == 1:
                self.s_str = '0' + self.s_str
            if len(self.m_str) == 1:
                self.m_str = '0' + self.m_str
            if len(self.h_str) == 1:
                self.h_str = '0' + self.h_str
            

            print(self.h_str  + " : " + self.m_str + " : " + self.s_str)
        

obj = StopWatch()
obj.execute()