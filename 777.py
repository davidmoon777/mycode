import random
import time

# 시작 금액
seedmoney = 10_000_000  
initial_money = seedmoney  
user_info = {
    "username": None,
    "password": None,
    "account_number": None,
    "account_password": None
}

print("🎰 슬롯 머신 & 🃏 맞고 & 🎴 섯다 & ♠ 블랙잭 & ⚖ 홀짝 카지노에 오신 걸 환영합니다! 🎰\n")

# 회원가입
def sign_up():
    global user_info
    print("\n🔑 회원가입을 시작합니다.")
    user_info["username"] = input("아이디 입력: ")

    while True:
        try:
            user_info["password"] = input("비밀번호 입력 (4자리 숫자): ")
            if not user_info["password"].isdigit() or len(user_info["password"]) != 4:
                raise ValueError
            break
        except ValueError:
            print("❌ 비밀번호는 4자리 숫자로 입력하세요!")

    while True:
        try:
            user_info["account_number"] = input("계좌번호 입력 (숫자만): ")
            if not user_info["account_number"].isdigit():
                raise ValueError
            break
        except ValueError:
            print("❌ 계좌번호는 숫자로만 입력하세요!")

    while True:
        try:
            user_info["account_password"] = input("계좌 비밀번호 입력 (4자리 숫자): ")
            if not user_info["account_password"].isdigit() or len(user_info["account_password"]) != 4:
                raise ValueError
            break
        except ValueError:
            print("❌ 계좌 비밀번호는 4자리 숫자로 입력하세요!")

    print("회원가입이 완료되었습니다! 🎉")


sign_up()
# 사용자 정보 확인
def view_user_info():
    global user_info, seedmoney
    print(f"\n👤 아이디: {user_info['username']}")
    print(f"💰 현재 보유 금액: {seedmoney:,}원")

# 슬롯 머신 게임
def play_slot_machine():
    global seedmoney

    while seedmoney > 0:
        print(f"\n💰 현재 보유 금액: {seedmoney:,}원")
        try:
            money = int(input("🎲 배팅 금액 입력 (0 입력 시 게임 변경): "))
            if money == 0:
                return
            if money < 0 or money > seedmoney:
                print("❌ 올바른 금액을 입력하세요.")
                continue
        except ValueError:
            print("❌ 숫자로 입력하세요.")
            continue

        seedmoney -= money

        a, b, c = random.choices(
            [7, 7, 7, 1, 2, 3, 4, 5, 6, 8, 9],
            weights=[1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6],
            k=3
        )

        print(f"\n🎰 | {a} | {b} | {c} | 🎰\n")

        if a == 7 and b == 7 and c == 7:
            winnings = money * 50
            seedmoney += winnings
            print(f"🎉 777 잭팟 당첨! {winnings:,}원 획득!")
        elif a == b == c:
            winnings = money * 10
            seedmoney += winnings
            print(f"🔥 잭팟 당첨! {winnings:,}원 획득!")
        elif a == b or b == c or a == c:
            winnings = money * 1.5
            seedmoney += int(winnings)
            print(f"⭐ 두 개 일치! {winnings:,.0f}원 획득!")
        else:
            print("❌ 꽝! 다음 기회를 노려보세요!")
        
        print(f"💰 현재 보유 금액: {seedmoney:,}원")

        choice = input("🎮 게임을 계속하시겠습니까? (1: 계속, 0: 홈으로 돌아가기): ").strip()
        if choice == "0":
            return

# 섯다 게임
def play_seotda():
    global seedmoney
    
    while seedmoney > 0:
        print(f"\n🎴 섯다 게임 시작! (💰 현재 보유 금액: {seedmoney:,}원)")
        try:
            bet = int(input("💰 배팅 금액 입력 (0 입력 시 게임 변경): "))
            if bet == 0:
                return
            if bet < 0 or bet > seedmoney:
                print("❌ 올바른 금액을 입력하세요!")
                continue
        except ValueError:
            print("❌ 숫자로 입력하세요.")
            continue

        seedmoney -= bet

        player_hand = random.sample(range(1, 11), 2)
        dealer_hand = random.sample(range(1, 11), 2)
        print(f"🎴 당신의 패: {player_hand}")

        while True:
            action = input("1️⃣ 계속한다 | 2️⃣ 죽는다\n👉 선택: ").strip()
            if action == "1":
                break
            elif action == "2":
                penalty = bet // 2
                seedmoney += penalty
                print(f"🏳️ 죽었습니다! 배팅금 절반({penalty:,}원) 돌려받음")
                break
            else:
                print("❌ 잘못된 입력입니다. 1 또는 2를 입력하세요.")

        if action == "2":
            continue

        player_score = sum(player_hand) % 10
        dealer_score = sum(dealer_hand) % 10

        print(f"🃏 딜러의 패: {dealer_hand}")

        if player_score > dealer_score:
            winnings = bet * 2
            seedmoney += winnings
            print(f"🎉 승리! {winnings:,}원 획득!")
        elif player_score == dealer_score:
            seedmoney += bet
            print("😐 무승부! 배팅금을 돌려받음")
        else:
            print(f"💸 패배! {bet:,}원 잃음")

        print(f"💰 현재 보유 금액: {seedmoney:,}원")

        choice = input("🎮 게임을 계속하시겠습니까? (1: 계속, 0: 홈으로 돌아가기): ").strip()
        if choice == "0":
            return

