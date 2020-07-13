x = list()
y = [] #list를 만드는 두가지 방법

x = [1,2,3,4]
y = ["hello","world"]
z = ["hello", 1, 2, 3]

print(x)
print(y)
print(x+y)
print(z)

print(x[0],x[3]) #list 원소

x[3]=10 #list 바꿔치기
print(x)

num_element = len(x) #list 길이 함수
print(num_element)

x = [4,2,3,1]
y = sorted(x) #배열 함수
print(y)

z = sum(x) #숫자형 list의 경우 배열을 모두 합치는 함수
print(z)

#list의 element들을 하나씩 보여주는 구문
for n in x: #n에 4,2,3,1이 대입됨
  print(n)

x = [4,3,2,1]
y = ["Hello", "there"]

# 원소가 몇번째 index인지 체크
print(x.index(2))
print(y.index("Hello"))
# 원소가 그 list 안에 있는지 체크
print(4 in x)
print("Hello" in y)

#튜플--------------------------------------------

x= tuple()
y= ()#소괄호로 생성

x = (1,2,3)
y = ('a','b','c')
z = (1, "hello", "there")

print(x+y)
print('a' in y)
print(z.index("hello"))

# x[0] = 10 #=>튜플은 가변 x. 안에있는 원소를 바꿀 수 없음.

#dictionary-------------------------------------------------------
#key와 value로 이루어져 있다.

x=dict()
y = {} #중괄호를 씀

x= {
  "name":("워니","워니2"), #name:key, 워니: 키
  "age": (20,30) #key 값에 들어가는건 불변하는 값들만 가능 => list는 불가능
}

print(x)
print(x["name"]) # name key에 있는 value가 뭔지
print(x["age"])

print("age" in x) # key만 알려주는 함수
print("워니" in x)

print(x.keys()) # dictionary의 key만 보는 것. dict만의 함수
print(x.values()) #dictionary의 value만 보는 것

for key in x:
  print("key: "+ str(key))
  print("value: "+ str(x[key]))

x["name"]="woonie" #value값은 바꾸기 가능
print(x)

x["school"] = "한빛" # 추가 가능
print(x)

#------------------------------------------------------------------------------------------------
#프로그램 - 과일 종류별 숫자 세는 프로그램

fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {}

for key in fruit:
  if key in d:
    d[key] = d[key] + 1
  else :
    d[key] = 1

print(d)