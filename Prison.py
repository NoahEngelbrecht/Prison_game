import time
import random  # Importerar random för att hjälpa till med upptäckten av dolda föremål.

# Globala variabler för att spåra spelets tillstånd
found_key = False  # Indikerar om spelaren har hittat den första nyckeln
visited_room = False  # Indikerar om spelaren har besökt huvudrummet
found_second_key = False  # Indikerar om spelaren har hittat den andra nyckeln
went_right = False  # Indikerar om spelaren har gått åt höger i korridoren
visited_room_1 = False  # Indikerar om rum 1 har besökts
visited_room_2 = False  # Indikerar om rum 2 har besökts
visited_room_3 = False  # Indikerar om rum 3 har besökts
fight = False  # Indikerar om spelaren har valt att slåss
talk = False  # Indikerar om spelaren har valt att prata
entered_corridor = False  # Indikerar om spelaren har gått in i korridoren
gitarr = False  # Indikerar om spelaren har hittat en gitarr
visited_cell5 = False  # Indikerar om cell 5 har besökts
visited_vakt_rum = False  # Indikerar om vakt rummet har besökts
visited_cell2 = False  # Indikerar om cell 2 har besökts
hidden_item_found = False  # Indikerar om spelaren har hittat den dolda föremålet

# Lista för att lagra prestationer
achievements = []

def add_achievement(achievement):
    # Lägger till en prestation om den inte redan finns.
    if achievement not in achievements:
        achievements.append(achievement)
        print(f"Grattis! Du har låst upp en prestation: {achievement}")

def start_meny():
    # Visar huvudmenyn med alternativ för spelaren.
    print("""Välkommen till mitt Prison Game spel
Du har tre olika val.
1. Spela spelet
2. Läsa instruktionerna
3. Avsluta spelet.""")
    
    # Hämtar användarens val av åtgärd
    start_val = input("Vad vill du göra? ").strip().lower()
    
    # Hanterar användarens val för att starta spelet, läsa instruktioner eller avsluta
    if start_val == "1":
        welcome_message()  # Anropar funktionen för välkomstmeddelande
        start_room()  # Startar spelet i start rummet
    elif start_val == "2":
        print("\n")
        filnamn = "Readme.txt"  # Filnamn för instruktioner
        try:
            # Försöker öppna och läsa instruktionernas fil
            with open(filnamn, "r", encoding="utf-8") as fil:
                content = fil.read()
                print(content)  # Skriver ut innehållet i filen
        except FileNotFoundError:
            print(f"Filen '{filnamn}' kunde inte hittas.")  # Meddelar om filen inte hittades
        except Exception as e:
            print(f"Ett fel inträffade: {e}")  # Hanterar andra fel
        input("Tryck på valfri tangent för att fortsätta...")  # Väntar på användarens input
        start_meny()  # Återvänder till huvudmenyn
    elif start_val == "3":
        exit()  # Avslutar spelet
    else: 
        print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
        start_meny()  # Återvänder till huvudmenyn

def rad():
    # Skriver ut en tom rad.
    print("")

def welcome_message():
    # Visar välkomstmeddelande till spelaren.
    rad()
    print("Välkommen till fängelset. Ditt mål är att ta dig ut genom att lösa olika problem och komma förbi vakterna.")
    time.sleep(0.7)
    print("Du är just nu i din cell.")
    time.sleep(1)

def exit_game():
    # Meddelar spelaren att de har lyckats ta sig ut ur fängelset.
    rad()
    print("Grattis, du lyckas ta dig ut ur fängelset!")
    time.sleep(0.3)
    play_again()  # Frågar om spelaren vill spela igen

def exit_lost_game():
    # Meddelar spelaren att de inte lyckades ta sig ut ur fängelset.
    rad()
    print("Du lyckades inte ta dig ut ur fängelset.")
    time.sleep(0.3)
    play_again()  # Frågar om spelaren vill spela igen

def play_again():
    # Frågar spelaren om de vill spela igen.
    rad()
    play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
    time.sleep(1)
    if play_again != "ja":
        print("Tack för att du spelade!")  # Tackar spelaren
        exit()  # Avslutar spelet
        time.sleep(1)
    if play_again == "ja":
        print("Varsågod att försöka igen")  # Meddelar spelaren att de kan försöka igen
        main()  # Återvänder till huvudfunktionen

