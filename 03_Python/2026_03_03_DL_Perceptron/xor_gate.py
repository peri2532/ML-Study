from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

if __name__ == '__main__': # 이 파일을 다른 파일에서 import 했을떄는, 아래 코드는 실행되지 않도록 하기 위한 장치
    for xs in [(0,0),(1,0),(0,1),(1,1)]: #[ ] 리스트: 변경 가능, () 튜플: 변경불가능
        y = AND(xs[0] , xs[1])
        print(str(xs) + " -> " + str(y))