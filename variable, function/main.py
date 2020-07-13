x=1
y=2
print(x)
print(y)

x = "Hello"
y = 'bye' ##""와 ''는 같음
z = """
안녕하세요
ㅇㅇㅇ입니다
"""

print(x)
print(y)
print(z)
print("안녕"+"잘지내니")

print("너 혹시 몇살이니 "+str(4)) # 서로다른 타입은 같이 쓸 수 없음. 캐스팅 해줘야함

x = 4 # 숫자타입
y = "4" # 문자열타입

print(str(x)+y) #문자열
print(x+int(y)) #숫자열로 연산

#if문 예제####################

x=3 
if x<2:
  print("hello")
elif x==3:
  print("Bye")
else:
    print("hi")

##############################################################

#함수 생성##############################

def chat(): #def:함수 정의 chat():함수정의명
  print("철수: 안녕? 넌 몇살이니?")
  print("영희 : 나? 나는 28")

chat()
chat()

def chat1(name1, name2):
  print("%s : 안녕? 넌 몇살이니?" %name1)
  print("%s : 나? 나는 28" %name2)

chat1("Alex", "윤하")
chat1("알렉스", "yunha")

def chat2(name1, name2, age):
  print("%s : 안녕? 넌 몇살이니?" %name1)
  print("%s : 나? 나는 %d" %(name2, age))

chat2("철수","영희",29)

def dsum(a, b):
  result = a+b
  return result

d = dsum(2,4)
print(d)

########################################################

#복습
#먼저 이름과 나이를 받아라
#나이가 18살 미만이면 "안녕"이라고 말해라
#나이가 18살~20살 사이면 "안녕하세요" 라고 말해라
#그 외에는 "안녕하십니까" 라고 말해라

def sayHello(name, age):
  if age<18:
    print("안녕")
  elif age>=18 and age<=20:
    print("안녕하세요")
  else:
    print("안녕하십니까")
  print("이름이 뭐니?")
  print("제 이름은 %s 입니다"%name)
  print("몇살이십니까")
  print("%d살 입니다."%age)

sayHello("alex", 17)
sayHello("철수", 18)
sayHello("영희", 21)

###########################################################

#format
print("a = {0:0.1f}, b= {2:0d}, c= {1:0.1f}".format(3.14, 3.5, 3))
#format으로 받을때 기본적으로 :0f, :0s, :0d등으로 받음. 그앞의 숫자는 format 안의 value들의 순서를 지정.