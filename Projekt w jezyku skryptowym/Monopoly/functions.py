import random 

# TRADE MENU DEFAULT
def trade_menu_clear(trade_menu):
    trade_menu.host_card_1 = 0
    trade_menu.host_card_2 = 0
    trade_menu.host_card_3 = 0
    trade_menu.host_card_1_name = ''
    trade_menu.host_card_2_name = ''
    trade_menu.host_card_3_name = ''
    trade_menu.trader_card_1 = 0
    trade_menu.trader_card_2 = 0
    trade_menu.trader_card_3 = 0
    trade_menu.trader_card_1_name = ''
    trade_menu.trader_card_2_name = ''
    trade_menu.trader_card_3_name = ''
    trade_menu.host_money = 0
    trade_menu.trader_money = 0
    trade_menu.host_name = 0
    trade_menu.trader_name = '_'
    trade_menu.find_trader = 0
    trade_menu.money = 0
    trade_menu.show_money = 0
 
# ACCEPT TRADE
def accept_trade(fields,players,current_player,display_card,trade_menu,trader):
    if trade_menu.host_card_1 != 0:
        fields[trade_menu.host_card_1].owner = int(trade_menu.trader_name)
    if trade_menu.host_card_2 != 0:
        fields[trade_menu.host_card_2].owner = int(trade_menu.trader_name)
    if trade_menu.host_card_3 != 0:
        fields[trade_menu.host_card_3].owner = int(trade_menu.trader_name)
    if trade_menu.host_money > 0:
        players[current_player].balance -= trade_menu.host_money
        players[int(trade_menu.trader_name)].balance += trade_menu.host_money

    if trade_menu.trader_card_1 != 0:
        fields[trade_menu.trader_card_1].owner = current_player
    if trade_menu.trader_card_2 != 0:
        fields[trade_menu.trader_card_2].owner = current_player
    if trade_menu.trader_card_2 != 0:
        fields[trade_menu.trader_card_2].owner = current_player
    if trade_menu.trader_money > 0:
        players[current_player].balance += trade_menu.trader_money
        players[int(trade_menu.trader_name)].balance -= trade_menu.trader_money


# TRADE MONEY 
def trade_host_money(fields,players,current_player,display_card,trade_menu,get_money):
    trade_menu.host_money=trade_menu.money
    trade_menu.money=0
    get_money = 0
    trade_menu.show_money = 0

def trade_trader_money(fields,players,current_player,display_card,trade_menu,get_money):
    trade_menu.trader_money=trade_menu.money
    trade_menu.money=0
    get_money = 0
    trade_menu.show_money = 0

# TRADE CARDS
def trade_host_fields(fields,players,current_player,display_card,trade_menu):
    if fields[display_card.actual_card].owner == current_player:
                    if trade_menu.host_card_1 == 0 and fields[display_card.actual_card].house_number == 0:
                        trade_menu.host_card_1 = display_card.actual_card
                        trade_menu.host_card_1_name = display_card.name
                    if trade_menu.host_card_2 == 0 and fields[display_card.actual_card].house_number == 0 \
                        and fields[display_card.actual_card].position != trade_menu.host_card_1:
                        trade_menu.host_card_2 = display_card.actual_card
                        trade_menu.host_card_2_name = display_card.name
                    if trade_menu.host_card_3 == 0 and fields[display_card.actual_card].house_number == 0 \
                        and fields[display_card.actual_card].position != trade_menu.host_card_2 and fields[display_card.actual_card].position != trade_menu.host_card_1:
                        trade_menu.host_card_3 = display_card.actual_card
                        trade_menu.host_card_3_name = display_card.name

def trade_trader_fields(fields,players,current_player,display_card,trade_menu,trader):
    if fields[display_card.actual_card].owner == trader:
                    if trade_menu.trader_card_1 == 0 and fields[display_card.actual_card].house_number == 0:
                        trade_menu.trader_card_1 = display_card.actual_card
                        trade_menu.trader_card_1_name = display_card.name
                    if trade_menu.trader_card_2 == 0 and fields[display_card.actual_card].house_number == 0 \
                        and fields[display_card.actual_card].position != trade_menu.trader_card_1:
                        trade_menu.trader_card_2 = display_card.actual_card
                        trade_menu.trader_card_2_name = display_card.name
                    if trade_menu.trader_card_3 == 0 and fields[display_card.actual_card].house_number == 0 \
                        and fields[display_card.actual_card].position != trade_menu.trader_card_2 and fields[display_card.actual_card].position != trade_menu.trader_card_1:
                        trade_menu.trader_card_3 = display_card.actual_card
                        trade_menu.trader_card_3_name = display_card.name  

