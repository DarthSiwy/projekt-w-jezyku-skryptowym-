import functions

def buy_all(fields,players,text_class):
    for i in range(4):
         players[i].balance = 5000
    for i in range(0,4):
        for j in range(10):
            k=j+i*10
            if fields[k].can_buy == 1 and fields[k].owner==44:
                    functions.buy_a_property(players[i],fields,text_class,k) 

def out(fields,players,text_class):
    for i in range(4):
         players[i].balance = 30
    players[3].balance = 10000
    for i in range(0,4):
        for j in range(10):
            k=j+i*10
            if fields[k].can_buy == 1 and fields[k].owner==44:
                    functions.buy_a_property(players[3],fields,text_class,k) 