num=int(input())  # 소인수분해할 숫자 받아오기
num_list=[]  # 소인수를 저장할 리스트 생성
while num != 1: # 소인분해가 완료될 때까지 반복
    for i in range(2, num+1):  # 2부터 num까지 나누기
        if num % i == 0: # 만약 num이 i로 나누어 떨어진다면
            num_list.append(i) # 소인수 리스트에 저장하기
            num = num // i  # 소인수 분해된 결과 업데이트
            break # 소인수분해가 완료되면 반복문 나오기
for i in num_list:
    print(i) # 소인수 리스트 프린트