# COLORS
def which_color(fields,players):
    for i in range (40):
        if fields[i].can_buy == 1:
            if fields[i].owner <4:
                fields[i].owner_color = players[fields[i].owner].color

# DICES
def roll_dice():
    return random.randint(1, 6)

def get_dice():
    return int(input())

# MOVE AND POSITIONS
def change_position_on_map(player,destination,fields,text_class):
    if fields[destination].visitors == 0:
        player.x_cord=fields[destination].position_1[0]
        player.y_cord=fields[destination].position_1[1]
    elif fields[destination].visitors == 1:
        player.x_cord=fields[destination].position_2[0]
        player.y_cord=fields[destination].position_2[1]
    elif fields[destination].visitors == 2:
        player.x_cord=fields[destination].position_3[0]
        player.y_cord=fields[destination].position_3[1]
    elif fields[destination].visitors == 3:
        player.x_cord=fields[destination].position_4[0]
        player.y_cord=fields[destination].position_4[1]
    fields[destination].visitors+=1

def move_player(player, steps,fields,text_class):
    position_old = player.position
    player.position += steps
    player.position %= 40
    print("Player ",str(player.name+1)," move ",steps," steps to position: ",player.position)

    change_position_on_map(player,player.position,fields,text_class)
    fields[position_old].visitors-=1
    print("Field ",str(fields[position_old].name),' have now ',str(fields[position_old].visitors),' visitors')
    if fields[player.position].position != 30:
        print("Field ",str(fields[player.position].name),' have now ',str(fields[player.position].visitors),' visitors')
    if player.position != 30 and player.position - position_old < 0:
        player.balance += 200
    # PRISON
    if fields[player.position].position == 30:
        print('--PRISON--')
        go_to_prison(player,fields,text_class)
    

# PRISON
def go_to_prison(player,fields,text_class):
    text_info='Player ' + str(player.name) + ' is going to prison'
    print("Player ",str(player.name+1)," go to prison")
    change_position_on_map(player,10,fields,text_class)
    player.prison = 3 
    player.position = 10  


# PAYS RENT
def pay_rent(players,fields,current_player,text_class,option):
    rent=100
    if  fields[players[current_player].position].can_house==1:
        if fields[players[current_player].position].house_number == 0:
            rent = fields[players[current_player].position].rent_0
            rent_number = 'rent_0'
        if fields[players[current_player].position].house_number == 1:
            rent = fields[players[current_player].position].rent_1
            rent_number = 'rent_1'
        if fields[players[current_player].position].house_number == 2:
            rent = fields[players[current_player].position].rent_2
            rent_number = 'rent_2'
        if fields[players[current_player].position].house_number == 3:
            rent = fields[players[current_player].position].rent_3
            rent_number = 'rent_3'
        if fields[players[current_player].position].house_number == 4:
            rent = fields[players[current_player].position].rent_4
            rent_number = 'rent_4'
        if fields[players[current_player].position].house_number == 5:
            rent = fields[players[current_player].position].rent_5
            rent_number = 'rent_5'   
    if fields[players[current_player].position].name == 12:
        rent = 50
    if fields[players[current_player].position].name == 12:
        rent = 100  
    if fields[players[current_player].position].name in (5,15,25,35):
        rent=100
    if option == 0:
        players[current_player].balance -= rent
        players[fields[players[current_player].position].owner].balance += rent
        print('Player ',players[current_player].name,' pays ',rent,'$ to ',\
            players[fields[players[current_player].position].owner].name+1)
    if option == 1:
        return rent

 # PAY RENT MESSAGE      
def pay_rent_message(players,fields,current_player,text_class):
    if  fields[players[current_player].position].can_house==1:
        if fields[players[current_player].position].house_number == 0:
            rent = fields[players[current_player].position].rent_0
        if fields[players[current_player].position].house_number == 1:
            rent = fields[players[current_player].position].rent_1
        if fields[players[current_player].position].house_number == 2:
            rent = fields[players[current_player].position].rent_2
        if fields[players[current_player].position].house_number == 3:
            rent = fields[players[current_player].position].rent_3
        if fields[players[current_player].position].house_number == 4:
            rent = fields[players[current_player].position].rent_4
        if fields[players[current_player].position].house_number == 5:
            rent = fields[players[current_player].position].rent_5

        text_class.value0 = 'Player ' + str(current_player+1)+ ' have to pay ' + str(rent) + '$ to player ' + str(fields[players[current_player].position].owner+1) 
        text_class.value0_position = [200,200]

# TAXES
def pay_tax(players,fields,current_player,text_class):
    tax = fields[players[current_player].position].tax
    players[current_player].balance -= tax
    if players[current_player].balance < 0:
        tax -= -players[current_player].balance
        players[current_player].balance = 0
    print('Player ',players[current_player].name,' pays tax ',tax,'$')

