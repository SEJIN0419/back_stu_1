while(True):
    print("온도를 입력하세요(100을 입력하면 종료합니다.): ",end='')
    temp = int(input())
    if temp == 100:
        print("온도 알림을 종료합니다.")
        break
    elif temp < 5:
        print("오늘은 매우 춥습니다.")
    else:
        print("따뜻합니다!")
    









