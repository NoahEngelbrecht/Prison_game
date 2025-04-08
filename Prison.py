import time

found_key = False  
visited_room = False  
found_second_key = False
went_right = False
visited_room_1 = False
visited_room_2 = False
visited_room_3 = False
fight = False
talk = False
entered_corridor = False
gitarr = False
visited_cell5 = False
visited_vakt_rum = False

def start_meny():
    print("""Välkommen till mitt Prison Game spel
Du har tre olika val.
1. Spela spelet
2. Läsa instruktionerna
3. Avsluta spelet.""")
    start_val = input("Vad vill du göra? ").strip().lower()
    if start_val == "spela spelet":
        welcome_message()
        start_room()
    elif start_val == "läsa instruktionerna":
        print("\n")
        filnamn = "Readme.txt"
        try:
            with open(filnamn, "r", encoding="utf-8") as fil:
                content = fil.read()
                print(content)
        except FileNotFoundError:
            print(f"Filen '{filnamn}' kunde inte hittas.")
        except Exception as e:
            print(f"Ett fel inträffade: {e}")
        input("Tryck på valfri tangent för att fortsätta...")
        start_meny()
    elif start_val == "avsluta spelet":
        exit()
    else:
        print("Ogiltigt val, försök igen")
        start_meny()

def welcome_message():
    print("Välkommen till fängelset. Ditt mål är att ta dig ut genom att lösa olika problem och komma förbi vakterna.")
    # time.sleep(1)

def exit_game():
    print("Grattis, du lyckas ta dig ut ur fängelset!")
    # time.sleep(0.3)
    play_again()

def exit_lost_game():
    print("Du lyckades inte ta dig ut ur fängelset.")
    # time.sleep(0.3)
    play_again()

def play_again():
    play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
    # time.sleep(1)
    if play_again != "ja":
        print("Tack för att du spelade!")
        exit()
        # time.sleep(1)
    if play_again == "ja":
        print("Varsågod att försöka igen")
        main()

def start_room():
    action = input("Vad vill du göra? (kolla runt, öppna dörren): ").strip().lower()
    # time.sleep(1)
    if action == "kolla runt":
        check_room()  
    elif action == "öppna dörren":
        try_open_door()
    else:
        print("Ogiltigt val, försök igen.")
        start_room()

def check_room():
    global found_key
    print("Du kollar runt i rummet.")
    # time.sleep(1)
    print("Du hittar en liten vass nyckel som du kan använda för att låsa upp dina hand- och fotbojor.")
    # time.sleep(1)
    print("Dörren är öppen så du kan gå ut.")
    found_key = True 
    go_left_or_right()

def try_open_door():
    print("Du försöker öppna dörren.")
    # time.sleep(1)
    print("Dörren är öppen så du kan sakta gå ut ur rummet.")
    # time.sleep(1)
    go_left_or_right()

def go_left_or_right():
    next_action = input("Vill du gå vänster eller höger? (vänster/höger): ").strip().lower()
    # time.sleep(1)
        
    if next_action == "vänster":
        go_left()
        print("Du återvänder till korridoren.")
        # time.sleep(1)
        go_right()
    elif next_action == "höger":
        go_right()
        # time.sleep(1)
    else:
        print("Ogiltigt val, försök igen.")
        go_left_or_right()

def go_left():
    print("Du går vänster i flera minuter och ser ingenting av intresse.")
    # time.sleep(1)
    print("Du känner att du måste återvända till korridoren för att fortsätta ditt äventyr.")
    # time.sleep(1)

def go_right():
    global went_right
    if not went_right:
        print("Du går till höger och ser två dörrar, en som står öppen medan den andra är stängd.")
        # time.sleep(0.5)
    door_action = input("Vill du gå till den öppna eller stängda dörren? (öppna/stängda): ").strip().lower()
    # time.sleep(1)
    if door_action == "öppna":
        enter_room()
    elif door_action == "stängda":
        enter_room2()
    else:
        print("Ogiltigt val")
        go_right()

