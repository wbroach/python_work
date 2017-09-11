
class Fibonacci():
    
    def __init__(self, size=10):
        
        self.size = size
        self.fibs = [0, 1]
        
    def fill_sequence(self):
        
        while len(self.fibs) < self.size:
            next_fib = self.fibs[-2] + self.fibs[-1]
            self.fibs.append(next_fib)
            
##test
f = Fibonacci(size=50)

f.fill_sequence()

seq = f.fibs

for i in seq:
    print(i)
