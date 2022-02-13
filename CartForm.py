# CartForm Class는 장바구니와 관련된 양식이 포함된 class
# 매개변수로 Cart 객체를 받아, 해당 Cart 객체의 메뉴 출력, 수정, 삭제 양식 선언

# ※ 기능 분할을 위한 class 설계

class CartForm():

    def __init__(self, cart):
        self.cart = cart

    # 카트 양식 함수
    def printForm(self):
        print("\n[ 장바구니 보기 ] 페이지 입니다.")

        while (True):   # 기능 선택 무한 반복

            print("\n1. 장바구니 출력 2. 메뉴 삭제 3. 메뉴 수정 0. 뒤로 가기")
            passageSelect = int(input("? "))

            if passageSelect == 1:
                self.cart.printCart()
                self.cart.printCartInfo()

            elif passageSelect == 2:
                self.deleteForm()

            elif passageSelect == 3:
                self.updateForm()

            elif passageSelect == 0:
                break

    # 카트 메뉴 삭제 양식 함수
    def deleteForm(self):
        print("\n아래에서 삭제할 메뉴를 골라주세요.")
        self.cart.printCart()
        print("0. 취소")
        menuSelect = int(input("? "))  

        if menuSelect != 0:
            self.cart.delMenu(menuSelect-1)

    # 카트 메뉴 개수 수정 양식 함수
    def updateForm(self):
        print("\n아래에서 개수를 수정할 메뉴를 골라주세요.")
        self.cart.printCart()
        print("0. 취소")
        menuSelect = int(input("? "))  

        if menuSelect != 0:
            print("\n몇 개로 바꿀까요?")
            menuCount = int(input("? "))  

            self.cart.updateMenuCount(menuSelect-1, menuCount)