def room_one():
    global visited_room_1, fight, talk
    if not visited_room_1:
        print("När du går in i detta rum ser du en vakt som direkt känner igen dig från dina tidigare försök att fly från fängelset.")
        # time.sleep(1)
        print("Vakten säger: 'Du ska inte vara här! Vad vill du göra?'")
        # time.sleep(1)
        visited_room_1 = True
        
    action = input("Vill du (slåss) eller (försöka övertala) vakten?: ").strip().lower()
    # time.sleep(1)
        
    if action == "slåss":
        fight = True
        print("Du försöker slåss mot vakten!")
        # time.sleep(1)
        if found_key:  
            success = input("Vill du använda din nyckel som ett vapen? (ja/nej): ").strip().lower()
            if success == "ja":
                print("Du använder nyckeln för att övermanna vakten och kan nu fortsätta.")
                # time.sleep(1)
                print("Du kan nu gå tillbaka till den långa korridoren och undersöka ett annat rum.")
                enter_room()
            elif success == "nej":
                print("Vakten övermannar dig och du blir fångad.")
                # time.sleep(1)
                exit_lost_game()
            else:
                print("Ogiltigt val, försök igen")
                room_one()

        else:
            print("Du har ingen nyckel att använda som vapen. Vakten övermannar dig.")
            # time.sleep(1)
            exit_lost_game()
    elif action == "försöka övertala":
        talk = True
        print("Du försöker övertala vakten att låta dig gå.")
        # time.sleep(1)
        talk_to_guard = input("Vill du berätta en historia om att du är oskyldig? (ja/nej): ").strip().lower()
        if talk_to_guard == "ja":
            print("Vakten tvekar lite på din historia men låter dig gå ändå.")
            # time.sleep(1)
            enter_room()
        elif talk_to_guard == "nej":
            print("Vakten är inte övertygad och fångar dig.")
            # time.sleep(1)
            exit_lost_game()
        else:
            print("Ogiltigt val, försök igen")
            room_one()
    else:
        print("Ogiltigt val, försök igen")
        room_one()

def room_two():
    print("När du går in i rummet ser du ett öppet fönster som du försöker att krypa igenom.")
    # time.sleep(1)
    print("Du lyckas krypa ut genom fönstret och kom ut ur fängelset, Grattis!")
    # time.sleep(1)
    exit_game()

def room_three():
    global found_second_key
    # time.sleep(1)
    print("I rum 3 hittar du en nyckel.")
    found_second_key = True 
    action = input("Vill du (fortsätta kolla runt) i rummet eller (gå igenom den öppna dörren) på motsatta väggen?: ").strip().lower()
    # time.sleep(1)
        
    if action == "fortsätta kolla runt":
        print("Du fortsätter att undersöka rummet noggrant.")
        # time.sleep(15)
        print("Du kollade runt i rummet men hittade ingenting och fortsätter därför igenom den öppna dörren.")
        # time.sleep(1)
        enter_corridor()
    elif action == "gå igenom den öppna dörren":
        enter_corridor()
    else:
        print("Ogiltigt val, försök igen.")
        room_three()

def enter_room():
    global found_key, visited_room, visited_room_1, visited_room_2, visited_room_3
    if not visited_room:
        print("Du går in genom den öppna dörren och ser en lång korridor med tre olika rum.")
        # time.sleep(0.5)
        visited_room = True  

    room_choice = input("Vilket av dessa tre rum vill du gå in i? (rum 1, rum 2, rum 3): ").strip().lower()
    # time.sleep(0.5)
    if room_choice == "rum 1":
        room_one()
    elif room_choice == "rum 2":
        room_two()
    elif room_choice == "rum 3":
        room_three()
    else:
        print("Ogiltigt val, försök igen")
        enter_room()
        
def enter_corridor():
    global entered_corridor
    if entered_corridor != True:
        print("Du går genom den öppna dörren och möts av en lång korridor.")
        # time.sleep(1)
        print("Korridoren har 15 fängelseceller och ett vakt rum.")
        # time.sleep(1)
        print("Du ser att cellerna 2, 5, 9 och 11 är öppna.")
        entered_corridor = True
        # time.sleep(1)
    
    cell_choice = input("Vilken cell vill du gå in i? (2, 5, 9, 11) eller vill du gå in i (vakt rummet)?: ").strip().lower()
    # time.sleep(1)
        
    if cell_choice == "2":
        cell_2()


    elif cell_choice == "5":
        cell_5()

    elif cell_choice == "9":
        cell_9()


    elif cell_choice == "11":
        cell_11()

    elif cell_choice == "vakt rummet":
        vakt_rum()

    else:
        print("Ogiltigt val, försök igen.")
        enter_corridor()
def cell_2():
    print("Du går in i fängelse cell nummer 2 och ser ett stort hål i väggen")
    explore = input("Vill du (utforska) hålet eller (gå tillbaka) till korridoren? ").strip().lower()
    if explore == "utforska":
        explore_hole()
    elif explore == "gå tillbaka":
        enter_corridor()
    else:
        print("Ogiltigt val, försök igen")
        cell_2()

