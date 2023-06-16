import pygame, sys, os
import values, functions, functions_admin

pygame.init()
pygame.font.init()
os.system('cls')
print("Monopoly game\n")
print("/ Pygame veriosn:  ",pygame.__version__," /\n")

number_of_players=4
image_tlo = pygame.image.load("textury/background.png")
image_pionki= [
    pygame.image.load("textury/pawn1.png"),
    pygame.image.load("textury/pawn2.png"),
    pygame.image.load("textury/pawn3.png"),
    pygame.image.load("textury/pawn4.png")]

font = pygame.font.Font(None, 50)
font_card = pygame.font.Font(None, 40)
font1 = pygame.font.Font(None, 30)
white = (255, 255, 255)
black = (0, 0, 0)
background = (105,105,105)
resolution=(1420,1000)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption('Monopoly Pygame')

#-----------------------------------------------------------------------------------------------------------------------------------       CLASS
class Player:
    def __init__(self, name):
        self.name= name
        self.balance = 3000
        self.position = 0
        self.name_number = 0
        self.x_cord = 0
        self.y_cord = 0
        self.width = 20
        self.hight = 20
        self.image = 0
        self.position = 0
        self.active = 1
        self.color = (0, 0, 0, 255)
        self.prison = 0
        self.active = 1
    def draw(self):
        window.blit(self.image,(self.x_cord, self.y_cord))

class Field:
    def __init__(self, position):
        self.position = position
        self.name = 'name'
        self.price = 0
        self.rent_m = 0
        self.rent_0 = 0
        self.rent_1 = 0
        self.rent_2 = 0
        self.rent_3 = 0
        self.rent_4 = 0
        self.rent_5 = 0
        self.color = 'white'    
        self.owner = 44
        self.postion_owner_color = [0,0]
        self.postion_owner_color_size = [0,0]
        self.owner_color = (0, 0, 0, 255)
        self.position_1 = [0,0]
        self.position_2 = [0,0]
        self.position_3 = [0,0]
        self.position_4 = [0,0]
        self.position_house_1 = [10,10]
        self.position_house_2 = [20,20]
        self.position_house_3 = [30,30]
        self.position_house_4 = [40,40]
        self.position_hotel = [0,0]
        self.visit_house_1 = 0
        self.visit_house_2 = 0
        self.visit_house_3 = 0
        self.visit_house_4 = 0
        self.visit_hotel = 0
        self.visitors = 0
        self.can_buy = 0
        self.can_house = 0
        self.owner_baner_position = [0,0]
        self.tax = 0
        self.treasure = 0
        self.house_number = 0
        self.upgrade_price = 100
        self.downgrade_price = 50
        self.other_1 = 0
        self.other_2 = 0
        self.size = 0
        self.house_rect_size = [16,16]
        self.house_color = (0, 153, 0, 255)
        self.hotel_color = (178, 34, 34, 255)
        self.mortgage = black

    def draw_owner(self):
        if self.can_buy == 1 and self.owner !=44:
                    pygame.draw.rect(window, self.owner_color, (self.postion_owner_color , self.postion_owner_color_size ))

    def draw_houses(self):
        if self.can_buy == 1 and self.owner !=44 and self.can_house == 1:
            if self.house_number == 5:
                pygame.draw.rect(window, self.hotel_color, (self.position_hotel,self.house_rect_size ))
            if self.house_number < 5 and self.house_number > 0:
                for i in range (1,(self.house_number+1)):
                    if i == 1:
                        pygame.draw.rect(window, self.house_color, (self.position_house_1,self.house_rect_size ))
                    if  i == 2:
                        pygame.draw.rect(window, self.house_color, (self.position_house_2,self.house_rect_size ))
                    if  i == 3:
                        pygame.draw.rect(window, self.house_color, (self.position_house_3,self.house_rect_size ))
                    if  i == 4:
                        pygame.draw.rect(window, self.house_color, (self.position_house_4,self.house_rect_size ))

        if self.house_number == -1:
                pygame.draw.rect(window, black, (self.position_hotel,self.house_rect_size ))
            

