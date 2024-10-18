import random

def check_balance(bb):
    print('Ваш баланс:',bb)

def new_round(stavka):
    suits = {0:'♠',1:'♥',2:'♦',3:'♣'}
    change_to_JQKT = {11:'J',12:'Q',13:'K',14:'T'}
    all_cards = []
    for i in range(52):
        if i//4+2 < 11:
            all_cards.append(str(i//4+2)+suits[i%4])
        else:
            all_cards.append(change_to_JQKT[i//4+2]+suits[i%4])
    all_cards_price = []
    for i in range(52):
        if i//4+2 < 11:
            all_cards_price.append(i//4+2)
        elif 10 < i//4+2 < 14:
            all_cards_price.append(10)
        else:
            all_cards_price.append(1)


    def add_card_to_players_hand(number,cards):
        if cards[number][0] == '1':
            karta_zagotovka = [' ---- ','|{} |','|    |','|    |',' ---- ']
        else:
            karta_zagotovka = [' ---- ','|{}  |','|    |','|    |',' ---- ']
        for i in range(len(players_hand)):
            players_hand[i].append(karta_zagotovka[i].format(cards[number]))

    def add_card_to_casino_hand(number,cards):
        if cards[number][0] == '1':
            karta_zagotovka = [' ---- ','|{} |','|    |','|    |',' ---- ']
        else:
            karta_zagotovka = [' ---- ','|{}  |','|    |','|    |',' ---- ']
        for i in range(len(casino_hand)):
            casino_hand[i].append(karta_zagotovka[i].format(cards[number]))

    def show_hand(hh):
        for r in hh:
            print(*r)

    def show_table(cs,ps,cash):
        print('=====================')
        print('СТАВКА:',cash)
        show_hand(casino_hand)
        print('Крупье:',cs)
        for _ in range(3):
            print()
        print('Вы:',ps)
        show_hand(players_hand)
        print('=====================')

    def take_player(ss):
        a = random.randrange(len(all_cards_round))
        add_card_to_players_hand(a,all_cards_round)
        all_cards_round.pop(a)
        ss += all_cards_price_round.pop(a)
        return ss

    def take_casino(ss):
        a = random.randrange(len(all_cards_round))
        add_card_to_casino_hand(a,all_cards_round)
        all_cards_round.pop(a)
        ss += all_cards_price_round.pop(a)
        return ss

    players_hand = [[],[],[],[],[]]
    casino_hand = [[],[],[],[],[]]
    all_cards_round = all_cards.copy()
    all_cards_price_round = all_cards_price.copy()
    player_sum = 0
    casino_sum = 0

    player_sum = take_player(player_sum)
    player_sum = take_player(player_sum)
    casino_sum = take_casino(casino_sum)

    show_table(casino_sum,player_sum,stavka)
    flg = True
    flg2 = True
    while flg:
        if player_sum == 21:
            print('ОГО! Повезло')
            print('=====================')
            print('ХОД КРУПЬЕ, нажмите ENTER для хода')
            flg = False
        else:
            print('Хотите взять карту?')
            print('[Y]/[N] --> ',end = '')
            turn = input()
            if turn == 'N':
                print('Главное вовремя остановиться')
                print('=====================')
                print('ХОД КРУПЬЕ, нажмите ENTER для хода')
                flg = False
            elif turn == 'Y':
                player_sum = take_player(player_sum)
                show_table(casino_sum,player_sum,stavka)
                if player_sum > 21:
                    flg = False
                    flg2 = False
                    print('ВЫ ПРОИГРАЛИ')
                    print('Ставка',stavka,'сгорает')
                    print('=====================')
                    print('КОНЕЦ РАУНДА')
                    print('=====================')
                    return -stavka
            else:
                print('Неопознанный символ')
                show_table(casino_sum,player_sum,stavka)
    while flg2:
        if casino_sum < 17:
            input()
            casino_sum = take_casino(casino_sum)
            show_table(casino_sum,player_sum,stavka)
            if casino_sum > 21:
                print('ВЫ ВЫИГРАЛИ')
                print('Ставка',stavka,'удваивается')
                print('=====================')
                print('КОНЕЦ РАУНДА')
                print('=====================')
                flg2 = False
                return stavka
        else:
            if casino_sum > player_sum:
                print('ВЫ ПРОИГРАЛИ')
                print('Ставка',stavka,'сгорает')
                print('=====================')
                print('КОНЕЦ РАУНДА')
                print('=====================')
                flg2 = False
                return -stavka
            elif casino_sum == player_sum:
                print('НИЧЬЯ')
                print('Ставка',stavka,'возвращается')
                print('=====================')
                print('КОНЕЦ РАУНДА')
                print('=====================')
                flg2 = False
                return 0
            else:
                print('ВЫ ВЫИГРАЛИ')
                print('Ставка',stavka,'удваивается')
                print('=====================')
                print('КОНЕЦ РАУНДА')
                print('=====================')
                flg2 = False
                return stavka



print('Внесите баланс: ',end = '')
balance = int(input())

ff = True
while balance > 100 and ff:
    check_balance(balance)
    print('Хотите сыграть?')
    print('[Y]/[N] --> ',end = '')
    ans = input()
    if ans == 'N':
        ff = False
        check_balance(balance)
        print('=====================')
        print('КОНЕЦ ИГРЫ')
        print('=====================')
    elif ans == 'Y':
        print('Поставьте ставку: ',end = '')
        new_stavka = int(input())
        if new_stavka <= balance:
            balance += new_round(new_stavka)
        else:
            print('столько на балансе нет!')
    else:
        print('Неопознанный символ')
if balance < 100:
    check_balance(balance)
    print('=====================')
    print('КОНЕЦ ИГРЫ')
    print('=====================')