import datetime
import time


current = 0 # 이자 시간


money = int(input("돈을 입력해주세요 : "))

game = 1 # 게임 지속 유무

sale_name = ["커피","음료수","과자","아이스크림"]
sale_money = [100,500,1000,600]
loan_money=0 # 빌린 돈 원금


while(game):

    if loan_money:
        now = datetime.datetime.now()
        time_s = (now - current).seconds
        time_bt = time_s/10
        minus_money = 100*round((time_bt))
        money = money - minus_money
        current = datetime.datetime.now()
        if money <0:
            temp = money
            money =0
            loan_money = loan_money + -(temp)
    print("현재 잔액은 %d원이며 빚은 %d원 있습니다." %(money,loan_money))
        

        
    print("(1) 커피 : 100 /(2) 음료수 : 500 /(3) 과자: 1000 /(4) 아이스크림 : 600/(8282) 돈 벌기 /(999) 대출 갚기")

    condition = int(input("종류를 번호로 입력 : "))

    if condition == 8282:
        print("광고를 시작합니다. 광고 한편에 500원이 지급되며 30초 걸립니다.")

        print("")
        print("   비트 캠프  ")
        print("     교 육   ")
        print("   커리 큘럼   ")
        print("   인공 지능   ")
        print("")
        time.sleep(30)
        money += 500
        print("광고가 끝났습니다. 현재 잔액은 %d입니다." %money)
        continue
            
        
        

    if condition == 999:
        print("안녕하세요 고객님 원금을 갚으러 오셨어요??")
        print("빌려가신 돈(원금)은 총 %d원 입니다." %loan_money)

        dept = int(input("반환할 원금을 입력해주세요 : "))
        loan_money = loan_money - dept
        if loan_money < 0:
            print("돈을 더 주셨네요?? 보너스 감사합니다")
            loan_money=0
            continue
        elif loan_money ==0:
            print("원금을 다 갚으셨습니다 고객님~")
            loan_money=0
            continue
        else:
            print("원금이 아직 %d원 남았습니다." %loan_money)
            continue

    
    how = int(input("%s를(을) 몇개 사시겠습니까?" %sale_name[condition-1]))

    money_temp = money - (sale_money[condition-1]*how)

    
    if money_temp <0:
        print("돈이 부족합니다.")

        while(True):
            print("안녕하세요 고객님 대출 받으시겠어요??")
            loan = input("대출이 가능합니다 하시겠습니까?? (Y/N): ")
            if loan == 'Y' or loan=='y':
                current = datetime.datetime.now()
                loan_money = int(input("대출을 얼마를 하고 싶습니까?"))
                money += loan_money
                print("%d원을 빌리시고 총 %d원 있으십니다." %(loan_money, money))
                print("이자로 10초에 100원씩 차감됩니다.")
                print("빨리 원금을 갚아주세요")
                break
            elif loan == 'N' or loan=='n':
                break
            else :
                print("잘못 입력하셨습니다. 다시 입력해주세요")
        continue
        
    else:
        money = money_temp
        print("%s를(을) %d개 구입이 완료되었습니다." %(sale_name[condition-1], how))
        print("현재 남은 돈 %d" %money)


    while(True):
        repeat = input("더 구입하시겠습니까?? (Y/N): ")
        if repeat == 'Y' or repeat=='y':
            break
        elif repeat == 'N' or repeat=='n' :
            print("자판기를 종료합니다.")

            if loan_money:
                print("대출이 남아있으면 종료 못합니다 고객님")
                print("갚으셔야 할 돈은 %d원 입니다." %loan_money)
                break
            else:
                print("자판기를 종료합니다.")
                game = 0
                break
        else :
            print("잘못 입력하셨습니다. 다시 입력해주세요")
