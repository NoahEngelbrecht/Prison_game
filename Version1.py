def welcome_message():
    print("Välkommen till fängelset. Ditt mål är att ta dig ut genom att lösa olika problem och komma förbi vakterna.")

def check_room():
    print("Du kollar runt i rummet.")
    print("Du hittar en liten svart nyckel som du kan använda för att låsa upp dina hand- och fotbojor.")
    print("Dörren är öppen så du kan gå ut.")

def try_open_door():
    print("Du försöker öppna dörren.")
    print("Dörren är öppen så du kan sakta gå ut ur rummet.")

def go_left():
    print("Du går vänster i flera minuter och ser ingenting av intresse.")
    print("Du känner att du måste återvända till korridoren för att fortsätta ditt äventyr.")

def go_right():
    print("Du går till höger och ser två dörrar, en som står öppen medan den andra är stängd.")
    door_action = input("Vill du gå till den öppna eller stängda dörren? (öppna/stängda): ").strip().lower()
    if door_action == "öppna":
        enter_room()
    elif door_action == "stängda":
        enter_room2()
    else:
        print("Ogiltligt val")

def enter_room():
    print("Du går in genom den öppna dörren och ser en lång korridor med tre olika rum.")
    room_choice = input("Vilket av dessa tre rum vill du gå in i? (rum 1, rum 2, rum 3): ").strip().lower()
    if room_choice == "rum 1":
        print("")
    elif room_choice == "rum 2":
        print("Rum 2 är tomt.")
    elif room_choice == "rum 3":
        print("I rum 3 hittar du en nyckel.")
    else:
        print("Ogiltigt val, försök igen.")

def enter_room2():
    print("Du går till den stängda dörren och försöker öppna den och märker att den är upplåst.")
    print("Du går in genom dörren och ser en vakt")
    interact_with_guard()
    

def interact_with_guard():
    print("Vad vill du göra? (slåss, springa): ")
    fight_or_run = input().strip().lower()
    if fight_or_run == "slåss":
        print("Du lyckas strypa vakten och kan nu fortsätta.")
    elif fight_or_run == "springa":
        print("Du försöker att springa men vakten fångar dig.")
    else:
        print("Ogiltigt val, försök igen.")

def main():
    welcome_message()
    
    while True:
        action = input("Vad vill du göra? (kolla runt, öppna dörren): ").strip().lower()
        
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
        
        if next_action == "vänster":
            go_left()
            print("Du återvänder till korridoren.")
            continue
        elif next_action == "höger":
            go_right()
        else:
            print("Ogiltigt val, försök igen.")
        
        play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
        if play_again != "ja":
            print("Tack för att du spelade!")
            break

if __name__ == "__main__":
    main()
