#for, while

for i in range(3):#i는 0부터 반복
  print("i="+str(i))
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")

i = 0
while i<3: #무한loop는 while잉 편함
  print("i = "+str(i))
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")
  i = i+1

#break, continue
j=0
while True : #무한loop는 while이 편함
  print("j= "+str(j))
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")
  j = j+1

  if j>1:
    break

for k in range(100):
  print("k= "+str(k))
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")
  k = k+1

  if k>1:
    break

for k in range(3):
  print("k= "+str(k))
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")
  k = k+1

  continue #continue를 만나면 다시 루프문 처음으로 이동

  print("흰둥이: 안녕 철수야 영희야 뭐해?")

for k in range(3):
  print("k= "+str(k))
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")
  k = k+1

  #continue #continue를 만나면 다시 루프문 처음으로 이동 -> continue 없기때문에 대화 세 줄 모두 프린트됨

  print("흰둥이: 안녕 철수야 영희야 뭐해?")

for k in range(3):
  print("k= "+str(k))
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")
  k = k+1

  if k%2==1 : #continue 하기위한 특별한 조건을 만들어 준 경우.
    continue #continue를 만나면 다시 루프문 처음으로 이동

  print("흰둥이: 안녕 철수야 영희야 뭐해?")