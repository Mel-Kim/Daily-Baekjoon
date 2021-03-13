S=input()
alphabet = list(range(97,123))

for x in alphabet:			
	print(S.find(chr(x)))
	

# 아스키코드 활용

# find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력

# ord( ) 함수: 문자 -> 숫자(아스키코드)로 변환
# chr( ) 함수: 숫자(아스키코드) -> 문자로 변환
# find 함수: 문자열에서만 사용 가능한 함수
# index 함수는 문자열뿐만 아니라 
# 리스트, 튜플과 같은 반복 가능한 iterable 자료형에서도 찾는 문자의 인덱스를 반환하는 함수

# find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력하지만 
# index함수는 >AttributeError가 발생
