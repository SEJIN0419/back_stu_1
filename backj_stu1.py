menu = int(input("메뉴 선택 1.온도알림이 2.거스름돈 계산기 :"))
while(True):
    if menu == 1:
        temp = int(input("온도를 입력하세요(-1을 입력하면 메뉴로 돌아갑니다.): "))
        if temp == -1:
            print("온도 알림을 종료합니다.")
            break
        elif temp < 10:
            print("오늘은 매우 춥습니다. 긴옷을 준비하세요!")
        else:
            print("따뜻합니다!")

    if menu == 2:
        payment = int(input("총 구입 금액을 입력하세요(-1을 입력하면 종료합니다) : "))
        if payment == -1:
            print("메뉴로 돌아갑니다.")
            break
        else:
            coin = int(input("지불한 금액을 입력하세요 : "))
            total = payment - coin
            print(f"총 거스름돈은 {total}입니다.")
            fifty = total // 50000 # 5만원
            ten = (total % 50000) // 10000 # 만원
            five = (total % 10000) // 5000 # 오천원
            one = (total % 5000) // 1000 # 천원
            back = (total % 1000) // 100 # 백원
            print(f"거스름돈은 : 5만원 {fifty}장, 만원 {ten}장, 오천원 {five}장, 천원 {one}장, 백원 {back}개 입니다")