class Text:
    def __init__(self):
        self.value0 = '0'
        self.value1 = '1'
        self.value2 = '1'
        self.value3 = '1'
        self.value4 = '1'
        self.value0_position = [0,0] 
        self.value1_position = [0,0]
        self.value2_position = [0,0]
        self.value3_position = [0,0]
        self.value4_position = [0,0]

    def draw(self):
        self.text = font_card.render((str(self.value0)),True,black)
        self.position = self.value0_position
        window.blit(self.text,(self.position))

class Text_Card:
    def __init__ (self):
        self.name = 'name'
        self.actual_card = 0
        self.info = 'info'
        self.price = 0
        self.rent_m = 0 
        self.rent_0 = 0
        self.rent_1 = 0
        self.rent_2 = 0
        self.rent_3 = 0
        self.rent_4 = 0
        self.rent_5 = 0
        self.special_cards = 0
        self.y = 400
    def draw(self):
        x=400;  y=self.y;   z=30
        self.text = font_card.render(('Name: '+str(self.name)),True,black)
        window.blit(self.text,(x,y+(-1)*z))
        self.text = font_card.render(('price: '+str(self.price)),True,black)
        window.blit(self.text,(x,y+0*z))
        if self.special_cards == 0:
            self.text = font_card.render(('no houses: '+str(self.rent_0)),True,black)
            window.blit(self.text,(x,y+1*z))
            self.text = font_card.render(('1 house: '+str(self.rent_1)),True,black)
            window.blit(self.text,(x,y+2*z))
            self.text = font_card.render(('2 house: '+str(self.rent_2)),True,black)
            window.blit(self.text,(x,y+3*z))
            self.text = font_card.render(('3 house: '+str(self.rent_3)),True,black)
            window.blit(self.text,(x,y+4*z))
            self.text = font_card.render(('4 house: '+str(self.rent_4)),True,black)
            window.blit(self.text,(x,y+5*z))
            self.text = font_card.render(('hotel: '+str(self.rent_5)),True,black)
            window.blit(self.text,(x,y+6*z))

class Trade_Menu:
    def __init__(self):
        self.host_card_1 = 0
        self.host_card_2 = 0
        self.host_card_3 = 0
        self.host_card_1_name = ''
        self.host_card_2_name = ''
        self.host_card_3_name = ''
        self.trader_card_1 = 0
        self.trader_card_2 = 0
        self.trader_card_3 = 0
        self.trader_card_1_name = ''
        self.trader_card_2_name = ''
        self.trader_card_3_name = ''
        self.host_money = 0
        self.trader_money = 0
        self.host_name = 0
        self.trader_name = '_'
        self.find_trader = 0
        self.money = 0
        self.show_money = 0
    def draw(self):
        self.text = font_card.render(('TRADE MENU'),True,black)
        window.blit(self.text,(400,150))
        self.text = font_card.render('Player '+str(self.host_name+1),True,black)
        window.blit(self.text,(290,200))
        if self.trader_name == '_':
            self.text = font_card.render('Player '+str(self.trader_name),True,black)
        else:
            self.text = font_card.render('Player '+str(self.trader_name+1),True,black)
        window.blit(self.text,(560,200))

        self.text = font_card.render(str(self.host_money)+' $',True,black)
        window.blit(self.text,(310,240))
        self.text = font_card.render(str(self.trader_money)+' $',True,black)
        window.blit(self.text,(590,240))
        if self.show_money > 0:
            self.text = font_card.render(str(self.money),True,black)
            window.blit(self.text,(470,400))

        self.text = font_card.render(str(self.host_card_1_name),True,black)
        window.blit(self.text,(280,280))
        self.text = font_card.render(str(self.host_card_2_name),True,black)
        window.blit(self.text,(280,320))
        self.text = font_card.render(str(self.host_card_3_name),True,black)
        window.blit(self.text,(280,360))

        self.text = font_card.render(str(self.trader_card_1_name),True,black)
        window.blit(self.text,(570,280))
        self.text = font_card.render(str(self.trader_card_2_name),True,black)
        window.blit(self.text,(570,320))
        self.text = font_card.render(str(self.trader_card_3_name),True,black)
        window.blit(self.text,(570,360))


