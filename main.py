class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "The engine is running!"

# 자식 클래스
class Car(Vehicle):
    def start_engine(self):
        return super().start_engine() + " It's a car engine."
    # super() 부모 클래스의 함수를 먼저 실행해서 가져오는 함수

# 인스턴스 생성
my_car = Car("Toyota", "Corolla", 2020)

# 메소드 호출
print(my_car.start_engine())