def start_room():
    # Frågar spelaren vad de vill göra i start rummet.
    rad()
    action = input("Vad vill du göra? (kolla runt, öppna dörren): ").strip().lower()
    time.sleep(1)
    if action == "kolla runt":
        check_room()  # Kollar rummet
    elif action == "öppna dörren":
        try_open_door()  # Försöker öppna dörren
    else:
        print("Ogiltigt val, försök igen.")  # Meddelar om ogiltigt val
        start_room()  # Återvänder till start rummet

def check_room():
    # Kontrollerar rummet för att hitta nyckeln.
    global found_key, hidden_item_found  # Använder den globala variabeln för att spåra nyckeln och den dolda föremålet
    print("Du kollar runt i rummet.")
    time.sleep(1)
    print("Du hittar en liten vass nyckel som du kan använda för att låsa upp dina hand- och fotbojor.")
    time.sleep(1)
    print("Dörren är öppen så du kan gå ut.")
    found_key = True  # Spelaren har nu hittat nyckeln
    time.sleep(0.5)
    add_achievement("Första nyckeln funnen!")  # Lägger till prestation
    time.sleep(0.3)
    
    # Ny funktionalitet: slumpmässig chans att hitta en dold föremål
    if random.choice([True, False]):  # 50% chans att hitta en dold föremål
        hidden_item_found = True
        print("Du hittar ett dolt föremål! Det kan hjälpa dig att fly.")
        time.sleep(0.5)
        add_achievement("Dolt föremål funnet!")  # Lägger till prestation
    else:
        print("Tyvärr, du hittar inget mer av intresse.")
    
    go_left_or_right()  # Frågar spelaren vilken väg de vill gå

def try_open_door():
    # Försöker öppna dörren.
    print("Du försöker öppna dörren.")
    time.sleep(1)
    print("Dörren är öppen så du kan sakta gå ut ur rummet.")
    time.sleep(1)
    go_left_or_right()  # Frågar spelaren vilken väg de vill gå

def go_left_or_right():
    # Frågar spelaren om de vill gå vänster eller höger.
    rad()
    next_action = input("Vill du gå vänster eller höger? (vänster/höger): ").strip().lower()
    time.sleep(1)
        
    if next_action == "vänster":
        go_left()  # Går vänster
        print("Du återvänder till korridoren.")
        time.sleep(1)
        go_left_or_right()
    elif next_action == "höger":
        go_right()  # Går höger
        time.sleep(1)
    else:
        print("Ogiltigt val, försök igen.")  # Meddelar om ogiltigt val
        go_left_or_right()  # Återvänder för att fråga igen

def go_left():
    # Beskriver vad som händer när spelaren går vänster.
    print("Du går vänster i flera minuter och ser ingenting av intresse.")
    time.sleep(1)
    print("Du känner att du måste återvända till korridoren för att fortsätta ditt äventyr.")
    time.sleep(1)

def go_right():
    # Beskriver vad som händer när spelaren går höger.
    global went_right  # Använder den globala variabeln för att spåra om spelaren har gått höger
    if not went_right:
        print("Du går till höger och ser två dörrar, en som står öppen medan den andra är stängd.")
        time.sleep(0.5)
        went_right = True  # Spelaren har nu gått höger
        time.sleep(0.3)
    door_action = input("Vill du gå till den öppna eller stängda dörren? (öppna/stängda): ").strip().lower()
    time.sleep(1)
    if door_action == "öppna":
        enter_room()  # Går in i rum 1
    elif door_action == "stängda":
        enter_room2()  # Går in i rum 2
    else:
        print("Ogiltigt val")  # Meddelar om ogiltigt val
        go_right()  # Återvänder för att fråga igen

