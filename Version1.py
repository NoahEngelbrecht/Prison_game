import time

def welcome_message():
    print("Välkommen till fängelset. Ditt mål är att ta dig ut genom att lösa olika problem och komma förbi vakterna.")
    time.sleep(1)

def exit_game():
    print("Grattis du lyckas ta dig ut ur fängelset")
    time.sleep(1)
    exit

def check_room():
    print("Du kollar runt i rummet.")
    time.sleep(1)
    print("Du hittar en liten svart nyckel som du kan använda för att låsa upp dina hand- och fotbojor.")
    time.sleep(1)
    print("Dörren är öppen så du kan gå ut.")
    time.sleep(1)


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
        print("Ogiltligt val")
        go_right()

def enter_room():
    print("Du går in genom den öppna dörren och ser en lång korridor med tre olika rum.")
    time.sleep(0.5)
    room_choice = input("Vilket av dessa tre rum vill du gå in i? (rum 1, rum 2, rum 3): ").strip().lower()
    time.sleep(0.5)
    if room_choice == "rum 1":
        print("När du går in i detta rum ser du en vakt som direkt känner igen dig från dina tidigare försök att fly från fängelset.")
        time.sleep(1)
        input("")
        time.sleep(1)
    elif room_choice == "rum 2":
        print("När du går in i rummet ser du ett öppet fönster som du försöker att krypa igenom.")
        time.sleep(1)
        print("Du lyckas krypa ut genom fönstret och kom ut ur fängelset, Grattis!")
        time.sleep(1)
        exit_game()
    elif room_choice == "rum 3":
        time.sleep(1)
        print("I rum 3 hittar du en nyckel.")
    else:
        time.sleep(1)
        print("Ogiltigt val, försök igen.")
        enter_room()

def enter_room2():
    time.sleep(1)
    print("Du går till den stängda dörren och försöker öppna den och märker att den är upplåst.")
    time.sleep(1)
    print("Du går in genom dörren och ser en vakt")
    time.sleep(1)
    interact_with_guard()
    

def interact_with_guard():
    print("Vad vill du göra? (slåss, springa): ")
    time.sleep(1)
    fight_or_run = input().strip().lower()
    time.sleep(1)
    if action == "kolla runt":
        if fight_or_run == "slåss":
            print("Du lyckas strypa vakten och kan nu fortsätta.")
            time.sleep(1)
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
            time.sleep(1)
            check_room()
            break  
        elif action == "öppna dörren":
            time.sleep(1)
            try_open_door()
            break  
        else:
            print("Ogiltigt val, försök igen.")
            time.sleep(1)

    while True:
        next_action = input("Vill du gå vänster eller höger? (vänster/höger): ").strip().lower()
        time.sleep(1)
        
        if next_action == "vänster":
            time.sleep(1)
            go_left()
            print("Du återvänder till korridoren.")
            time.sleep(1)
            continue
        elif next_action == "höger":
            time.sleep(1)
            go_right()
            time.sleep(1)
        else:
            print("Ogiltigt val, försök igen.")
            time.sleep(1)
        
        play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
        time.sleep(1)
        if play_again != "ja":
            print("Tack för att du spelade!")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
