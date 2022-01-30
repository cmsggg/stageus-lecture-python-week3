from MenuList import MenuList
from Cart import Cart
from Payment import Payment

class Kiosk:

    # 생성자. 필요한 객체 선언 및 멤버 변수 선언
    def __init__(self):
        self.menuList = MenuList()
        self.cart = Cart()
        self.payment = None
        self.isFinish = False

    # 구동 함수
    def start(self):

        print("안녕하세요. 우리들의 카페 입니다.") 

        passageSelect = -1
        while (passageSelect != 0):   # 기능 선택 무한 반복

            print("\n1. 메뉴 담기 2. 장바구니 보기 3. 결제하기 0. 키오스크 종료")
            passageSelect = int(input("? "))

            if passageSelect == 1:
                self.addCart()
            elif passageSelect == 2:
                self.showCart()
            elif passageSelect == 3:
                self.pay()

            if self.isFinish == True:   # 결제까지 끝났으면 프로그램 종료
                print("\n이용해주셔서 감사합니다.")
                break

    # 메뉴 담기 양식 출력 함수
    def addCart(self):
        print("\n[ 메뉴 담기 ] 페이지 입니다.")

        typeSelect = -1
        while (typeSelect != 0):   # 카테고리 선택 무한 반복

            print("\n아래 보기에서 카테고리를 골라주세요.")
            self.menuList.printType()
            typeSelect = int(input("? "))

            if typeSelect != 0:

                menuSelect = -1
                while (menuSelect != 0):   # 메뉴 담기 무한 반복

                    print("\n아래 보기에서 메뉴를 골라주세요.")
                    self.menuList.printMenuList(typeSelect-1)
                    menuSelect = int(input("? "))

                    if menuSelect != 0:
                        self.cart.addMenu(self.menuList.getMenu(typeSelect-1, menuSelect-1))
                        self.menuList.getMenu(typeSelect-1, menuSelect-1).printMenu("result")
                        print(" 추가 완료")

    # 장바구니 관리 양식 출력 함수
    def showCart(self):
        print("\n[ 장바구니 보기 ] 페이지 입니다.")

        passageSelect = -1
        while (passageSelect != 0):   # 기능 선택 무한 반복

            print("\n1. 장바구니 출력 2. 메뉴 삭제 0. 뒤로 가기")
            passageSelect = int(input("? "))

            if passageSelect == 1:
                self.cart.printCart()
                self.cart.printCartInfo()
            elif passageSelect == 2:
                self.cart.delMenu()

    # 결제 진행 양식 출력 함수
    def pay(self):
        self.payment = Payment(self.cart)
        print("\n[ 결제 ] 페이지 입니다.")

        print("\n1. 현금 결제 2. 카드 결제 0. 뒤로 가기")
        passageSelect = int(input("? "))

        if passageSelect == 1:
            self.payment.cash()
            self.isFinish = True
        elif passageSelect == 2:
            self.payment.card()
            self.isFinish = True