def room_one():
    # Beskriver vad som händer när spelaren går in i rum 1.
    global visited_room_1, fight, talk  # Använder globala variabler för att spåra rum och interaktioner
    rad()
    if not visited_room_1:
        print("När du går in i detta rum ser du en vakt som direkt känner igen dig från dina tidigare försök att fly från fängelset.")
        time.sleep(1)
        print("Vakten säger: 'Du ska inte vara här!' Vad vill du göra?")
        time.sleep(1)
        visited_room_1 = True  # Rummet har nu besökts
        rad()
        
    action = input("Vill du (slåss) eller (försöka övertala) vakten?: ").strip().lower()
    time.sleep(1)
        
    if action == "slåss":
        fight = True  # Spelaren har valt att slåss
        print("Du försöker slåss mot vakten!")
        time.sleep(1)
        if found_key:  # Kontrollerar om spelaren har nyckeln
            success = input("Vill du använda din nyckel som ett vapen? (ja/nej): ").strip().lower()
            if success == "ja":
                print("Du använder nyckeln för att övermanna vakten och kan nu fortsätta.")
                time.sleep(1)
                print("Du kan nu gå tillbaka till den långa korridoren och undersöka ett annat rum.")
                enter_room()  # Går tillbaka till rummet
            elif success == "nej":
                print("Vakten övermannar dig och du blir fångad.")
                time.sleep(1)
                exit_lost_game()  # Spelaren förlorar spelet
            else:
                print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
                time.sleep(1)
                room_one()  # Återvänder till rum 1

        else:
            print("Du har ingen nyckel att använda som vapen. Vakten övermannar dig.")
            time.sleep(1)
            exit_lost_game()  # Spelaren förlorar spelet

    elif action == "försöka övertala":
        talk = True  # Spelaren har valt att prata
        print("Du försöker övertala vakten att låta dig gå.")
        time.sleep(1)
        talk_to_guard = input("Vill du berätta en historia om att du är oskyldig? (ja/nej): ").strip().lower()
        if talk_to_guard == "ja":
            print("Vakten tvekar lite på din historia men låter dig gå ändå.")
            time.sleep(1)
            enter_room()  # Går in i rummet
        elif talk_to_guard == "nej":
            print("Vakten är inte övertygad och fångar dig.")
            time.sleep(1)
            exit_lost_game()  # Spelaren förlorar spelet
        else:
            print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
            time.sleep(1)
            room_one()  # Återvänder till rum 1
    else:
        print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
        time.sleep(1)
        room_one()  # Återvänder till rum 1

def room_two():
    # Beskriver vad som händer när spelaren går in i rum 2.
    rad()
    print("När du går in i rummet ser du ett öppet fönster som du försöker att krypa igenom.")
    time.sleep(1)
    print("Du lyckas krypa ut genom fönstret och kom ut ur fängelset, Grattis!")
    time.sleep(1)
    exit_game()  # Spelaren vinner spelet

def room_three():
    # Beskriver vad som händer när spelaren går in i rum 3.
    global found_second_key  # Använder den globala variabeln för att spåra den andra nyckeln
    rad()
    time.sleep(1)
    print("I rum 3 hittar du en nyckel.")
    found_second_key = True  # Spelaren har nu hittat den andra nyckeln
    add_achievement("Andra nyckeln funnen!")  # Lägger till prestation
    action = input("Vill du fortsätta (kolla runt) i rummet eller (gå igenom) den öppna dörren på motsatta väggen?: ").strip().lower()
    time.sleep(1)
        
    if action == "kolla runt":
        print("Du fortsätter att undersöka rummet noggrant.")
        time.sleep(15)  # Simulerar att spelaren letar efter en lång tid
        print("Du kollade runt i rummet men hittade ingenting och fortsätter därför igenom den öppna dörren.")
        time.sleep(1)
        enter_corridor()  # Går in i korridoren
    elif action == "gå igenom":
        time.sleep(1)
        enter_corridor()  # Går in i korridoren
    else:
        print("Ogiltigt val, försök igen.")  # Meddelar om ogiltigt val
        time.sleep(1)
        room_three()  # Återvänder till rum 3