# 맞고 게임
def play_matgo():
    global seedmoney

    while seedmoney > 0:
        print(f"\n🃏 맞고 게임 시작! (💰 현재 보유 금액: {seedmoney:,}원)")
        try:
            bet = int(input("💰 배팅 금액 입력 (0 입력 시 게임 변경): "))
            if bet == 0:
                return
            if bet < 0 or bet > seedmoney:
                print("❌ 올바른 금액을 입력하세요!")
                continue
        except ValueError:
            print("❌ 숫자로 입력하세요.")
            continue

        seedmoney -= bet

        player_hand = random.sample(range(1, 11), 3)
        dealer_hand = random.sample(range(1, 11), 3)
        print(f"🃏 당신의 패: {player_hand}")
        print(f"🃏 딜러의 패: {dealer_hand}")

        player_score = sum(player_hand) % 10
        dealer_score = sum(dealer_hand) % 10

        print(f"🏅 당신의 점수: {player_score}")
        print(f"🏅 딜러의 점수: {dealer_score}")

        if player_score > dealer_score:
            winnings = bet * 2
            seedmoney += winnings
            print(f"🎉 승리! {winnings:,}원 획득!")
        elif player_score == dealer_score:
            seedmoney += bet
            print("😐 무승부! 배팅금을 돌려받음")
        else:
            print(f"💸 패배! {bet:,}원 잃음")

        print(f"💰 현재 보유 금액: {seedmoney:,}원")

        choice = input("🎮 게임을 계속하시겠습니까? (1: 계속, 0: 홈으로 돌아가기): ").strip()
        if choice == "0":
            return

# 블랙잭 게임
def play_blackjack():
    global seedmoney

    while seedmoney > 0:
        print(f"\n♠ 블랙잭 게임 시작! (💰 현재 보유 금액: {seedmoney:,}원)")
        try:
            bet = int(input("💰 배팅 금액 입력 (0 입력 시 게임 변경): "))
            if bet == 0:
                return
            if bet < 0 or bet > seedmoney:
                print("❌ 올바른 금액을 입력하세요!")
                continue
        except ValueError:
            print("❌ 숫자로 입력하세요.")
            continue

        seedmoney -= bet

        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        player_hand = random.sample(deck, 2)
        dealer_hand = random.sample(deck, 2)

        print(f"♠ 당신의 패: {player_hand} (합: {sum(player_hand)})")
        print(f"♠ 딜러의 패: [{dealer_hand[0]}, ?]")

        while sum(player_hand) < 21:
            action = input("1️⃣ 히트 | 2️⃣ 스탠드\n👉 선택: ").strip()
            if action == "1":
                new_card = random.choice(deck)
                player_hand.append(new_card)
                deck.remove(new_card)
                print(f"♠ 새 카드: {new_card}, 현재 패: {player_hand} (합: {sum(player_hand)})")
                if sum(player_hand) > 21 and 11 in player_hand:
                    player_hand[player_hand.index(11)] = 1
                    print(f"♠ 에이스가 1로 조정됨: {player_hand} (합: {sum(player_hand)})")
            elif action == "2":
                break
            else:
                print("❌ 잘못된 입력입니다. 1 또는 2를 입력하세요.")

        player_total = sum(player_hand)
        if player_total > 21:
            print(f"♠ 버스트! 패배! {bet:,}원 잃음")
            print(f"💰 현재 보유 금액: {seedmoney:,}원")
            choice = input("🎮 게임을 계속하시겠습니까? (1: 계속, 0: 홈으로 돌아가기): ").strip()
            if choice == "0":
                return
            continue

        print(f"♠ 딜러의 패: {dealer_hand} (합: {sum(dealer_hand)})")
        while sum(dealer_hand) < 17:
            new_card = random.choice(deck)
            dealer_hand.append(new_card)
            deck.remove(new_card)
            print(f"♠ 딜러가 뽑음: {new_card}, 현재 패: {dealer_hand} (합: {sum(dealer_hand)})")
            if sum(dealer_hand) > 21 and 11 in dealer_hand:
                dealer_hand[dealer_hand.index(11)] = 1
                print(f"♠ 딜러의 에이스가 1로 조정됨: {dealer_hand} (합: {sum(dealer_hand)})")

        dealer_total = sum(dealer_hand)

        if dealer_total > 21:
            winnings = bet * 2
            seedmoney += winnings
            print(f"♠ 딜러 버스트! 승리! {winnings:,}원 획득!")
        elif player_total > dealer_total:
            winnings = bet * 2
            seedmoney += winnings
            print(f"♠ 승리! {winnings:,}원 획득!")
        elif player_total == dealer_total:
            seedmoney += bet
            print("😐 무승부! 배팅금을 돌려받음")
        else:
            print(f"💸 패배! {bet:,}원 잃음")

        print(f"💰 현재 보유 금액: {seedmoney:,}원")
        choice = input("🎮 게임을 계속하시겠습니까? (1: 계속, 0: 홈으로 돌아가기): ").strip()
        if choice == "0":
            return