#----------------------------------------------------------------------------------------------------------------------------          MAIN 
def main(): 
    # CREATE PLAYERS, FIELDS, AND LISTS
    players=[]
    fields= []
    text_class = Text()
    display_card = Text_Card()
    trade_menu = Trade_Menu()
    for i in range(number_of_players):                     
        players.append(Player(i))
        players[i].image=image_pionki[i]
    for i in range(40):                         
        fields.append(Field(i))

    # IMPORT VALUES
    values.values_of_cards(fields)
    values.values_of_players(players)

    # MOVE ALL PLAYERS TO POSITION 0
    for i in range (number_of_players):
        functions.change_position_on_map(players[i],0,fields,text_class)
    fields[0].visitors = number_of_players

    # VARIAVBLES
    game_time = 0
    get_roll_number = 0
    after_buy = 0
    current_player = 0
    dice = 0
    fields_menu = 0 
    roll_dice_ = 0
    after_roll = 0
    next_turn = 0
    ready_to_end = 0
    after_payment = 0
    after_tax = 0
    after_treasure = 0
    press_to_continue = 0
    wait_for_continue = 0
    message = 0
    before_payment = 1
    trade_menu_start = 0
    trade_menu_open = 0
    active_players = 4
    find_trader = 0
    get_money = 0
    number_a = ''
    number_b = '0'
    number_c = 0
    give_number = 0
    can_rent = 1
    rent_amount = 0
    possible_bankrupt = 0
    rent_holder = 44
    want_to_bankrupt = 0
    last_player = 0

    # KEY PRESSED LETTERS
    key_f_pressed = False
    key_y_pressed = False
    key_u_pressed = False
    key_g_pressed = False
    key_h_pressed = False
    key_r_pressed = False
    key_q_pressed = False
    key_c_pressed = False
    key_t_pressed = False
    key_m_pressed = False
    key_n_pressed = False
    key_b_pressed = False
    key_o_pressed = False
    key_a_pressed = False
    key_l_pressed = False

    # KEY PRESSED NUMBERS
    key_numbers_pressed = False
    key_1_pressed = False
    key_1_pressed = False
    key_2_pressed = False
    key_3_pressed = False
    key_4_pressed = False
    key_5_pressed = False
    key_6_pressed = False
    key_7_pressed = False
    key_8_pressed = False
    key_9_pressed = False  

    # COMANDS 
    #functions.trade_menu_clear(trade_menu)
    #functions_admin.buy_all(fields,players,text_class) # BUY ALL
    #functions_admin.out(fields,players,text_class) 
 
    # START MESSAGE
    print("\nPlayer: ",current_player+1," Position: ",players[current_player].position)
    clock = pygame.time.Clock()
    display_interval = 1000
    last_display_time = pygame.time.get_ticks()

    
