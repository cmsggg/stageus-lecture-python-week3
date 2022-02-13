# Database class는 추후 데이터베이스와 통신하는 class로, 현 시점에선 고정 데이터를 넣어 사용.
# 데이터베이스와 관련된 기능이 포함된 class
# 데이터베이스 출력 등의 로직 선언

# ※ 모듈화를 위한 Class 설계

class Database:
        
    # 생성자. 카테고리와 메뉴 목록 관련 멤버 변수 선언
    def __init__(self):

        self.categoryList = ["커피", "음료", "플랫치노", "우유"]
        self.menuList = [
            [
                [self.categoryList[0], "아메리카노", 3200],
                [self.categoryList[0], "카페 라떼", 3700],
                [self.categoryList[0], "카푸치노", 3700],
                [self.categoryList[0], "카페 모카", 3900],
                [self.categoryList[0], "카라멜 마끼아또", 3900],
                [self.categoryList[0], "바닐라 라떼", 3900],
                [self.categoryList[0], "화이트 초콜릿 모카", 3900]
            ],
            [
                [self.categoryList[1], "에이드", 3800],
                [self.categoryList[1], "과일 주스", 4200],
                [self.categoryList[1], "쉐이크", 4300],
                [self.categoryList[1], "과일차", 3800],
                [self.categoryList[1], "아이스티", 2500],
                [self.categoryList[1], "녹차 & 홍차", 2800],
                [self.categoryList[1], "캐모마일", 3000],
                [self.categoryList[1], "페퍼민트티", 3000],
                [self.categoryList[1], "밀크티", 3800]
            ],
            [
                [self.categoryList[2], "복숭아", 3500],
                [self.categoryList[2], "망고", 3500],
                [self.categoryList[2], "모카", 3800],
                [self.categoryList[2], "카라멜", 3800],
                [self.categoryList[2], "자몽", 3800],
                [self.categoryList[2], "녹차", 4200],
                [self.categoryList[2], "초콜릿", 4200],
                [self.categoryList[2], "민트 초콜릿", 4200],
                [self.categoryList[2], "요거트", 4200]
            ],
            [
                [self.categoryList[3], "흑당 라떼", 3300],
                [self.categoryList[3], "이곡 라떼", 3500],
                [self.categoryList[3], "초콜릿", 3700],
                [self.categoryList[3], "녹차 라떼", 3700],
                [self.categoryList[3], "토피 넛 라떼", 4000],
                [self.categoryList[3], "민트 초콜릿", 4000],
                [self.categoryList[3], "고구마 라떼", 4000]
            ]
        ]

    # 카테고리 목록 출력 함수
    def printCategoryList(self):
        for index in range(0, self.getCategoryCount()):
            print(str(index+1) + ". " + self.categoryList[index])

    # 카테고리 개수 반환 함수
    def getCategoryCount(self):
        return len(self.menuList)

    # 메뉴 목록 출력 함수
    def printMenuList(self, categoryIndex):
        for index in range(0, self.getMenuCount(categoryIndex)):
            print(str(index+1) + ". ", end="")
            self.printMenu(categoryIndex, index)

    # 메뉴 개수 반환 함수
    def getMenuCount(self, categoryIndex):
        return len(self.menuList[categoryIndex])

    # 메뉴 반환 함수
    def getMenu(self, categoryIndex, menuIndex):
        return self.menuList[categoryIndex][menuIndex]

    # 메뉴 출력 함수
    def printMenu(self, categoryIndex, index):
        tmpData = self.menuList[categoryIndex][index]
        print("%-6s" % tmpData[0], end="")
        print("%-20s" % tmpData[1], end="")
        print("%-6d" % tmpData[2])