def enter_room():
    # Hanterar vad som händer när spelaren går in i rummet.
    global found_key, visited_room, visited_room_1, visited_room_2, visited_room_3
    rad()
    if not visited_room:
        print("Du går in genom den öppna dörren och ser en lång korridor med tre olika rum.")
        time.sleep(0.5)
        visited_room = True  # Rummet har nu besökts

    room_choice = input("Vilket av dessa tre rum vill du gå in i? (rum 1, rum 2, rum 3): ").strip().lower()
    time.sleep(0.5)
    if room_choice == "rum 1":
        time.sleep(1)
        room_one()  # Går in i rum 1
    elif room_choice == "rum 2":
        time.sleep(1)
        room_two()  # Går in i rum 2
    elif room_choice == "rum 3":
        time.sleep(1)
        room_three()  # Går in i rum 3
    else:
        print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
        time.sleep(1)
        enter_room()  # Återvänder för att fråga igen
        
def enter_corridor():
    # Hanterar vad som händer när spelaren går in i korridoren.
    global entered_corridor  # Använder den globala variabeln för att spåra om spelaren har gått in i korridoren
    rad()
    if entered_corridor != True:
        print("Du går genom den öppna dörren och möts av en lång korridor.")
        time.sleep(1)
        print("Korridoren har 15 fängelseceller och ett vakt rum.")
        time.sleep(1)
        print("Du ser att cellerna 2, 5, 9 och 11 är öppna.")
        entered_corridor = True  # Korridoren har nu besökts
        time.sleep(1)
    
    cell_choice = input("Vilken cell vill du gå in i? (2, 5, 9, 11) eller vill du gå in i (vakt rummet)?: ").strip().lower()
    time.sleep(1)
        
    if cell_choice == "2":
        time.sleep(1)
        cell_2()  # Går in i cell 2

    elif cell_choice == "5":
        time.sleep(1)
        cell_5()  # Går in i cell 5

    elif cell_choice == "9":
        time.sleep(1)
        cell_9()  # Går in i cell 9

    elif cell_choice == "11":
        time.sleep(1)
        cell_11()  # Går in i cell 11

    elif cell_choice == "vakt rummet":
        time.sleep(1)
        vakt_rum()  # Går in i vakt rummet

    else:
        print("Ogiltigt val, försök igen.")  # Meddelar om ogiltigt val
        time.sleep(1)
        enter_corridor() 

def cell_2():
    # Beskriver vad som händer när spelaren går in i cell 2.
    global visited_cell2  # Använder den globala variabeln för att spåra cell 2
    rad()
    if not visited_cell2:
        print("Du går in i fängelse cell nummer 2 och ser ett stort metallskåp som har en komplicerad matteekvation på sig och ett fyrsiffrigt lås.")
        time.sleep(1)
        explore = input("Vill du försöka (lösa) matteekvationen och testa om svaret är rätt kod till låset eller (gå tillbaka) till korridoren? ").strip().lower()
        visited_cell2 = True  # Cell 2 har nu besökts
    if explore == "lösa":
        print("Problemet som står på skåpet är x=((15^2+25^2)⋅(12-4)/10 + 500 ")
        svar = input("Vad är x lika med? ").strip().lower()
        if svar == "1180":
            print("Det är korrekt!")  # Meddelar att svaret är korrekt
            lock = input("Vill du testa koden på låset som hänger för skåpet? (Ja) (Nej) ").strip().lower()
            if lock == "ja":
                print("Koden till låset var korrekt, du öppnar skåpet och ser ett hål som ser tillräckligt stort ut för att krypa igenom.")
                krypa = input("Vill du försöka krypa igenom hålet? (ja) (nej) ").strip().lower()
                if krypa == "ja":
                    explore_hole()  # Går in i hålet
                if krypa == "nej":
                    print("Du väljer att inte krypa igenom hålet och går istället tillbaka till korridoren och utforskar där.")
                else:
                    print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
                    cell_2()  # Återvänder till cell 2
            elif lock == "nej":
                print("Istället för att skriva in koden du fick fram börjar du testa slumpmässiga koder")
                lock2 = "0"
                while lock2 != "1180":
                    lock2 = input("Vilken kod vill du testa? ").strip().lower()
            else:
                print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
        else:
            print("Fel svar, vill du försöka igen?")  # Meddelar att svaret var fel
            try_again = input("(Ja) (Nej) ").strip().lower()
            if try_again == "ja":
                cell_2()  # Återvänder till cell 2 för ett nytt försök
            elif try_again == "nej":
                print("Du väljer istället att gå tillbaka till korridoren och utforska vidare där")
                enter_corridor()  # Går tillbaka till korridoren

    elif explore == "gå tillbaka":
        time.sleep(1)
        enter_corridor()  # Går tillbaka till korridoren
    else:
        print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
        time.sleep(1)
        cell_2()  # Återvänder till cell 2

