menu = int(input("메뉴 선택 1.온도알림이 2.거스름돈 계산기 :"))
while(True):
    if menu == 1:
        temp = input("온도를 입력하세요(exit 을 입력하면 메뉴로 돌아갑니다.): ")
        if temp == 'exit':
            print("온도 알림을 종료합니다.")
            break
        elif int(temp) < 0:
            print("영하의 날씨 입니다 매우 춥습니다! 두꺼운 옷을 챙기세요!")
        elif int(temp) < 10:
            print("오늘은 춥습니다. 따뜻한 긴옷을 준비하세요!")
        elif int(temp) < 30:
            print("적당한 날씨 입니다!")
        else:
            print("매우더운 날씨 입니다! 건강 유의하세요!")

    if menu == 2:
        payment = input("총 구입 금액을 입력하세요(exit을 입력하면 종료합니다) : ")
        if payment == 'exit':
            print("거스름돈 계산기를 종료합니다.")
            break
        else:
            coin = int(input("지불한 금액을 입력하세요 : "))
            total = int(payment) - coin
            print(f"총 거스름돈은 {total}입니다.")
            fifty = total // 50000 # 5만원
            ten = (total % 50000) // 10000 # 만원
            five = (total % 10000) // 5000 # 오천원
            one = (total % 5000) // 1000 # 천원
            back = (total % 1000) // 100 # 백원
            print(f"거스름돈은 : 5만원 {fifty}장, 만원 {ten}장, 오천원 {five}장, 천원 {one}장, 백원 {back}개 입니다")
