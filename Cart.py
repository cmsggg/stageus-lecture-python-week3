# Cart class는 장바구니와 관련된 기능이 포함된 class
# 장바구니 출력, 수정, 삭제 등의 로직 선언

# ※ 모듈화를 위한 Class 설계

class Cart:

    # 생성자. 장바구니 목록 멤버 변수 선언
    def __init__(self):
        self.cartList = []

    # 장바구니 메뉴 개수 반환 함수
    def getCartCount(self):
        return len(self.cartList)

    # 장바구니 메뉴 총합 개수 반환 함수
    def getCartTotalCount(self):
        totalCount = 0
        
        for index in range(0, self.getCartCount()):
            totalCount += self.cartList[index].getCount()

        return totalCount

    # 장바구니 총합 금액 반환 함수
    def getCartPrice(self):
        totalPrice = 0

        for index in range(0, self.getCartCount()):
            totalPrice += self.cartList[index].getPrice()

        return totalPrice

    # 장바구니 Menu 추가 함수
    def addMenu(self, menu):
        self.cartList.append(menu)

    # 장바구니 Menu 삭제 함수
    def delMenu(self, index):
        del self.cartList[index]

    # 장바구니 Menu 개수 변경 함수
    def updateMenuCount(self, index, value):
        self.cartList[index].setCount(value)

    # 장바구니 목록 출력 함수
    def printCart(self):
        for index in range(0, self.getCartCount()):
            print(str(index+1) + ". ", end="")
            self.cartList[index].printMenu()

    # 장바구니 정보 출력 함수
    def printCartInfo(self):
        print("메뉴 종류 : " + str(self.getCartCount()))
        print("총 개수 : " + str(self.getCartTotalCount()))
        print("총합 가격 : " + str(self.getCartPrice()))