#----------------------------------------------------------------------------------------------------------------------------- WHILE RUN
    run = True
    while run:                                                      
        keys=pygame.key.get_pressed()
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)     

        
        # TIME
        current_time = pygame.time.get_ticks()
        if current_time - last_display_time >= display_interval:
            game_time +=1
            last_display_time = current_time


        # BANKRUPT
        if keys [pygame.K_l] and not key_l_pressed and trade_menu_open == 0 and fields_menu == 0: 
            key_l_pressed = True
            want_to_bankrupt = 1 
            message=1
            text_class.value0 = 'Bankrupt? y/n'  
            text_class.value0_position = [250,800]
        if not keys [pygame.K_l]:
            key_l_pressed = False

        if keys [pygame.K_n] and want_to_bankrupt == 1:
            want_to_bankrupt = 0
            message = 0 

        if keys [pygame.K_y] and want_to_bankrupt == 1:
            for i in range(40):
                if fields[i].owner == current_player:
                    fields[i].owner = rent_holder
                if rent_holder != 44:
                    players[rent_holder].balance += players[current_player].balance
                players[current_player].active=0
                players[current_player].balance=0
                want_to_bankrupt = 0
                text_class.value0 = 'null'
                message = 0 
                next_turn = 1

 



        

        # TRADE MENU
        if keys [pygame.K_t] and not key_t_pressed and trade_menu_open == 0 and fields_menu == 0 and want_to_bankrupt == 0: 
            key_t_pressed = True
            trade_menu_open = 1
            trade_menu_start = 1
            find_trader = 1
            trader = 7
            display_card.y = 500
            get_money = 0
            trade_menu.host_name = current_player
            print(' TRADE ')      
        if keys [pygame.K_t] and not key_t_pressed and trade_menu_open == 1: 
            key_t_pressed = True
            trade_menu_open = 0 
            trade_menu_start = 0
            find_trader = 0
            trader = 7
            fields_menu = 0
            display_card.y = 400
            get_money = 0 
            message = 0
            functions.trade_menu_clear(trade_menu)
        if not keys[pygame.K_t]:
            key_t_pressed = False 

        # TRADE MENU CHOSE TRADER
        if trade_menu_start == 1 and find_trader == 1:
            message=1
            text_class.value0 = 'Choose player number '
            text_class.value0_position = [350,500]
            if not key_1_pressed and not key_2_pressed and not key_3_pressed and not key_4_pressed:
                if keys [pygame.K_1]:
                    key_1_pressed = True
                    trader=0
                if keys [pygame.K_2]:
                    key_1_pressed = True
                    trader=1
                if keys [pygame.K_3]:
                    key_1_pressed = True
                    trader=2
                if keys [pygame.K_4]:
                    key_4_pressed = True
                    trader=3
            key_1_pressed = False
            key_2_pressed = False
            key_3_pressed = False
            key_4_pressed = False
            trader=int(trader)
            if  trader != current_player:
                if trader==0 or trader==1 or trader==2 or trader==3:
                    if players[trader].active==1:
                        trade_menu.trader_name = trader
                        find_trader = 0
                        #message = 0
                        text_class.value0 = 'Press a to accept trade'
                        text_class.value0_position = [350,840]

        # TRADE MENU CHOOSE CARDS
        if trade_menu_start == 1 and fields_menu == 1  and get_money == 0:
            if keys [pygame.K_b] and not key_n_pressed and not key_b_pressed:
                key_b_pressed = True
                functions.trade_host_fields(fields,players,current_player,display_card,trade_menu)
            if keys [pygame.K_n] and not key_n_pressed and not key_b_pressed:
                key_n_pressed = True
                functions.trade_trader_fields(fields,players,current_player,display_card,trade_menu,trader)   
            if not keys[pygame.K_n]:
                key_n_pressed = False
            if not keys[pygame.K_b]:
                key_b_pressed = False

        # TRADE MENU MONEY    
        if keys [pygame.K_m] and not key_m_pressed and get_money==0 and find_trader == 0 and fields_menu == 0:
            key_m_pressed = True
            get_money = 1
            give_number = 1
            print('money start')
            number_b = '0'
            number_c = 0
            trade_menu.show_money = 1
        if keys [pygame.K_m] and not key_m_pressed and get_money==1:
            key_m_pressed = True
            get_money = 0
            print('money stop')
            trade_menu.money=0
            trade_menu.show_money = 0
        if not keys[pygame.K_m]:
            key_m_pressed = False

        if get_money == 1 and give_number == 1 :
            if keys [pygame.K_0] and not key_0_pressed:
                key_0_pressed = True
                number_a = '0'
            if keys [pygame.K_1] and not key_1_pressed:
                key_1_pressed = True
                number_a = '1'
            if keys [pygame.K_2] and not key_2_pressed:
                key_2_pressed = True
                number_a = '2'
            if keys [pygame.K_3] and not key_3_pressed:
                key_3_pressed = True
                number_a = '3'
            if keys [pygame.K_4] and not key_4_pressed:
                key_4_pressed = True
                number_a = '4'
            if keys [pygame.K_5] and not key_5_pressed:
                key_5_pressed = True
                number_a = '5'
            if keys [pygame.K_6] and not key_6_pressed:
                key_6_pressed = True
                number_a = '6'
            if keys [pygame.K_7] and not key_7_pressed:
                key_7_pressed = True
                number_a = '7'
            if keys [pygame.K_8] and not key_8_pressed:
                key_8_pressed = True
                number_a = '8'
            if keys [pygame.K_9] and not key_9_pressed:
                key_9_pressed = True
                number_a = '9'

            if number_a != '':
                number_b = number_b + number_a
            number_a = ''
            number_c=int(number_b)
            trade_menu.money=number_c

            if keys [pygame.K_b] and not key_n_pressed and not key_b_pressed:
                key_b_pressed = True
                if players[current_player].balance-trade_menu.money > -1:
                    functions.trade_host_money(fields,players,current_player,display_card,trade_menu,get_money)
                    get_money = 0
            if keys [pygame.K_n] and not key_n_pressed and not key_b_pressed:
                key_n_pressed = True
                if players[trader].balance-trade_menu.money > -1:
                    functions.trade_trader_money(fields,players,current_player,display_card,trade_menu,get_money)
                    get_money = 0

            if not keys[pygame.K_n]:
                key_n_pressed = False
            if not keys[pygame.K_b]:
                key_b_pressed = False
            if not keys[pygame.K_0]:
                key_0_pressed = False
            if not keys[pygame.K_1]:
                key_1_pressed = False
            if not keys[pygame.K_2]:
                key_2_pressed = False
            if not keys[pygame.K_3]:
                key_3_pressed = False
            if not keys[pygame.K_4]:
                key_4_pressed = False
            if not keys[pygame.K_5]:
                key_5_pressed = False
            if not keys[pygame.K_6]:
                key_6_pressed = False
            if not keys[pygame.K_7]:
                key_7_pressed = False
            if not keys[pygame.K_8]:
                key_9_pressed = False
            if not keys[pygame.K_9]:
                key_9_pressed = False


        # TRADE MENU ACCEPT
        if keys [pygame.K_a] and not key_a_pressed:
            key_a_pressed = True
            trade_menu_open = 0 
            trade_menu_start = 0
            find_trader = 0
            trader = 7
            fields_menu = 0
            display_card.y = 400
            get_money = 0 
            message = 0
            print('accept')
            functions.accept_trade(fields,players,current_player,display_card,trade_menu,trader)
            functions.trade_menu_clear(trade_menu)
        if not keys[pygame.K_a]:
            key_a_pressed = False






        # FIELDS MENU OPEN
        if keys [pygame.K_f] and fields_menu == 0 and not key_f_pressed and find_trader == 0 and get_money == 0 and want_to_bankrupt == 0: 
            fields_menu = 1
            print(' fiedls_menu open')
            #actul_card = players[current_player].position
            if fields[players[current_player].position].can_buy == 1:
                display_card.actual_card = players[current_player].position
            else:
                display_card.actual_card = players[current_player].position +1
            functions.display_actual_card(fields,players,current_player,text_class,display_card,0)
            last_display_time = current_time
            key_f_pressed = True
        if not keys[pygame.K_f]:
                key_f_pressed = False
        # CLOSE FIELD MENU
        if keys [pygame.K_f] and fields_menu == 1 and not key_f_pressed: 
             print(' fields menu close')
             fields_menu = 0
             key_f_pressed = True
                

        # FIELDS MENU WHILE OPEN
        if fields_menu == 1:
            # MOVE FORWARD 
            if keys [pygame.K_y] and not key_y_pressed:  
                if fields[(display_card.actual_card+1)%40].can_buy == 1:
                    functions.display_actual_card(fields,players,current_player,text_class,display_card,1)
                else:
                    functions.display_actual_card(fields,players,current_player,text_class,display_card,2)
                key_y_pressed = True
            if not keys[pygame.K_y]:
                key_y_pressed = False

            # MOVE BACKWARD
            if keys [pygame.K_u] and not key_u_pressed:  
                if fields[(display_card.actual_card-1)%40].can_buy == 1:
                    functions.display_actual_card(fields,players,current_player,text_class,display_card,-1)
                else:
                    functions.display_actual_card(fields,players,current_player,text_class,display_card,-2)
                key_u_pressed = True
            if not keys[pygame.K_u]:
                key_u_pressed = False

            # HOUSE BUY 
            if keys [pygame.K_h] and not key_h_pressed and fields[display_card.actual_card].owner == current_player and trade_menu_open == 0 : 
                if  fields[display_card.actual_card].house_number < 5 and after_roll == 1:
                    functions.buy_house(fields,players,current_player,text_class,display_card)
                key_h_pressed = True
            if not keys[pygame.K_h]:
                key_h_pressed = False

            # HOUSE SELL 
            if keys [pygame.K_g] and not key_g_pressed and fields[display_card.actual_card].owner == current_player and trade_menu_open == 0:  
                if  fields[display_card.actual_card].house_number > -1 and after_roll == 1:
                    functions.sell_house(fields,players,current_player,text_class,display_card)
                key_g_pressed = True
            if not keys[pygame.K_g]:
                key_g_pressed = False


        # ROLL THE DICES   
        if players[current_player].prison == 0 :             
            # RANDOM
            if keys [pygame.K_r] and roll_dice_== 0 and not key_r_pressed: 
                roll_dice_ = 1
                dice =  functions.roll_dice() +  functions.roll_dice()
                print("Roll: ", dice)
                functions.move_player(players[current_player],dice,fields,text_class)
                after_roll = 1
                ready_to_end = 1
                key_r_pressed = True
            if not keys[pygame.K_r]:
                key_r_pressed = False
            # MANUALL
            if keys [pygame.K_o] and roll_dice_ == 0 and get_roll_number == 1:
                roll_dice_ = 1
                dice = functions.get_dice()
                dice = 30
                get_roll_number = 0
                print("Roll: ", dice)
                functions.move_player(players[current_player],dice,fields,text_class)
                after_roll = 1
                ready_to_end = 1
        
        # PRISON TURN
        if players[current_player].prison > 0 and roll_dice_ ==0:
            players[current_player].prison -= 1
            print('Player ',current_player+1,' have ',players[current_player].prison,' turns in prison')
            roll_dice_ = 1
            dice = 0
            after_roll = 1
            ready_to_end = 1


        # CONTINUE
        if keys [pygame.K_c] and wait_for_continue == 1 and not key_c_pressed: 
            key_c_pressed = True
            press_to_continue = 1
            wait_for_continue = 0
            message = 0
            if after_roll == 1:
                ready_to_end = 1
        if not keys[pygame.K_c]:
                key_c_pressed = False

        # AFTER ROLL ACTIONS
        if after_roll == 1 and fields_menu == 0:
            # END TURN
            if keys [pygame.K_q] and ready_to_end == 1 and not key_q_pressed:
                next_turn=1
                buy=0
                key_q_pressed = True
            if not keys[pygame.K_q]:
                key_q_pressed = False


            # POSSIBLE BANKPRUT
            if possible_bankrupt == 1:
                if want_to_bankrupt == 0:
                    text_class.value0 = 'You need money, or go bankrupt  ' + str(rent_amount) + '$' 
                text_class.value0_position = [250,800]
                rent_holder = fields[players[current_player].position].owner
                if players[current_player].balance >= rent_amount:
                    can_rent = 1
                    possible_bankrupt = 0
                    before_payment = 1

                

            # BUY
            if keys [pygame.K_b] and after_buy==0:
                if after_buy == 0:
                    after_buy=1
                    message=1
                    wait_for_continue = 1
                    if fields[players[current_player].position].can_buy == 1 and fields[players[current_player].position].owner==44:
                        if players[current_player].balance-fields[players[current_player].position].price >0:
                            functions.buy_a_property(players[current_player],fields,text_class,players[current_player].position)
                            #functions.buy_a_property_message(players,current_player,fields,text_class,players[current_player].position,1)
                        #else:
                            #functions.buy_a_property_message(players,current_player,fields,text_class,players[current_player].position,4)
                    #elif  fields[players[current_player].position].can_buy == 1 and fields[players[current_player].position].owner!=44:
                        #functions.buy_a_property_message(players,current_player,fields,text_class,players[current_player].position,2)                       
                    #else:
                        #functions.buy_a_property_message(players,current_player,fields,text_class,players[current_player].position,3)

            # PAYMENT RENT
            if fields[players[current_player].position].rent_0 > 0 \
                and after_payment==0 and can_rent==1 \
                and fields[players[current_player].position].can_buy > 0 \
                and fields[players[current_player].position].owner != players[current_player].name \
                and fields[players[current_player].position].owner != 44:
                if before_payment == 1:
                    functions.pay_rent_message(players,fields,current_player,text_class)
                    ready_to_end = 0
                    wait_for_continue = 1
                    message = 1
                    before_payment = 0
                    rent_amount = functions.pay_rent(players,fields,current_player,text_class,1)
                    if players[current_player].balance - rent_amount >-1:
                        can_rent = 1
                    else:
                        can_rent = 0
                        possible_bankrupt = 1
                        wait_for_continue = 0
                        before_payment = 1
                if press_to_continue == 1 and can_rent==1:
                    functions.pay_rent(players,fields,current_player,text_class,0)
                    after_payment = 1
                    press_to_continue = 0
                    message = 0
                    before_payment = 1    


            # PAYMENT TAX
            if fields[players[current_player].position].tax > 0 and after_tax==0:
                functions.pay_tax(players,fields,current_player,text_class)
                after_tax = 1


            # TREASURE
            if fields[players[current_player].position].treasure > 0 and after_treasure==0:
                functions.treasure(players,fields,current_player,text_class)
                after_treasure = 1


        # GO TO NEXT TURN, NEXT PLAYER
        if next_turn == 1:
            print("Player",current_player+1, ' ended his tour\n')
            ok = 0
            out = 0 
            while ok < 1:
                current_player += 1
                if current_player == number_of_players:
                    current_player = 0
                if players[current_player].active == 1:
                    ok = 1
                    last_player = current_player
                out +=1
                if out == 10:
                    ok =1
            next_turn = 0
            dice = 0
            after_roll = 0
            ready_to_end = 0
            roll_dice_ = 0
            after_payment = 0
            after_tax=0
            after_treasure = 0
            after_buy = 0
            press_to_continue = 0
            wait_for_continue = 0
            message=0
            rent_holder = 44
            functions.trade_menu_clear(trade_menu)
            print("\nPlayer: ",current_player+1, " Position: ",players[current_player].position)
            


        # LAYERS AND TEXT --------------------------------------------------------------------------------------------------------------------------------------------
        
        # BACKGROUND
        window.fill(background)                                                                         
        window.blit(image_tlo,(0,0)) 

        # INFO MESSAGE
        if message == 1:
            text_class.draw()

        # TRADE MENU
        if trade_menu_open == 1:
            trade_menu.draw()
        
        # PLAYERS
        for i in range(number_of_players): 
            if players[i].active == 1:
                players[i].draw()   

        # FIELD MENU ON/OFF
        if fields_menu == 1:
            display_card.draw()   

        # WHICH TOURN AND ROLL
        text_info = ''
        text_current_player = font.render('Player turn '+str(current_player+1), True, black)
        text_draw_result = font.render('Dices: ' + str(dice), True, black)
        text_info_baner = font.render(text_info,True,black)
        window.blit(text_current_player, (1050,50))
        window.blit(text_draw_result,(1050,100))
        window.blit(text_info_baner,(220,140))

        # HUD
        text_hud = font1.render('R - Roll the dice',True,black)
        window.blit(text_hud,(1050,520))
        text_hud = font1.render('Q - quit your turn',True,black)
        window.blit(text_hud,(1050,552))
        text_hud = font1.render('B - buy the property',True,black)
        window.blit(text_hud,(1050,584))
        text_hud = font1.render('C - continue',True,black)
        window.blit(text_hud,(1050,616))
        text_hud = font1.render('F- fields',True,black)
        window.blit(text_hud,(1050,648))
        text_hud = font1.render('Y/U - next/previous field',True,black)
        window.blit(text_hud,(1050,680))
        text_hud = font1.render('G/H - sell/buy house',True,black)
        window.blit(text_hud,(1050,712))
        text_hud = font1.render('T - trade menu',True,black)
        window.blit(text_hud,(1050,744))
        text_hud = font1.render('M - money in trade',True,black)
        window.blit(text_hud,(1050,776))
        text_hud = font1.render('B/N - assing to trader 1/2',True,black)
        window.blit(text_hud,(1050,808))
        text_hud = font1.render('L - go bankrup',True,black)
        window.blit(text_hud,(1050,840))
        
        
        
        
        
        

        # CLOCK
        clock_value = str(game_time)
        text_clock = font1.render(clock_value,True,black)
        window.blit(text_clock,(1350,980))

        # BALANCE AND NAMES
        text_players=[1,2,3,4]
        position_y=250
        for i in range(number_of_players):
            if players[i].active == 1:
                money=str(players[i].balance)+ ' $ '
            else:
                money = 'BANKRUPT'
            text='Player '+str(players[i].name+1)+ '    '+str(money)  \
            #+ '   P: '  + str(players[i].position) + spacja + ' ' \
            text_players[i]=font.render(text,True,black)
            window.blit(text_players[i],(1020,position_y))
            position_y=position_y+50

        # DISPLAY OWNER BANNERS AND HOUSES
        functions.which_color(fields,players)
        for i in range(40):
            fields[i].draw_owner()
            fields[i].draw_houses()
        pygame.display.update()
if __name__ == "__main__":
    main() 