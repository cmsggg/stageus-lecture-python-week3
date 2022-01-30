class Payment:

    # 생성자. cart 객체 멤버 변수와 금액 관련 멤버 변수 생성
    def __init__(self, cart):
        self.cart = cart
        self.totalPrice = self.cart.getTotalPrice()
        self.money = 0
        self.rest = 0

    # 현금 결제 출력 함수
    def cash(self):
        print("\n총합 급액 : " + str(self.totalPrice))

        while True:
            print("\n얼마를 넣으시겠습니까")
            self.money += int(input("? "))

            if (self.money < self.totalPrice):
                print("\n금액이 부족합니다.")
            else:
                self.rest = self.money - self.totalPrice
                print("\n결제 완료")
                break

        self.printReceipt("cash")

    # 카드 결제 출력 함수
    def card(self):
        print("\n총합 급액 : " + str(self.totalPrice))
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
            print("결제 금액 : " + str(self.totalPrice))
            print("반환 금액 : " + str(self.rest))
        elif method == "card":
            print("카드 결제")
            print("결제 금액 : " + str(self.totalPrice))
