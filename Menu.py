class Menu:
    
    # 생성자. 메뉴의 기본 정보 멤버 변수 생성
    def __init__(self, type, name, price, stock):
        self.type = type
        self.name = name
        self.price = price
        self.stock = stock

    # 메뉴 재고 설정 함수
    def setStock(self, number):
        if self.stock < number:
            self.stock += number
            return True
        else:
            return False

    # 메뉴 정보 출력 함수
    def printMenu(self, format):
        if format == "type":
            print(self.type)
        if format == "menu":
            print("%-20s" % self.name, end="")
            print("%-6d" % self.price)
        elif format == "result":
            print("%s %d" % (self.name, self.price), end="")
        elif format == "all":
            print("%-6s" % self.type, end="")
            print("%-20s" % self.name, end="")
            print("%-6d" % self.price, end="")
            print("%-5d" % self.stock)         