def cell_5():
    # Beskriver vad som händer när spelaren går in i cell 5.
    global gitarr, visited_cell5  # Använder globala variabler för att spåra gitarren och besök i cell 5
    rad()
    if not visited_cell5:
        print("Du går in i fängelse cell nummer 5")
        time.sleep(1)
        print("I cellen hittar du en gitarr")
        time.sleep(1)
        visited_cell5 = True  # Cell 5 har nu besökts
        add_achievement("Hittade en gitarr!")  # Lägger till prestation
    gitarren = input("Vad vill du göra med gitarren? (spela musik) eller använda den som ett (vapen) ").strip().lower()
    if gitarren == "spela musik":
        time.sleep(1)
        print("Du spelar så hög musik att vakterna hittar dig.")  # Spelaren blir upptäckt av vakterna
        time.sleep(1)
        exit_lost_game()  # Spelaren förlorar spelet
    elif gitarren == "vapen":
        time.sleep(1)
        gitarr = True  # Spelaren har nu använt gitarren som vapen
        print("Du slår sönder gitarren så att du får en vass träbit du kan använda för att attackera vakterna om du träffar på dem.")
        time.sleep(1)
        utforska_eller_tillbaka = input("Vill du fortsätta att (utforska) fängelseceller eller vill du (gå tillbaka)? ").strip().lower()
        if utforska_eller_tillbaka == "utforska":
            time.sleep(1)
            print("Du fortsätter att utforska rummet ")
            time.sleep(0.5)
            print("När du kollar runt i rummet märker du att ena delen av väggen bara är en bit tunn kartong.")
            time.sleep(1)
            print("Du tar bort kartongbiten och ser att det leder till ett stort hål som leder dig ut ur fängelset")
            time.sleep(1)
            exit_game()  # Spelaren vinner spelet
            
        elif utforska_eller_tillbaka == "gå tillbaka":
            time.sleep(1)
            print("Du går tillbaka ut till korridoren.")
            time.sleep(1)
            enter_corridor()  # Går tillbaka till korridoren
        else:
            print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
            time.sleep(1)
            cell_5()  # Återvänder till cell 5
    else:
        print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
        time.sleep(1)
        cell_5()  # Återvänder till cell 5

def cell_9():
    # Beskriver vad som händer när spelaren går in i cell 9.
    rad()
    print("Du går in i fängelse cell nummer 9")
    time.sleep(1)
    print("Cellen är helt tom förutom två sängar så du går tillbaka ut till korridoren och kan nu utforska ett annat rum.")
    time.sleep(1)
    enter_corridor()  # Går tillbaka till korridoren

def cell_11():
    # Beskriver vad som händer när spelaren går in i cell 11.
    rad()
    print("Du går in i fängelse cell nummer 11")
    time.sleep(1)
    print("När du kommer in i cellen ser du att det står en vakt där inne och söker igenom rummet.")
    time.sleep(1)
    print("Vakten märker att du inte borde vara där och drar dig tillbaka till en cell som du inte kan ta dig ut ur.")
    time.sleep(1)
    exit_lost_game()  # Spelaren förlorar spelet

