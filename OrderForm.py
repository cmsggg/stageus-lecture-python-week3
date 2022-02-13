from Menu import Menu
from Database import Database

# OrderForm Class는 주문과 관련된 양식이 포함된 class
# 매개변수로 Cart 객체를 받아, 해당 Cart 객체에 메뉴 삽입 양식 선언

# ※ 기능 분할을 위한 class 설계

class OrderForm:

    # 생성자. Cart Object 멤버 변수 저장
    def __init__(self, cart):
        self.cart = cart
        self.database = Database()

    # 주문 양식 함수
    def printForm(self):
        print("\n[ 메뉴 담기 ] 페이지 입니다.")

        while (True):   # 카테고리 선택 무한 반복
            categoryIndex = self.selectCategoryForm()
            if categoryIndex != 0:

                while (True):   # 메뉴 선택 무한 반복
                    menuIndex = self.selectMenuForm(categoryIndex)
                    if menuIndex != 0:
                        menuCount = self.selectCountForm()
                        self.insertMenu(categoryIndex, menuIndex, menuCount)
                    elif (menuIndex == 0):
                        break

            elif (categoryIndex == 0):
                break

    # 카테고리 선택 양식 함수
    def selectCategoryForm(self):
        print("\n아래 보기에서 카테고리를 골라주세요.")
        self.database.printCategoryList()
        print("0. 뒤로 가기")
        categoryIndex = int(input("? "))   

        return categoryIndex

    # 메뉴 선택 양식 함수
    def selectMenuForm(self, categoryIndex):
        print("\n아래 보기에서 메뉴를 골라주세요.")
        self.database.printMenuList(categoryIndex-1)
        print("0. 뒤로 가기")
        menuIndex = int(input("? "))

        return menuIndex

    # 개수 선택 양식 함수
    def selectCountForm(self):
        print("\n몇 개를 추가 할까요?")
        menuCount = int(input("? "))

        return menuCount

    # 메뉴 삽입 함수
    def insertMenu(self, typeSelect, menuIndex, menuCount):
        data = self.database.getMenu(typeSelect-1, menuIndex-1)
        tmpMenu = Menu(data, menuCount)   # Menu 객체 생성 및 초기화
        self.cart.addMenu(tmpMenu)
        print("메뉴 추가 완료")