# TREASURE
def treasure(players,fields,current_player,text_class):
    gift = 0
    random_number = random.randint(1, 10)
    if random_number < 4:
        gift = random_number*20*(-1)
    else:
        gift = random_number*20

    if gift > 0:
        players[current_player].balance += gift
    else:
        players[current_player].balance -= gift
        if players[current_player].balance < 0:
            gift -= -players[current_player].balance
            players[current_player].balance = 0
    print('Player ',players[current_player].name,' get gift ',gift,'$')


# BUY PROPERTY
def buy_a_property(player,fields,text_class,field_number):
    if player.balance-fields[field_number].price >-1:
        fields[field_number].owner=player.name
        print("Player ",str(player.name+1)," bought property: ",fields[field_number].name )
        player.balance-=fields[field_number].price
# BUY PROPERTY MESSAGE
def buy_a_property_message(players,current_player,fields,text_class,field_number,options):
    text_class.value0_position = [200,200]
    if options == 1:
        text_class.value0 = 'Player ' + str(current_player+1) + ' bought property: ' +  str(fields[players[current_player].position].name) 
    elif options == 2:
        text_class.value0 = 'You cant buy this property, it has owner '#+str(fields[players[current_player].position].owner+1) 
    elif options == 3:
        text_class.value0 = 'You cant buy this property' 
    else:
        text_class.value0 = 'Not enough money' 

# HOUSE BUY OR SELL
def buy_house(fields,players,current_player,text_class,display_card):
    if fields[display_card.actual_card].house_number == -1:
        fields[display_card.actual_card].house_number +=1
        players[current_player].balance -= fields[display_card.actual_card].upgrade_price

    if fields[display_card.actual_card].house_number in (1,5) :
        if fields[display_card.actual_card].size == 3:
            if fields[display_card.actual_card].owner == fields[fields[display_card.actual_card].other_1].owner \
                == fields[fields[display_card.actual_card].other_2].owner:
                fields[display_card.actual_card].house_number +=1
                players[current_player].balance -= fields[display_card.actual_card].upgrade_price
                print('Player',current_player+1,' bought a house on field ',fields[display_card.actual_card].name,\
                    ' ',fields[display_card.actual_card].house_number,'H')
        if fields[display_card.actual_card].size == 2:
            if fields[display_card.actual_card].owner == fields[fields[display_card.actual_card].other_1].owner:
                fields[display_card.actual_card].house_number +=1
                players[current_player].balance -= fields[display_card.actual_card].upgrade_price
                print('Player',current_player+1,' bought a house on field ',fields[display_card.actual_card].name,\
                    ' ',fields[display_card.actual_card].house_number,'H')

def sell_house(fields,players,current_player,text_class,display_card):
    if fields[display_card.actual_card].house_number == 0:
        fields[display_card.actual_card].house_number -=1
        players[current_player].balance += fields[display_card.actual_card].rent_m

    if fields[display_card.actual_card].house_number > 0:
        if fields[display_card.actual_card].size == 3:
            if fields[display_card.actual_card].owner == fields[fields[display_card.actual_card].other_1].owner \
                == fields[fields[display_card.actual_card].other_2].owner:
                fields[display_card.actual_card].house_number -=1
                players[current_player].balance += fields[display_card.actual_card].downgrade_price
                print('Player',current_player+1,' sell a house on field ',fields[display_card.actual_card].name,\
                    ' ',fields[display_card.actual_card].house_number,'H')
        if fields[display_card.actual_card].size == 2:
            if fields[display_card.actual_card].owner == fields[fields[display_card.actual_card].other_1].owner:
                fields[display_card.actual_card].house_number -=1
                players[current_player].balance += fields[display_card.actual_card].downgrade_price
                print('Player',current_player+1,' sell a house on field ',fields[display_card.actual_card].name,\
                    ' ',fields[display_card.actual_card].house_number,'H')
    


# DISPLAY MESSAGE
def display_actual_card(fields,players,current_player,text_class,display_card,change):
    if change != 0:
        display_card.actual_card += change
        display_card.actual_card %= 40
    position = display_card.actual_card
    display_card.name   = fields[position].name
    display_card.price  = fields[position].price
    
    if fields[position].can_house == 1:
        display_card.special_cards = 0
        display_card.rent_0 = fields[position].rent_0
        display_card.rent_1 = fields[position].rent_1
        display_card.rent_2 = fields[position].rent_2
        display_card.rent_3 = fields[position].rent_3
        display_card.rent_4 = fields[position].rent_4
        display_card.rent_5 = fields[position].rent_5 
    if fields[position].can_house == 0:
        display_card.special_cards = 1