# 홀짝 게임
def play_holjak():
    global seedmoney

    while seedmoney > 0:
        print(f"\n⚖ 홀짝 게임 시작! (💰 현재 보유 금액: {seedmoney:,}원)")

        while True:
            try:
                bet = input("💰 배팅 금액 입력 (0 입력 시 게임 변경): ")
                if not bet.isdigit():
                    raise ValueError
                bet = int(bet)
                if bet == 0:
                    return
                if bet < 0 or bet > seedmoney:
                    print("❌ 올바른 금액을 입력하세요!")
                    continue
                break
            except ValueError:
                print("❌ 숫자로 입력하세요!")

        seedmoney -= bet

        choice = input("홀(1) 또는 짝(2)을 선택하세요: ")
        if choice not in ['1', '2']:
            print("❌ 잘못된 입력입니다. 홀(1) 또는 짝(2)을 입력하세요.")
            seedmoney += bet
            continue

        # 카지노가 이길 확률을 추가 (2% 확률로 카지노가 승리)
        outcome = random.choices(["홀", "짝", "카지노 승리"], weights=[49, 49, 2])[0]

        print(f"🎰 결과: {outcome}")

        if outcome == "카지노 승리":
            print(f"💸 카지노의 승리! {bet:,}원 잃음")

        elif (outcome == "홀" and choice == "1") or (outcome == "짝" and choice == "2"):
            winnings = int(bet * 1.9)  # 1.9배 배당률 적용
            seedmoney += winnings
            print(f"🎉 승리! {winnings:,}원 획득!")
        else:
            print(f"💸 패배! {bet:,}원 잃음")

        print(f"💰 현재 보유 금액: {seedmoney:,}원")

        choice = input("🎮 게임을 계속하시겠습니까? (1: 계속, 0: 홈으로 돌아가기): ").strip()
        if choice == "0":
            return

# 출금 기능
def withdraw():
    global seedmoney
    min_withdraw = initial_money * 1.5  
    
    if seedmoney < min_withdraw:
        print(f"❌ 출금은 초기 금액의 150% ({min_withdraw:,}원) 이상일 때만 가능합니다.")
        return
    
    print(f"\n💸 현재 보유 금액: {seedmoney:,}원 (출금 가능 최소 금액: {min_withdraw:,}원)")

    # 계좌번호 입력
    account = input("🏦 계좌번호 입력 (숫자만, 예: 1234567890): ").strip()
    if account != user_info["account_number"]:
        print(f"❌ 입력하신 계좌번호가 다릅니다. 정말 출금하시겠습니까? (계좌번호: {user_info['account_number']})")
        return
    
    # 비밀번호 입력
    password = input("🔒 비밀번호 입력: ").strip()
    if password != user_info["account_password"]:
        print(f"❌ 입력하신 비밀번호가 다릅니다. 정말 출금하시겠습니까? (비밀번호: {user_info['account_password']})")
        return
    
    try:
        amount = int(input("💰 출금 금액 입력: "))
        if amount <= 0 or amount > seedmoney:
            print("❌ 올바른 출금 금액을 입력하세요.")
            return
        
        confirm = input("출금하시겠습니까? (출금하기 입력): ").strip()
        if confirm == "출금하기":
            seedmoney -= amount
            print(f"💸 {amount:,}원이 계좌 {account}로 출금되었습니다!")
            print(f"💰 남은 금액: {seedmoney:,}원")
        else:
            print("❌ 출금이 취소되었습니다.")
    except ValueError:
        print("❌ 숫자로 입력하세요.")

# 게임 시작
while seedmoney > 0:
    print("\n🎰 슬롯 머신 (1) | 🃏 맞고 (2) | 🎴 섯다 (3) | ♠ 블랙잭 (4) | ⚖ 홀짝 (5) | 💸 출금 (6) | 👤 사용자 정보 (7) | 🚪 종료 (0)")
    choice = input("게임을 선택하세요: ").strip()

    if choice == "1":
        play_slot_machine()
    elif choice == "2":
        play_matgo()
    elif choice == "3":
        play_seotda()
    elif choice == "4":
        play_blackjack()
    elif choice == "5":
        play_holjak()
    elif choice == "6":
        withdraw()
    elif choice == "7":
        view_user_info()
    elif choice == "0":
        print("\n🚪 게임 종료! 남은 돈:", seedmoney, "원")
        break
    else:
        print("❌ 잘못된 입력입니다. 다시 선택하세요.")

if seedmoney <= 0:
    print("\n💸 파산! 카지노의 승리! 💸")
