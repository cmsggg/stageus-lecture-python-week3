# PaymentForm Class는 결제와 관련된 양식이 포함된 class
# 매개변수로 Cart 객체를 받아, 해당 Cart 객체에 대한 결제 양식 선언

# ※ 기능 분할을 위한 class 설계

class PaymentForm:

    # 생성자. Cart Object 멤버 변수 저장 및 금액 관련 멤버 변수 선언
    def __init__(self, cart):
        self.cart = cart
        self.money = 0
        self.rest = 0

    # 결제 양식 함수
    def printForm(self):
        print("\n[ 결제 ] 페이지 입니다.")
        print("\n1. 현금 결제 2. 카드 결제 0. 뒤로 가기")
        passageSelect = int(input("? "))

        if passageSelect == 1:
            self.cashForm()
            print("\n이용해주셔서 감사합니다.\n")
            
        elif passageSelect == 2:
            self.cardForm()
            print("\n이용해주셔서 감사합니다.\n")

    # 현금 결제 양식 함수
    def cashForm(self):
        print("\n총합 급액 : " + str(self.cart.getCartPrice()))

        while True:
            print("\n얼마를 넣으시겠습니까")
            self.money += int(input("? "))

            if (self.money < self.cart.getCartPrice()):
                print("\n금액이 부족합니다.")
            else:
                self.rest = self.money - self.cart.getCartPrice()
                print("\n결제 완료")
                break

        self.printReceipt("cash")

    # 카드 결제 양식 함수
    def cardForm(self):
        print("\n총합 급액 : " + str(self.cart.getCartPrice()))
        print("IC카드 인식 중 입니다.")
        print("\n결제 완료")

        self.printReceipt("card")

    # 영수증 출력 함수
    def printReceipt(self, method):
        print("\n====== 영수증 ======")
        print("\n* 주문 내역")
        self.cart.printCart()

        print("\n* 주문 정보")
        self.cart.printCartInfo()

        print("\n* 결제 내용")
        if method == "cash":
            print("현금 결제")
            print("투입 금액 : " + str(self.money))
            print("결제 금액 : " + str(self.cart.getCartPrice()))
            print("반환 금액 : " + str(self.rest))
        elif method == "card":
            print("카드 결제")
            print("결제 금액 : " + str(self.cart.getCartPrice()))
