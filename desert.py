print(""".    _    *     .  ______   .          .     '      .            '+
  (      |||      _   _|      |___   .   *    '    .         *
    ||  ||||| .  | | |   | |      |       .    '                    .    '
 __||||_|||||____| |_|_____________|________________________________________
 . |||| |||||  ||   _____      _____  .   .       .             .       .
  . ||`-'|||| ||||    __________            .
     |__ |||| ||||      .          .     .     .        -            .   .
  __    ||||`-'|||  .       .    __________
 .    . |||| ___|  ___________             .
 _   ___|||||__  _           .          _
      _ `---'    .   .    .   _   .   .    .
 _  ^      .  -    .    -    .       -    .    .  .      -   .     .    -
                                                   _   __""")
while True:
    print("Welcome to the Deadliest Desert!!!")
    print("You lost your way in the desert! Do you need help! (yes/no)")
    choice = input().lower()
    if choice == 'yes':
        print("""--------------------------------------------------------------------------------------------------------------------""")
        print("""Ok then, head towards north direction and walk about 2 hours you will reach a palm tree.""")
        hint1 = input("You will take rest here till evening or start immediately (rest/start) : ").lower()
        print("""--------------------------------------------------------------------------------------------------------------------""")
        if hint1 == 'rest':
            print("You hit by a deadliest sand storm")
            print("******************")
            print("*****YOU DIED*****")
            print("******************")

        elif hint1 == 'start':
            print("Again start your journey towards north, by evening you reach an Oasis!")
            hint2 = input("""Drink water and take rest tonight here or start your journey (rest/start) : """).lower()
            print("""--------------------------------------------------------------------------------------------------------------------""")
            if hint2 == 'rest':
                print("Desert animals attacked night time!")
                print("******************")
                print("*****YOU DIED*****")
                print("******************")
            elif hint2 == 'start':
                print("""Now look into the sky and follow the brightest star till morning!\nNow take some rest and again start your journey towards north!""")
                hint3 = input("""A Deadliest Sand Storm is coming. Run or lay down and cover yourself (run/cover) :  """)
                print( """--------------------------------------------------------------------------------------------------------------------""")
                if hint3 == 'run':
                    print("Sand Storm hit badly")
                    print("******************")
                    print("*****YOU DIED*****")
                    print("******************")

                elif hint3 == 'cover':
                    print("You have escaped from storm and found a Highway!")
                    print("*******************************")
                    print("*****HURRAY! YOU SURVIVED!*****")
                    print("*******************************")

                    break
                else:
                    print("Choose right choice")
                    print("""--------------------------------------------------------------------------------------------------------------------""")

            else:
                print("Choose right choice")
                print("""--------------------------------------------------------------------------------------------------------------------""")

        else:
            print("Choose right choice")
            print("""--------------------------------------------------------------------------------------------------------------------""")

    elif choice == 'no':
        print("You lost the way in the desert!")
        print("******************")
        print("*****YOU DIED*****")
        print("******************")
    else:
        print("Choose right choice")
        print("""--------------------------------------------------------------------------------------------------------------------""")


