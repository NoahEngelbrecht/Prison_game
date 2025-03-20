import time


found_key = False  
visited_room = False  
found_second_key = False  

def welcome_message():
    print("Välkommen till fängelset. Ditt mål är att ta dig ut genom att lösa olika problem och komma förbi vakterna.")
    time.sleep(1)

def exit_game():
    print("Grattis, du lyckas ta dig ut ur fängelset!")
    time.sleep(1)
    exit() 

def check_room():
    global found_key
    print("Du kollar runt i rummet.")
    time.sleep(1)
    print("Du hittar en liten vass nyckel som du kan använda för att låsa upp dina hand- och fotbojor.")
    time.sleep(1)
    print("Dörren är öppen så du kan gå ut.")
    found_key = True 

def try_open_door():
    print("Du försöker öppna dörren.")
    time.sleep(1)
    print("Dörren är öppen så du kan sakta gå ut ur rummet.")
    time.sleep(1)

def go_left():
    print("Du går vänster i flera minuter och ser ingenting av intresse.")
    time.sleep(1)
    print("Du känner att du måste återvända till korridoren för att fortsätta ditt äventyr.")
    time.sleep(1)

def go_right():
    print("Du går till höger och ser två dörrar, en som står öppen medan den andra är stängd.")
    time.sleep(1)
    door_action = input("Vill du gå till den öppna eller stängda dörren? (öppna/stängda): ").strip().lower()
    time.sleep(1)
    if door_action == "öppna":
        enter_room()
    elif door_action == "stängda":
        enter_room2()
    else:
        print("Ogiltigt val")
        go_right()

def enter_room():
    global found_key, visited_room
    if not visited_room:
        print("Du går in genom den öppna dörren och ser en lång korridor med tre olika rum.")
        time.sleep(0.5)
        visited_room = True  

    room_choice = input("Vilket av dessa tre rum vill du gå in i? (rum 1, rum 2, rum 3): ").strip().lower()
    time.sleep(0.5)
    if room_choice == "rum 1":
        print("När du går in i detta rum ser du en vakt som direkt känner igen dig från dina tidigare försök att fly från fängelset.")
        time.sleep(1)
        print("Vakten säger: 'Du ska inte vara här! Vad vill du göra?'")
        time.sleep(1)
        
        action = input("Vill du (slåss) eller (försöka övertala) vakten?: ").strip().lower()
        time.sleep(1)
        
        if action == "slåss":
            print("Du försöker slåss mot vakten!")
            time.sleep(1)
            if found_key:  
                success = input("Vill du använda din nyckel som ett vapen? (ja/nej): ").strip().lower()
                if success == "ja":
                    print("Du använder nyckeln för att övermanna vakten och kan nu fortsätta.")
                    time.sleep(1)
                    print("Du kan nu gå tillbaka till den långa korridoren och undersöka ett annat rum.")
                    enter_room()
                elif success == "nej":
                    print("Vakten övermannar dig och du blir fångad.")
                    time.sleep(1)
                    exit_game()
            else:
                print("Du har ingen nyckel att använda som vapen. Vakten övermannar dig.")
                time.sleep(1)
                exit_game()
        elif action == "försöka övertala":
            print("Du försöker övertala vakten att låta dig gå.")
            time.sleep(1)
            persuasion = input("Vill du berätta en historia om att du är oskyldig? (ja/nej): ").strip().lower()
            if persuasion == "ja":
                print("Vakten tvekar lite på din historia men låter dig gå ändå.")
                time.sleep(1)
                enter_room()
            else:
                print("Vakten är inte övertygad och fångar dig.")
                time.sleep(1)
                exit_game()
    elif room_choice == "rum 2":
        print("När du går in i rummet ser du ett öppet fönster som du försöker att krypa igenom.")
        time.sleep(1)
        print("Du lyckas krypa ut genom fönstret och kom ut ur fängelset, Grattis!")
        time.sleep(1)
        exit_game()
    elif room_choice == "rum 3":
        time.sleep(1)
        print("I rum 3 hittar du en nyckel.")
        found_second_key = True 
        action = input("Vill du (fortsätta kolla runt) i rummet eller (gå igenom den öppna dörren) på motsatta väggen?: ").strip().lower()
        time.sleep(1)
        
        if action == "fortsätta kolla runt":
            print("Du fortsätter att undersöka rummet noggrant.")
            time.sleep(1)
            check_room()
        elif action == "gå igenom den öppna dörren":
            enter_corridor()
        else:
            print("Ogiltigt val, försök igen.")
            enter_room()
    else:
        time.sleep(1)
        print("Ogiltigt val, försök igen.")
        enter_room()

def enter_corridor():
    print("Du går genom den öppna dörren och möts av en lång korridor.")
    time.sleep(1)
    print("Korridoren har 15 fängelseceller och ett vakt rum.")
    time.sleep(1)
    print("Du ser att cellerna 2, 5, 9 och 11 är öppna.")
    time.sleep(1)
    
    while True:
        cell_choice = input("Vilken cell vill du gå in i? (2, 5, 9, 11) eller vill du gå in i (vakt rummet)?: ").strip().lower()
        time.sleep(1)
        
        if cell_choice in ["2", "5", "9", "11"]:
            print(f"Du går in i cell {cell_choice}.")
            time.sleep(1)
            print("Det är en tom cell. Du kan återvända till korridoren.")
            input("Tryck på Enter för att återvända till korridoren.")
        elif cell_choice == "vakt rummet":
            print("Du går in i vakt rummet.")
            time.sleep(1)
            print("Vakten är inte här. Du kan undersöka rummet.")
            input("Tryck på Enter för att återvända till korridoren.")
        else:
            print("Ogiltigt val, försök igen.")

def enter_room2():
    time.sleep(1)
    print("Du går till den stängda dörren och försöker öppna den och märker att den är upplåst.")
    time.sleep(1)
    print("Du går in genom dörren och ser en vakt.")
    time.sleep(1)
    interact_with_guard()

def interact_with_guard():
    global found_key
    print("Vad vill du göra? (slåss, springa): ")
    time.sleep(1)
    fight_or_run = input().strip().lower() 
    time.sleep(1)
    if fight_or_run == "slåss":
        print("Du lyckas strypa vakten innan du fortsättar tar du även vaktens nyckel")
        time.sleep(1)
        found_key = True
        enter_room()
    elif fight_or_run == "springa":
        print("Du försöker att springa men vakten fångar dig.")
        time.sleep(1)
    else:
        print("Ogiltigt val, försök igen.")
        time.sleep(1)
        interact_with_guard()

def main():
    welcome_message()
    
    while True:
        action = input("Vad vill du göra? (kolla runt, öppna dörren): ").strip().lower()
        time.sleep(1)
        
        if action == "kolla runt":
            check_room()
            break  
        elif action == "öppna dörren":
            try_open_door()
            break  
        else:
            print("Ogiltigt val, försök igen.")

    while True:
        next_action = input("Vill du gå vänster eller höger? (vänster/höger): ").strip().lower()
        time.sleep(1)
        
        if next_action == "vänster":
            go_left()
            print("Du återvänder till korridoren.")
            time.sleep(1)
            continue
        elif next_action == "höger":
            go_right()
            time.sleep(1)
        else:
            print("Ogiltigt val, försök igen.")
        
        play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
        time.sleep(1)
        if play_again != "ja":
            print("Tack för att du spelade!")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
