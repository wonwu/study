# for문

홍길동1 = { '국어' : 95, '영어' : 90, '수학' : 80, '과학' : 50 }
홍길동2 = { '국어' : 100, '영어' : 50, '수학' : 90, '과학' : 90 }
홍길동3 = { '국어' : 99, '영어' : 60, '수학' : 100, '과학' : 40 }
홍길동4 = { '국어' : 55, '영어' : 80, '수학' : 80, '과학' : 60 }

sum1 = sum2 = sum3 = sum4 = 0
dicKeys = list(홍길동1.keys())

for i in range(len(홍길동1)):
    sum1 += 홍길동1[dicKeys[i]]
    sum2 += 홍길동2[dicKeys[i]]
    sum3 += 홍길동3[dicKeys[i]]
    sum4 += 홍길동4[dicKeys[i]]

avg1 = sum1 / len(홍길동1)
avg2 = sum2 / len(홍길동2)
avg3 = sum3 / len(홍길동3)
avg4 = sum4 / len(홍길동4)

print("홍길동1 합계 = {}, 평균 = {}" .format(sum1, avg1))
print("홍길동2 합계 = {}, 평균 = {}" .format(sum2, avg2))
print("홍길동3 합계 = {}, 평균 = {}" .format(sum3, avg3))
print("홍길동4 합계 = {}, 평균 = {}" .format(sum4, avg4))

totalSum = sum1 + sum2 + sum3 + sum4
totalAvg = ( avg1 + avg2 + avg3 + avg4 ) / 4
print("전체4명 합계 = {}, 평균 = {}" .format(totalSum, totalAvg))