def vakt_rum():
    # Beskriver vad som händer när spelaren går in i vakt rummet.
    global gitarr, visited_vakt_rum  # Använder globala variabler för att spåra gitarren och besök i vakt rummet
    rad()
    if not visited_vakt_rum:
        print("Du går in i vakt rummet och ser ett helt övervakningssystem över hela fängelset.")
        time.sleep(1)
        print("På väggen hänger också en av vakternas nycklar som du kan använda för att låsa upp alla dörrar i fängelset, detta inkluderar den låsta dörren bredvid dig som leder ut ur fängelset.")
        time.sleep(1)
        visited_vakt_rum = True  # Vakt rummet har nu besökts
        add_achievement("Besökte vakt rummet!")  # Lägger till prestation
    spring_eller_kolla = input("Vill du (springa) ut ur fängelset med hjälp av nycklarna du hittade eller (kolla) på övervakningskamerorna och leta efter andra sätt att ta dig ut? ").strip().lower()
    if spring_eller_kolla == "springa":
        time.sleep(1)
        print("Du öppnade dörren och började springa ut ur fängelset.")
        time.sleep(5)
        print("Du märkte dock inte att det stod en vakt utanför dörren på en rökpaus.")
        time.sleep(1)
        print("Vakten märker att du försöker fly och börjar jaga dig")
        time.sleep(1)
        fight_or_run = input("Vill du försöka (springa) ifrån vakten eller (slåss) mot vakten ").strip().lower()
        if fight_or_run == "springa":
            print("Vakten är snabbare än vad du är och fångar dig.")  # Spelaren blir fångad
            time.sleep(1)
            exit_lost_game()  # Spelaren förlorar spelet
        elif fight_or_run == "slåss":
            if gitarr == True:  # Kontrollerar om spelaren har gitarren
                print("Du använder gitarren du hittade förut för att hugga vakten i magen")
                time.sleep(1)
                print("Du lyckas hugga vakten i magen och kan nu springa ut ur fängelset utan att några andra vakter hittar dig.")
                time.sleep(1)
                exit_game()  # Spelaren vinner spelet
            else:
                print("Vakten lyckas övermanna dig med sin batong.")  # Spelaren blir övermannad
                time.sleep(1)
                exit_lost_game()  # Spelaren förlorar spelet
        else:
            print("Ogiltigt val, försök igen")  # Meddelar om ogiltigt val
            time.sleep(1)
            vakt_rum()  # Återvänder till vakt rummet

def explore_hole():
    # Beskriver vad som händer när spelaren kryper genom hålet.
    rad()
    print("Du kryper genom hålet men när du har gått halvvägs känner du att hålet har blivit mindre och du fastnar med höften.")
    time.sleep(1)
    print("Du försöker att komma loss från hålet men lyckas inte så du ligger där i flera timmar innan du blir hittad av en vakt.\nDu blir sedan utdragen ur hålet och vakten drar dig till en ny fängelsecell som du inte kan ta dig ut ur")
    time.sleep(1)
    exit_lost_game()  # Spelaren förlorar spelet

def enter_room2():
    # Beskriver vad som händer när spelaren går in i rum 2.
    rad()
    time.sleep(1)
    print("Du går till den stängda dörren och försöker öppna den och märker att den är upplåst.")
    time.sleep(1)
    print("Du går in genom dörren och ser en vakt.")
    time.sleep(1)
    interact_with_guard()  # Interagerar med vakten

def interact_with_guard():
    # Interagerar med vakten i rum 2.
    global found_key  # Använder den globala variabeln för att spåra nyckeln
    rad()
    print("Vad vill du göra? (slåss, springa): ")
    time.sleep(1)
    fight_or_run = input().strip().lower()  # Hämtar spelarens val
    time.sleep(1)
    if fight_or_run == "slåss":
        print("Du lyckas strypa vakten innan du fortsätter tar du även vaktens nyckel")
        time.sleep(1)
        found_key = True  # Spelaren har nu fått nyckeln
        add_achievement("Fick vaktens nyckel!")  # Lägger till prestation
        enter_room()  # Går tillbaka till rummet
    elif fight_or_run == "springa":
        print("Du försöker att springa men vakten fångar dig.")  # Spelaren blir fångad
        time.sleep(1)
        exit_lost_game()  # Spelaren förlorar spelet
    else:
        print("Ogiltigt val, försök igen.")  # Meddelar om ogiltigt val
        time.sleep(1)
        interact_with_guard()  # Återvänder för att fråga igen

def main():
    """Startar spelet genom att anropa startmenyn."""
    start_meny()  # Anropar startmenyn
    
if __name__ == "__main__":
    main()  # Startar spelet
