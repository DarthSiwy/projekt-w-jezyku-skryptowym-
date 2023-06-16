# WORKING WITH PLAYERS
def values_of_players(players):
    players[0].color = (160, 32, 240, 255)
    players[2].color = (0, 0, 255, 255) 
    players[3].color = (255, 0, 0, 255)
    players[1].color = (255, 255, 0, 255)

# WORIKING WITH FIELDS 
def values_of_cards(fields):
    data=[]
    pawn_distance=30
    
    # READ FROM FILE
    file=open('valuess.txt')
    for line in file:                                          
        elementy = line.split()    
        data.append(elementy)
    file.close()

    # INSERT VALUES
    for i in range(40):
        fields[i].price = (i+1)*10
        fields[i].name = data[i][1]
        fields[i].can_buy = int(data[i][2])
        fields[i].can_house = int(data[i][2])
        fields[i].color = str(data[i][3])
        if (1 <= i <= 9) or (21 <= i <= 29):
            fields[i].postion_owner_color_size = [74,10]
        if (11 <= i <= 19) or (31 <= i <= 39):
            fields[i].postion_owner_color_size = [10,80]
        fields[i].rent_m = round(fields[i].price/2)
        fields[i].rent_0 = (i+1)*5
        fields[i].rent_1 = fields[i].rent_0 * 2
        fields[i].rent_2 = fields[i].rent_0 * 3
        fields[i].rent_3 = fields[i].rent_0 * 4
        fields[i].rent_4 = fields[i].rent_0 * 5
        fields[i].rent_5 = fields[i].rent_0 * 6
        fields[i].other_1 = int(data[i][4])
        fields[i].other_2 = int(data[i][5])

        if fields[i].other_1 >0 and fields[i].other_2 >0:
            fields[i].size = 3

        if fields[i].other_1 >0 and fields[i].other_2==0:
            fields[i].size = 2

    # RENT PROPERTIES
    for i in (0,2,4,7,10,17,20,22,30,33,38):
        fields[i].rent_0 = 0
        fields[i].rent_1 = 0
        fields[i].rent_2 = 0
        fields[i].rent_3 = 0
        fields[i].rent_4 = 0
        fields[i].rent_5 = 0
    for i in (5,12,28,15,25,35):
        fields[i].can_house = 0
    for i in (2,7,17,22,33):
        fields[i].treasure = 1
    fields[4].tax = 200
    fields[38].tax = 300



    # OWNER COLOR BANER
    field_distance_baner_x = 79 
    field_distance_baner_y = 84
    fields[9].postion_owner_color = [150,990]
    for i in range (8,0,-1):
        fields[i].postion_owner_color[0] = fields[i+1].postion_owner_color[0] + field_distance_baner_x
        fields[i].postion_owner_color[1] = fields[i+1].postion_owner_color[1] 
    
    fields[19].postion_owner_color = [0,125]
    for i in range (18,10,-1):
        fields[i].postion_owner_color[0] = fields[i+1].postion_owner_color[0]
        fields[i].postion_owner_color[1] = fields[i+1].postion_owner_color[1] + field_distance_baner_y

    fields[21].postion_owner_color = [150,0]
    for i in range (22,30):
        fields[i].postion_owner_color[0] = fields[i-1].postion_owner_color[0] + field_distance_baner_x
        fields[i].postion_owner_color[1] = fields[i-1].postion_owner_color[1]

    fields[31].postion_owner_color = [990,125]
    for i in range (32,40):
        fields[i].postion_owner_color[0] = fields[i-1].postion_owner_color[0]
        fields[i].postion_owner_color[1] = fields[i-1].postion_owner_color[1] + field_distance_baner_y
    


    # PAWNS POSITIONS
    field_distance_pawn_x = 79
    field_distance_pawn_y = 84
    fields[0].position_1=[904,930]
    fields[20].position_1=[83,50]
    fields[30].position_1=[904,50]
    fields[10].position_1=[83,930]
                                                  
    fields[1].position_1=[790,930]  
    for i in range(0,10):
        fields[i].position_1[1] = fields[1].position_1[1]
        if i>1:
            fields[i].position_1[0] = fields[i-1].position_1[0] - field_distance_pawn_x

        fields[i].position_2[0]=fields[i].position_1[0] + pawn_distance
        fields[i].position_2[1]=fields[i].position_1[1]

        fields[i].position_3[0]=fields[i].position_1[0]
        fields[i].position_3[1]=fields[i].position_1[1] + pawn_distance
        
        fields[i].position_4[0]=fields[i].position_1[0] + pawn_distance
        fields[i].position_4[1]=fields[i].position_1[1] + pawn_distance
    
    fields[11].position_1=[83,810]
    for i in range(10,20):
        fields[i].position_1[0] = fields[11].position_1[0]
        if i>11:
            fields[i].position_1[1] = fields[i-1].position_1[1] - field_distance_pawn_y

        fields[i].position_2[0]=fields[i].position_1[0] 
        fields[i].position_2[1]=fields[i].position_1[1] + pawn_distance

        fields[i].position_3[0]=fields[i].position_1[0] - pawn_distance
        fields[i].position_3[1]=fields[i].position_1[1] 
        
        fields[i].position_4[0]=fields[i].position_1[0] - pawn_distance
        fields[i].position_4[1]=fields[i].position_1[1] - pawn_distance
    
    fields[21].position_1=[195,50]
    for i in range(20,30):
        fields[i].position_1[1] = fields[21].position_1[1]
        if i>21:
            fields[i].position_1[0] = fields[i-1].position_1[0] + field_distance_pawn_x

        fields[i].position_2[0]=fields[i].position_1[0] - pawn_distance
        fields[i].position_2[1]=fields[i].position_1[1] 

        fields[i].position_3[0]=fields[i].position_1[0] 
        fields[i].position_3[1]=fields[i].position_1[1] - pawn_distance
        
        fields[i].position_4[0]=fields[i].position_1[0] - pawn_distance
        fields[i].position_4[1]=fields[i].position_1[1] - pawn_distance
    
    fields[31].position_1=[904,171]
    for i in range(30,40):
        fields[i].position_1[0] = fields[31].position_1[0]
        if i>31:
            fields[i].position_1[1] = fields[i-1].position_1[1] + field_distance_pawn_y

        fields[i].position_2[0]=fields[i].position_1[0] 
        fields[i].position_2[1]=fields[i].position_1[1] - pawn_distance

        fields[i].position_3[0]=fields[i].position_1[0] + pawn_distance
        fields[i].position_3[1]=fields[i].position_1[1] 
        
        fields[i].position_4[0]=fields[i].position_1[0] + pawn_distance
        fields[i].position_4[1]=fields[i].position_1[1] - pawn_distance  


    # HOUSEs AND HOTEL POSITIONS
    house_space = 2
    x = fields[1].house_rect_size[1] + house_space 
    y = fields[1].house_rect_size[1] + house_space
    field_distance_house_x = 79
    field_distance_house_y = 84

    fields[9].position_house_1 = [152,888]
    fields[9].position_hotel = [178,888]
    for i in range(9,0,-1):
        if i < 9:
            fields[i].position_house_1[0] = fields[i+1].position_house_1[0] + field_distance_house_x
            fields[i].position_house_1[1] = fields[9].position_house_1[1]
            fields[i].position_hotel[0] = fields[i+1].position_hotel[0] + field_distance_house_x
            fields[i].position_hotel[1] = fields[9].position_hotel[1]     

        fields[i].position_house_2[0] = fields[i].position_house_1[0] + x
        fields[i].position_house_2[1] = fields[i].position_house_1[1]

        fields[i].position_house_3[0] = fields[i].position_house_1[0] + x*2
        fields[i].position_house_3[1] = fields[i].position_house_1[1]

        fields[i].position_house_4[0] = fields[i].position_house_1[0] + x*3
        fields[i].position_house_4[1] = fields[i].position_house_1[1]

    fields[21].position_house_1 = [152,96]
    fields[21].position_hotel = [178,96]
    for i in range(21,30):
        if i > 21:
            fields[i].position_house_1[0] = fields[i-1].position_house_1[0] + field_distance_house_x
            fields[i].position_house_1[1] = fields[21].position_house_1[1] 
            fields[i].position_hotel[0] = fields[i-1].position_hotel[0] + field_distance_house_x
            fields[i].position_hotel[1] = fields[21].position_hotel[1]    

        fields[i].position_house_2[0] = fields[i].position_house_1[0] + x
        fields[i].position_house_2[1] = fields[i].position_house_1[1]

        fields[i].position_house_3[0] = fields[i].position_house_1[0] + x*2
        fields[i].position_house_3[1] = fields[i].position_house_1[1]

        fields[i].position_house_4[0] = fields[i].position_house_1[0] + x*3
        fields[i].position_house_4[1] = fields[i].position_house_1[1]

    fields[19].position_house_1 = [125,129]
    fields[19].position_hotel = [125,155]
    for i in range(19,10,-1):
        if i < 19:
            fields[i].position_house_1[0] = fields[19].position_house_1[0] 
            fields[i].position_house_1[1] = fields[i+1].position_house_1[1] + field_distance_house_y   
            fields[i].position_hotel[0] = fields[19].position_hotel[0] 
            fields[i].position_hotel[1] = fields[i+1].position_hotel[1] + field_distance_house_y  

        fields[i].position_house_2[0] = fields[i].position_house_1[0] 
        fields[i].position_house_2[1] = fields[i].position_house_1[1] + y

        fields[i].position_house_3[0] = fields[i].position_house_1[0] 
        fields[i].position_house_3[1] = fields[i].position_house_1[1] + y*2

        fields[i].position_house_4[0] = fields[i].position_house_1[0] 
        fields[i].position_house_4[1] = fields[i].position_house_1[1] + y*3

    fields[31].position_house_1 = [868,129]
    fields[31].position_hotel = [868,155]
    for i in range(31,40):
        if i > 31:
            fields[i].position_house_1[0] = fields[31].position_house_1[0] 
            fields[i].position_house_1[1] = fields[i-1].position_house_1[1] + field_distance_house_y   
            fields[i].position_hotel[0] = fields[31].position_hotel[0] 
            fields[i].position_hotel[1] = fields[i-1].position_hotel[1] + field_distance_house_y 

        fields[i].position_house_2[0] = fields[i].position_house_1[0] 
        fields[i].position_house_2[1] = fields[i].position_house_1[1] + y

        fields[i].position_house_3[0] = fields[i].position_house_1[0] 
        fields[i].position_house_3[1] = fields[i].position_house_1[1] + y*2

        fields[i].position_house_4[0] = fields[i].position_house_1[0] 
        fields[i].position_house_4[1] = fields[i].position_house_1[1] + y*3

    # PRINT TERMINAL 
    for i in range(40):   
        #print(data[i])
        pass
    #print('\n----end of values----\n\n\n')