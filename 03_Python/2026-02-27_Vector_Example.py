# import numpy as np # numnpy는 벡터/행렬 계산을 빠르게 해주는 라이브러리
# a=np.array([1,2,3])
# b=np.array([4,5,6,])

# dot = np.dot(a,b)

# norm_a =np.linalg.norm(a) #linalg =linear algebra 선형대수
# norm_b = np.linalg.norm(b) # ||a||,||b|| (벡터의 길이)계산

# cos_theta = dot / (norm_a * norm_b) #값이 1에 가까우면 방향이 비슷, 0이면 직교, -1이면 반대.
# print("dot: ", dot)
# print("cos(theta):", cos_theta) #결과 출력

# a = [1, 2, 3]
# b = [4, 5, 6]
# result = 0
# for i in range(3):
#     result += a[i] * b[i]
    
# print(result)


import numpy as np
a= np.array([1,2,3])
b= np.array([4,5,6])
c = np.array([1, -2, 1])
dot = np.dot(a,c)

norm_a=np.linalg.norm(a)
norm_b=np.linalg.norm(b)
norm_c=np.linalg.norm(c)
cos_theta = dot / (norm_a * norm_c)
print("dot: ", dot)
print("코사인 세타 계산 : ",cos_theta )