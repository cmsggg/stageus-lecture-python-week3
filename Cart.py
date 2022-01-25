class Cart:

    # 생성자. 장바구니 목록 멤버 변수 생성
    def __init__(self):
        self.cartList = []

    # 장바구니 Menu 추가 함수
    def addMenu(self, menu):
        self.cartList.append(menu)

    # 장바구니 메뉴 삭제 함수
    def delMenu(self):
        self.printCart()
        print("0. 뒤로가기")

        delSelect = int(input("? "))
        del self.cartList[delSelect-1]

    # 장바구니 목록 출력 함수
    def printCart(self):
        for index in range(0, len(self.cartList)):
            print(str(index+1) + ". ", end="")
            self.cartList[index].printMenu("result")
            print("")

    # 장바구니 정보 출력 함수
    def printCartInfo(self):
        print("총 개수 : " + str(self.calTotalNumber()))
        print("총합 가격 : " + str(self.calTotalPrice()))

    # 장바구니 상품 개수 반환 함수
    def calTotalNumber(self):
        return len(self.cartList)

    # 장바구니 총합 가격 반환 함수
    def calTotalPrice(self):
        totalPrice = 0

        for index in range(0, len(self.cartList)):
            totalPrice += self.cartList[index].price

        return totalPrice