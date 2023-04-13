import pygame, sys, random, os

pygame.init()
os.system('cls')
print("Monopoly game\n\n-------------------")
print("Pygame veriosn\t",pygame.__version__,"\n\n")

image_tlo = pygame.image.load("tlo.png")
image_pionki= [
    pygame.image.load("pionek1.png"),
    pygame.image.load("pionek2.png"),
    pygame.image.load("pionek3.png"),
    pygame.image.load("pionek4.png")]

liczba_pionkow=4

font = pygame.font.Font(None, 50)
white = (255, 255, 255)
black = (0, 0, 0)
background = (105,105,105)

resolution=(1920,1080)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption('Monopoly w pygame')

#----------------------------------------             CLASS
class Pawn:
    def __init__(self, name, image):
        self.name = name
        self.x_cord = 1200
        self.y_cord = 0
        self.width = 20
        self.hight = 20
        self.image = image
        self.position = 0
    def tick(self):
        pass

    def draw(self):
        window.blit(self.image,(self.x_cord, self.y_cord))

class Player:
    def __init__(self, name):
        self.name=name
        self.money = 1500
        self.position = 1
    def draw(self):
        pass

class Field:
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.rent = 0
        self.color = 0
        self.position = 0
        self.x_position_1 = 0
        self.y_position_1 = 0
        self.x_position_2 = 0
        self.y_position_2 = 0
        self.x_position_3 = 0
        self.y_position_3 = 0
        self.x_position_4 = 0
        self.y_position_4 = 0
        self.x_position_house_1 = 0
        self.y_position_house_1 = 0
        self.x_position_house_2 = 0
        self.y_position_house_2 = 0
        self.x_position_house_3 = 0
        self.y_position_house_3 = 0
        self.x_position_house_4 = 0
        self.y_position_house_4 = 0
        self.x_position_hotel = 0
        self.y_position_hotel = 0
        self.visit_house_1 = 0
        self.visit_house_2 = 0
        self.visit_house_3 = 0
        self.visit_house_4 = 0
        self.visit_hotel = 0
    def draw(self):
        pass

class Card:
    def __init__(self, name):
        self.name = name
    def draw(self):
        pass

class Properties:
    def __init__(self):
        self.name = "property"
        self.price = 0
        self.rent = 0
        self.color = 0
        self.position = 0


#------------------------------------------                  DEF
def move_player(player, steps):
    player.position += steps
    print("Player ",str(player.name+1)," move ",steps," steps")
    print("Player: ",str(player.name+1), " Position: ",player.position)
    




#----------------------------------------------                 MAIN 
def main():  
    pionki=[]
    players=[]
    fields= []
    fields_price_values = []

    for i in range(liczba_pionkow):
        pionki.append(Pawn(i,image_pionki[i]))
        pionki[i].y_cord += i*25
        players.append(Player(i))

    


    for i in range(40):
        fields.append(Field(i))
        fields[i].position = i

        fields_price_values.append( (i+1)*50 )
        fields[i].price = fields_price_values [i]



    
    r=0
    q=1
    current_player = 0
    next = 0
    kostki = 0
    
    clock = pygame.time.Clock()

    print("Player: ",current_player+1, " Position: ",players[current_player].position)

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
        
        if keys [pygame.K_q] and q==0:
            q=1
            next=1
        
        if keys [pygame.K_r] and r==0 and q==1: 
            r=1

        if r==1:
            kostki = random.randint(1,12)
            print("Roll: ",kostki)
            move_player(players[current_player],kostki)
            r=q=0 
            
        
        if next==1:
            current_player += 1
            if current_player == liczba_pionkow:
                current_player = 0
            next = kostki = 0
            print("\nPlayer: ",current_player+1, " Position: ",players[current_player].position)
            


        
        
        string_balans_graczy = " "
        for i in range(liczba_pionkow):
            string_balans_graczy = string_balans_graczy + ""+str(i+1) + " " + str(players[i].money) + "\n"

        text_current_player = font.render('Tura gracza '+str(current_player+1), True, black)
        text_balance = font.render('Balans graczy '+string_balans_graczy, True, black)
        text_draw_result = font.render('Wylosowano: ' + str(kostki), True, black)

        window.fill(background)
        window.blit(image_tlo,(0,0))
        for i in range(liczba_pionkow): 
            pionki[i].draw()      

        window.blit(text_current_player, (1200,200))
        window.blit(text_draw_result,(1200,300))
        window.blit(text_balance,(1200,400))

        text = "Pierwszy napis\nDrugi napis"
        font_ = pygame.font.SysFont(None, 50)
        text_surface = font_.render(text, True, (255, 255, 255))
        #window.blit(text_surface, (1200,600))
     
        pygame.display.update()

if __name__ == "__main__":
    main() 