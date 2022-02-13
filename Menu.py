# Cart.py 객체에 N차원 리스트로 값을 삽입하여 관리하는 것 보단, 객체로 관리하는 것이 편리하므로 Menu.py class를 생성
# 메뉴 출력, 수정 등의 로직 선언

# ※ 데이터 복제를 위한 Class 설계

class Menu:
    
    # 생성자. 각 매개 변수 저장
    def __init__(self, data, count):
        self.category = data[0]
        self.name = data[1]
        self.price = data[2]
        self.count = count

    # 카테고리 반환 함수
    def getCategory(self):
        return self.category

    # 이름 반환 함수
    def getName(self):
        return self.name

    # 가격 반환 함수
    def getPrice(self):
        return self.price * self.count

    # 개수 반환 함수
    def getCount(self):
        return self.count

    # 개수 수정 함수
    def setCount(self, count):
        self.count = count

    # 메뉴 출력 함수
    def printMenu(self):
        print("%-6s" % self.category, end="")
        print("%-20s" % self.name, end="")
        print("%-6d" % self.price, end="")
        print("%-4s" % self.count, end="")
        print(self.price * self.count)