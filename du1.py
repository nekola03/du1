from turtle import exitonclick, forward, left, right, penup, pendown, speed, setpos, circle, hideturtle     #import funkcí z knihovny turtle

#FUNKCE VYKRESLENÍ KŘÍŽKU
def hashtag_function(hor, ver):       
    penup()     
    setpos((hor*10)-5,(ver*10)-5)   #přesun na střed buňky
    pendown()
    for _ in range(4):  #tvorba křížku pomocí for cyklu
        left(45)          
        forward(5)         
        left(180)           
        forward(5)          
        left(45)            

#FUNKCE VYKKRESLENÍ KOLEČKA
def circle_function(hor, ver):
    penup()     
    setpos((hor*10)-5,(ver*10)-5)   #přesun na střed dané buňky
    right(90)
    forward(4)
    left(90)
    pendown()
    circle(4)      #tvorba kruhu pomocí existující funkce

#FUNKCE URČENÍ KŘÍŽKU NA OSE X
def coordinates_hor(siteX):
    value = int(input("Zadej buňku na vodorovné ose -> ")) #zadání hodnoty na vodorovné ose (dle úkolu je možné, aby program spadl, když se zadá číslo nekonvertovatelné na int)
    while ((value > siteX) or (value <= 0)):      #vstupní hodnota value musí být v rozsahu 1 - siteX
        if(value > siteX):
            print("Hodnota musí být stejné nebo menší než ", siteX) 
        elif(value <= 0):
            print("Hodnota musí být větší než 0")       
        value = int(input("Zadej buňku na vodorovné ose -> "))  #případná oprava hodnoty
    return value

#FUNKCE URČENÍ KŘÍŽKU NA OSE Y
def coordinates_ver(siteY):
    value = int(input("Zadej buňku na svislé ose -> "))  #níže princip jako u osy X (tentokrát na svislé ose)
    while ((value > siteY) or (value <= 0)):      #vstupní hodnota value musí být v rozsahu 1 - siteY
        if(value > siteY):
            print("Hodnota musí být stejné nebo menší než ", siteY) 
        elif(value <= 0):
            print("Hodnota musí být větší než 0")       
        value = int(input("Zadej buňku na vodorovné ose -> "))  #případná oprava hodnoty
    return value
    
#VYKRESLENÍ HRACÍHO POLE NA ZÁKLADĚ ZADANÉ VELIKOSTI
siteX = int(input("Zadej rozměr X hracího pole -> "))
if siteX <= 1:                                           #piškvorky nejdou hrád na jednom řádku
    print("Musíš zadat kladné číslo a větší než 1!!!")                
    exit()                  
siteY = int(input("Zadej rozměr Y hracího pole -> "))
if siteY <= 1:                                           #piškvorky nejdou hrát na jednom sloupci
    print("Musíš zadat kladné číslo a větší než 1!!!")               
    exit() 
                                                                                          
speed(0)   
for m in range(siteY):       #vykresleno hrací pomocí tří vložených FOR cyklů                            
    for k in range(siteX):
        for _ in range(4):  
            forward(10)
            left(90)
        penup()
        forward(10)
        pendown()
    right(180)
    forward((10*siteX))
    right(90)
    forward(10)
    right(90)
print("Úspěšně jsi nakreslil hrací plochu a jdeme hrát!! Začíná hráč s X a poté hraje hráč s O")

#MEZIVÝPOČTY POTŘEBNÉ PRO SPRÁVNOU HRU
numberSquare = siteX * siteY        #počet všceh tahů (hracích buněk)
odEvenLap = numberSquare // 2
#print(odEvenLap)       
residue = numberSquare % 2
#print(residue)          #pokud bude výsledkem celé číslo, residue bude nula a pokud 1, bude počet tahů lichých a provede se poslední část kódu (podmínka if)
hideturtle()                        

#SUDÝ POČET TAHŮ
for _ in range(odEvenLap):     
    #ZNAČKA X
    print("\n HRAJE HRÁČ 1")
    valueX = coordinates_hor(siteX)
    valueY = coordinates_ver(siteY)
    hashtag_function(valueX,valueY)        

    #ZNAČKA O
    print("\n HRAJE HRÁČ 2")       #princip stejný jako u hráče 1 (rozdíl je ve vykreslení kolečka)
    valueX = coordinates_hor(siteX)
    valueY = coordinates_ver(siteY)
    circle_function(valueX,valueY)
    
#PŘI LICHÉM POČTU TAHU SE PROVEDE PŘEDCHOZÍ FOR CYKLUS + NÁSLEDUJÍCÍ ČÁST KÓDU
if(residue == 1):  
    #ZNAČKA X
    print("\n HRAJE HRÁČ 1")
    valueX = coordinates_hor(siteX)
    valueY = coordinates_ver(siteY)
    hashtag_function(valueX,valueY)  

print("\n\nÚSPĚŠNĚ JSI DOHRÁL HRU")
exitonclick()