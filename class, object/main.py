#1.class, object--------------------------

class Person:
  name = "워니"

  def say_hello(self): #self는 함수안에서 본인의 속성을 써야할 때 사용.
    print("hello 내 이름은"+self.name)


p1 = Person()
p1.say_hello()

class Person1():
 #객체를 초기화하는 함수
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_Hello(self):
    print("hello, 내 이름은 "+ self.name+"이고 나이는 "+str(self.age)+"이야")

  def say_Hello_to(self,to_name):
    print("hello "+to_name+ " 내 이름은 "+ self.name+"이고 나이는 "+str(self.age)+"이야")

  def introduce(self):
    print("내 이름은 "+self.name+" 나이는 "+ str(self.age)+"살 이야.")

#초기화할 객체의 속성을 순서대로 적어주면 됨.
woonie = Person1("woonie",20) 
michael = Person1("michael",21)
jenny = Person1("jenny",22)

woonie.say_Hello()
michael.say_Hello_to("영희")
jenny.say_Hello_to("철수")

#상속----------------------------------------------

class Police(Person1): #상속을 뜻함
  def arrest(self, to_arrest):
    print("넌 체포됐다 "+ to_arrest)

class Programmer(Person1):
  def program(self, to_program):
    print("다음엔 뭘 만들지? 아 이걸 만들어야 겠다:" + to_program)

wonie = Person1("워니", 20)
jeny = Police("jeny",27)
michal = Programmer("michal",28)

jeny.introduce()
jeny.arrest("hack")

michal.introduce()
michal.program("이메일 클라이언트")

""" 이런건 객체안에 method가 없기 때문에 안됨.
wonie.arrest("w")
wonie.program("prog")
jeny.program("p1")
wonie.arrest("a")
"""