def cell_5():
    global gitarr, visited_cell5
    if not visited_cell5:
        print("Du går in i fängelse cell nummer 5")
        print("I cellen hittar du en gitarr")
        visited_cell5 = True
    gitarren = input("Vad vill du göra med gitarren? (spela musik) eller använda den som ett (vapen) ")
    if gitarren == "spela musik":
        print("Du spelar så hög musik att vakterna hittar dig.")
        exit_lost_game()
    elif gitarren == "vapen":
        gitarr = True
        print("Du slår sönder gitarren så att du får en vass träbit du kan använda för att attackera vakterna om du träffar på dem.")
        utforska_eller_tillbaka = input("Vill du fortsätta att (utforska) fängelseceller eller vill du (gå tillbaka)? ")
        if utforska_eller_tillbaka == "utforska":
            print("Du fortsätter att utforska rummet ")
            print("När du kollar runt i rummet närker du att ena delen av väggen bara är en bit tunn kartong.")
            print("Du tar bort kartong biten och ser att det leder till ett stort hål som leder dig ut ur fängelset")
            exit_game()
            
        elif utforska_eller_tillbaka == "gå tillbaka":
            print("Du går tillbaka ut till korridoren.")
            enter_corridor()
        else:
            print("Ogiltigt val, försök igen")
            cell_5()
    else:
        print("Ogiltigt val, försök igen")
        cell_5()

def cell_9():
    print("Du går in i fängelse cell nummer 9")
    print("Cellen är helt tom förutom två sängar så du går tillbaka ut till korridoren och kan nu utforska ett annat rum.")
    enter_corridor()

def cell_11():
    print("Du går in i fängelse cell nummer 11")
    print("När du kommer in i cellen ser du att det står en vakt där inne och söker igenon rummet.")
    print("Vakten märker att du inte borde vara där och drar dig tillbaka till en cell som du inte kan ta dig ut ur.")
    exit_lost_game()

def vakt_rum():
    global gitarr, visited_vakt_rum
    if not visited_vakt_rum:
        print("Du går in i vakt rummet och ser ett helt övervakningsystem över hela fängelset.")
        print("På väggen hänger också en av vakternas nycklar som du kan använda för att låsa upp alla dörrar i fängelset detta inkluderar den låste dörren bredvid dig som leder ut ur fängelset.")
        visited_vakt_rum = True
    spring_eller_kolla = input("Vill du (springa) ut ur fängelset med hjälp av nycklarna du hittade eller (kolla) på övervakningskamrorna och leta efter andra sätt att ta dig ut? ")
    if spring_eller_kolla == "springa":
        print("Du öppnade dörren och började springa ut ur fängelset.")
        time.sleep(5)
        print("Du märkte dock inte att det stog en vakt utanför dörren på en rökpaus.")
        print("Vakten märker att du försöker fly och börjar jaga dig")
        fight_or_run = input("Vill du försöka (springa) ifrån vakten eller (slåss) mot vakten ")
        if fight_or_run == "springa":
            print("Vakten är snabbare än vad du är och fångar dig.")
            exit_lost_game()
        elif fight_or_run == "slåss":
            if gitarr == True:
                print("Du använder gitarren du hittade förut för att hugga vakten i magen")
                print("DU lyckas hugga vakten i magen och kan nu springa ut ur fängelset utan att några andra vakten hittar dig.")
                exit_game()
            else:
                print("Vakten lyckas övermanne dig med sin batong.")
                exit_lost_game()
        else:
            print("Ogiltigt val, försök igen")
            vakt_rum()
        

def explore_hole():
    print("Du kryper genom hålet men när du har gått halvvägs känner du att hålet har blivit mindre och du fastnar med höften.")
    print("Du försöker att komma loss från hålet men lyckas inte så du ligger där i flera timmar innan du blir hittad av en vakt.\nDu blir sedan utdragen ur hålet och vakten drar dig till en ny fängelsecell som du inte kan ta dig ut ur")
    exit_lost_game()

def enter_room2():
    # time.sleep(1)
    print("Du går till den stängda dörren och försöker öppna den och märker att den är upplåst.")
    # time.sleep(1)
    print("Du går in genom dörren och ser en vakt.")
    # time.sleep(1)
    interact_with_guard()

def interact_with_guard():
    global found_key
    print("Vad vill du göra? (slåss, springa): ")
    # time.sleep(1)
    fight_or_run = input().strip().lower() 
    # time.sleep(1)
    if fight_or_run == "slåss":
        print("Du lyckas strypa vakten innan du fortsätter tar du även vaktens nyckel")
        # time.sleep(1)
        found_key = True
        enter_room()
    elif fight_or_run == "springa":
        print("Du försöker att springa men vakten fångar dig.")
        # time.sleep(1)
    else:
        print("Ogiltigt val, försök igen.")
        # time.sleep(1)
        interact_with_guard()

def main():
    start_meny()
    
    

if __name__ == "__main__":
    main()
