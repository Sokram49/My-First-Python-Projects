"""
My first choose your own adventure game.
hardcoded as shit
idk why i put so much into this
"""

print("This is a game where you choose your own adventure! anytime you want to quit press Q")

name = input("Type your name: ").lower()
print(name,"starts their journey...")

answer = input("You are stranded on an island, what would you like to do? (gather wood/find food/look around)")

if answer == "q":
  quit()

if answer == "gather wood":
  answer = input("You manage to gather enough wood to start a fire, do you want to (start fire) or (look for food)? ")
  if answer == "start fire":
    answer = input("You start the fire and it starts to get dark, do you want to (sleep) or (stay up)? ")
    if answer == "stay up":
      answer = input("You stay up and hear an ominous howl, do you (go check) or (stay)? ")
      if answer == "go check":
        answer = input("You go check and find a little hut, do you go (in) or (back)? ")
        if answer == "in":
          answer = input("You enter the hut and find that its empty but it seems theres a latch on the floor, do you open it? (yes/no) ")
          if answer == "yes":
            print("You open the latch and fall in, you find youself in a room full of treasures and anything you could ever want! The End.")

          elif answer == "no":
            print("You leave the latch alone but find that the space starts closing in, you are squished to death.")
        elif answer == "back":
          print("You go back but you can't find your fire so you got lost and died.")
      elif answer == "stay":
        print("You stay but get attacked by a wild boar and you die.")
    elif answer == "sleep":
      print("You go to sleep and never wake up.")

  elif answer == "look for food":
    answer = input("Luckily you found some food before it go dark, do you (eat) or (start fire)? ")
    if answer == "start fire":
      answer = input("You start a fire and eat your food, do you want to sleep now? (yes/no) ")
      if answer == "no":
        answer = input("You stay up and suddenly feel the urge to release a massive dookie, do dookie? (yes/no) ")
        if answer == "yes":
          answer = input("You take a massive dookie and feel relieved do you want to sleep now? (yes/no) ")
          if answer == "yes":
            answer = input("You go to sleep and wake up to the lovely morning sun, you see a boat in the distance do you swim to it? (yes/no) ")
            if answer == "yes":
              print("You start to swim to the boat and they notice you, you manage to get on the boat and are saved! The End.")

            elif answer == "no":
              print("You decide not to swim so you do nothing die.")
          elif answer == "no":
            print("You try to stay up but pass out and die.")
        elif answer == "no":
          print("You die from self-dookie.")
      elif answer == "yes":
        print("You are are attacked in your sleep and die.")
    elif answer == "eat":
      print("You eat but you die because you had no warmth.")

elif answer == "find food":
  answer = input("You find some wild berries and fruit, do you (eat) or (look for wood)? ")
  if answer == "look for wood":
    answer = input("You manage to find enough wood for a fire do you want to start it? (yes/no) ")
    if answer == "yes":
      answer = input("Now you have your fire, what would you like to do now? (explore/rest) ")
      if answer == "explore":
        answer = input("You go exploring and find a little creek do you want to (bathe) or (drink)? ")
        if answer == "drink":
          answer = input("You drink some and feel refreshed, do you want to explore more? (yes/no) ")
          if answer == "yes":
            print("You find a secret passage and enter a whole village whith vibrant people, they welcome you and take you in. The End.")

          elif answer == "no":
            print("You get lost and die.")
        elif answer == "bathe":
          print("You bathe but a wild animal comes out and kills you.")            
      elif answer == "rest":
        print("You lie down but your clothes catch on fire and you die.")
    elif answer == "no":
      print("You don't start the fire and die from the cold.")  

  elif answer == "eat":
    answer = input("You eat and now what do you want to do? (find water/sleep) ")
    if answer == "sleep":
      answer = input("You take a lil nap and wake up to the sun setting, you need to start a fire do you want to go look for wood? (yes/no) ")
      if answer == "yes":
        answer = input("You manage to find wood and get a fire going, you see a suspicious light in the distance wanna check? (yes/no) ")
        if answer == "yes":
          answer = input("You head towards the light and find a strange device, leave it alone? (yes/no) ")
          if answer == "no":
            answer = input("You mess with the device and you start to feel sleepy, resist the sleepiness? (yes/no) ")
            if answer == "no":
              print("You fall asleep and wake up back in your room, it was all a dream...")

            elif answer == "yes":
             print("You resist the sleepiness but you pass out and die.")
          elif answer == "yes":
            print("You leave the device alone and head back but you find the device again, you run away but find the device another time, your stuck in a loop, you go insane and die.")
        elif answer == "no":
          print("You decide not to check but a wild animal comes out and kills you.")
      elif answer == "no":
        print("You do nothing and die.")
    elif answer == "find water":
      print("You couldn't find water and die.")

elif answer == "look around":
  answer = input("You make sense of your surroundings and see some smoke in the distance, do you go to the smoke? (yes/no) ")  
  if answer == "yes":
    answer = input("you head towards the smoke and find someone sitting near a fire, do you want to (approach) or (go back) ")
    if answer == "approach":
      answer = input("You approach the person and are able to communicate, they are in the same position as you, help them? (yes/no) ")
      if answer == "yes":
        answer = input("You decide to help them out and manage to gather lots of supplies, do you want to try to make (shelter) or (weapons) ")
        if answer == "weapons":
          answer = input("You make weapons and go out to hunt and bring back meat to cook, do you want to explore more? (yes/no) ")
          if answer == "no":
            print("You sit with your friend to eat and you both are enjoying the moment, you think being stranded on this island wont be so bad after all. The End.")
          
          elif answer == "yes":
            print("You explore more but get attacked by a wild animal and die.")
        elif answer == "shelter":
          print("You try to make shelter but fail miserably and die from exhaustion.")
      elif answer == "no":
        print("You decide to fight them but they kill you.")
    elif answer == "go back":
      print("You go back but get lost and die.")

  elif answer == "no":
    answer = input("you stay where you are and think about what you could do, do you want to gather materials? (yes/no) ")
    if answer == "yes":
      answer = input("You manage to gather quite a bit, you could either make a (raft) or (fire) which one? ")
      if answer == "raft":
        answer = input("You set sail on your raft with little materials leftover, do you want to make something with the leftovers? (yes/no) ")
        if answer == "yes":
          answer = input("You manage to make a fishing rod and catch some fish, do you want to eat it? (yes/no) ")
          if answer == "no":
            answer = input("You don't eat it but then you see some aircraft in the sky, do you try to get its attention? (yes/no) ")
            if answer == "Yes":
              print("You manage to get its attention and it rescues you. The End.")

            elif answer == "no":
              print("You missed your only chance of survival and spend the rest of your days at sea and end up dying.")
          elif answer == "yes":
            print("You eat the fish but you are poisoned and die.")
        elif answer == "no":
          print("You save your leftovers but then a whale swallows you up and you die.")
      elif answer == "fire":
        print("You fail to make a fire and waste your materials, with nothing left you die.")
    elif answer == "no":
      print("You do nothing and die.")

else:
  print("You do nothing and die.")

print(f"Thank you for playing {name}!")
