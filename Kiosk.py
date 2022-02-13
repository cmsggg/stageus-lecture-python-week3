from Cart import Cart
from OrderForm import OrderForm
from CartForm import CartForm
from PaymentForm import PaymentForm

# Kioso Class는 키오스크와 관련된 양식이 포함된 class
# 키오스크의 기본적인 동작 양식 class
# 모든 양식 class는 cart 객체를 매개변수로 요구하므로 Kiosk class에서 선언

# ※ 기능 분할을 위한 class 설계

class Kiosk:

    # 생성자. Cart Class 멤버 변수 선언
    def __init__(self):
        self.cart = Cart()

    # 프로그램 양식 출력 함수
    def start(self):

        print("안녕하세요. 우리들의 카페 입니다.") 

        while (True):   # 기능 선택 무한 반복

            print("\n1. 메뉴 담기 2. 장바구니 보기 3. 결제하기 0. 키오스크 종료")
            passageSelect = int(input("? "))

            if passageSelect == 1:
                self.orderForm()
            elif passageSelect == 2:
                self.cartForm()
            elif passageSelect == 3:
                self.paymentForm()
            elif passageSelect == 0:
                print("\n우리들의 카페 키오스크를 종료합니다.")
                break

    # OrderForm Class 실행
    def orderForm(self):
        orderFormObject = OrderForm(self.cart)
        orderFormObject.printForm()

    # CartForm Class 실행
    def cartForm(self):
        cartFormObject = CartForm(self.cart)
        cartFormObject.printForm()

    # PaymentForm Class 실행
    def paymentForm(self):
        paymentFormObject = PaymentForm(self.cart)
        paymentFormObject.printForm()