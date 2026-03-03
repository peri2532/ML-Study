import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__': # 이 파일을 다른 파일에서 import 했을떄는, 아래 코드는 실행되지 않도록 하기 위한 장치
    for xs in [(0,0),(1,0),(0,1),(1,1)]: #[ ] 리스트: 변경 가능, () 튜플: 변경불가능
        y = AND(xs[0] , xs[1])
        print(str(xs) + " -> " + str(y))