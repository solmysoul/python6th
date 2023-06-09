class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.number = 10

    def __str__(self): # 프린트 할 때 예쁘게 출력해주는 함수
        return f'ParentClass name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('부모 : ', new_number, '만큼 더해야지')
        self.number = self.number + new_number

class ChildClass (ParentClass): # 부모 클래스를 상속 받아서 실행함, 아무 입력을 하지 않으면 부모 클래스와 똑같이 출력
    def __init__(self):
        super().__init__() # 재정의, 이 코드가 없으면 오류남
        self.name = 'child'

    def __str__(self):
        return f'ChildClass name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('말 안듣는 자식: 고정적으로 5 더할건데?')
        self.number = self.number + 5


parent = ParentClass()
child = ChildClass()
print(parent)
print(child)
print("=============")

print('7을 더하세요')
parent.add_num(7)
child.add_num(7)

print(parent)
print(child)



