import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

def makerandomnum_warpper(func):
    def randomnum(n,max): # 生成器函数
      counter = 0
      while True:
          if (counter > n): 
              return
          yield random.randint(0,max)
          counter += 1
    def scatter_improve(n,max):
      x=list(randomnum(n,max))
      y=list(randomnum(n,max))
      func(x,y,max)
        
    return scatter_improve

@makerandomnum_warpper
def makescatter(x,y,max):
  
    plt.axis([0,max,0,max])
    plt.scatter(x,y,marker='o')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Scatter Plot')
    plt.show()

if __name__ == "__main__": 
    makescatter(50,50)
