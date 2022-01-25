from Menu import Menu

class MenuList:

    # 생성자. 메뉴 목록 멤버 변수 생성
    def __init__(self):
        
        # 메뉴 데이터 셋 초기화
        self.menuInfoList = [
            [
                ["커피", "아메리카노", 3200, 100],
                ["커피", "카페 라떼", 3700, 100],
                ["커피", "카푸치노", 3700, 100],
                ["커피", "카페 모카", 3900, 100],
                ["커피", "카라멜 마끼아또", 3900, 100],
                ["커피", "바닐라 라떼", 3900, 100],
                ["커피", "화이트 초콜릿 모카", 3900, 100]
            ],
            [
                ["음료", "에이드", 3800, 100],
                ["음료", "과일 주스", 4200, 100],
                ["음료", "쉐이크", 4300, 100],
                ["음료", "과일차", 3800, 100],
                ["음료", "아이스티", 2500, 100],
                ["음료", "녹차 & 홍차", 2800, 100],
                ["음료", "캐모마일", 3000, 100],
                ["음료", "페퍼민트티", 3000, 100],
                ["음료", "밀크티", 3800, 100]
            ],
            [
                ["플랫치노", "커피", 3500, 100],
                ["플랫치노", "복숭아", 3500, 100],
                ["플랫치노", "망고", 3500, 100],
                ["플랫치노", "모카", 3800, 100],
                ["플랫치노", "카라멜", 3800, 100],
                ["플랫치노", "자몽", 3800, 100],
                ["플랫치노", "녹차", 4200, 100],
                ["플랫치노", "초콜릿", 4200, 100],
                ["플랫치노", "민트 초콜릿", 4200, 100],
                ["플랫치노", "요거트", 4200, 100]
            ],
            [
                ["우유", "흑당 라떼", 3300, 100],
                ["우유", "이곡 라떼", 3500, 100],
                ["우유", "초콜릿", 3700, 100],
                ["우유", "녹차 라떼", 3700, 100],
                ["우유", "토피 넛 라떼", 4000, 100],
                ["우유", "민트 초콜릿", 4000, 100],
                ["우유", "고구마 라떼", 4000, 100]
            ]
        ]

        # 메뉴 목록 멤버 변수 초기화
        self.menuList = []
        for index in range(0, len(self.menuInfoList)):
            tmpList = []
            for index2 in range(0, len(self.menuInfoList[index])):
                tmpMenu = Menu(self.menuInfoList[index][index2][0], self.menuInfoList[index][index2][1], self.menuInfoList[index][index2][2], self.menuInfoList[index][index2][3])
                tmpList.append(tmpMenu)
            self.menuList.append(tmpList)

    # 카테고리의 목록을 출력하는 함수
    def printType(self):
        for index in range(0, len(self.menuList)):
            print(str(index+1) + ". ", end="")
            self.getMenu(index, 0).printMenu("type")
        print("0. 뒤로가기")

    # 해당 카테고리의 메뉴 목록을 출력하는 함수
    def printMenuList(self, typeIndex):
        for index in range(0, len(self.menuList[typeIndex])):
            print(str(index+1) + ". ", end="")
            self.getMenu(typeIndex, index).printMenu("menu")
        print("0. 뒤로가기")

    # 메뉴 반환 함수
    def getMenu(self, typeIndex, menuIndex):
        return self.menuList[typeIndex][menuIndex]