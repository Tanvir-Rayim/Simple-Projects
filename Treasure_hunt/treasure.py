print(r'''
      __                                                      
     /  l                                                     
   .'   :               __.....__..._  ____                   
  /  /   \          _.-"        "-.  ""    "-.                
 (`-: .---:    .--.'          _....J.         "-.             
  """y     \,.'    \  __..--""       `+""--.     `.           
    :     .'/    .-"""-. _.            `.   "-.    `._.._     
    ;  _.'.'  .-j       `.               \     "-.   "-._`.   
    :    / .-" :          \  `-.          `-      "-.      \  
     ;  /.'    ;          :;               ."        \      `,
     :_:/      ::\        ;:     (        /   .-"   .')      ;
       ;-"      ; "-.    /  ;           .^. .'    .' /    .-" 
      /     .-  :    `. '.  : .- / __.-j.'.'   .-"  /.---'    
     /  /      `,\.  .'   "":'  /-"   .'       \__.'          
    :  :         ,\""       ; .'    .'      .-""              
   _J  ;         ; `.      /.'    _/    \.-"                  
  /  "-:        /"--.b-..-'     .'       ;                    
 /     /  ""-..'            .--'.-'/  ,  :                    
:`.   :     / : bug         `-i" ,',_:  _ \                   
:  \  '._  :__;             .'.-"; ; ; j `.l                  
 \  \          "-._         `"  :_/ :_/                       
  `.;\             "-._                                       
    :_"-._             "-.                                    
      `.  l "-.     )     `.                                  
        ""^--""^-. :        \                                 
                  ";         \                                
                  :           `._                             
                  ; /    \ `._   ""---.                       
                 / /   _      `.--.__.'                       
                : :   / ;  :".  \                             
                ; ;  :  :  ;  `. `.                           
               /  ;  :   ; :    `. `.                         
              /  /:  ;   :  ;     "-'                         
             :_.' ;  ;    ; :                                 
                 /  /     :_l                                 
                 `-'                                          
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_turn = input("Two door in front of you. Which one will you pick? (Left or Right) : ").lower()
if first_turn == "left":
    second_turn = input("You come across a River. What would you do? (Wait or Swim) : ").lower()
    if second_turn == "wait":
        third_turn = input("Now you were teleported. You have three doors, choose carefully. (Red, Blue or Yellow) :").lower()
        if third_turn == "yellow":
            print("Congratulations! You have found the treasure!")
        elif third_turn == "red":
            print("Burned by fire. Game Over!")
        elif third_turn == "blue":
            print("Taken by ORCS. Game Over!")
        else:
            print("Game Over!")
    elif second_turn == "swim":
        print("Eaten by sharks. Game Over!")
    else:
        print("Game Over!")
elif first_turn == "right":
    print("Fell into a hole. Game Over!")
else:
    print("Game Over!")
