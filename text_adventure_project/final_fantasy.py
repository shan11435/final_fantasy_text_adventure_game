import time
import random
items = []
level = []
choice = []
quest = []
weapon = ["buster sword", "iron sword", "metal sword", "sword of artorias"]
# continue line 1837
# complete rocket town gold quest
# continue cave_choice_two quest
# penny from shinra wants to reunite with her family
# need titanium, and myrthil shard for master sword
# defeat cave monster to get titanium and LV2
# get gold from cave soldier
# rocket town requires gold
# to buy fire in rocket town you need gold
# you find penny family in rocket town, you bring them back to her
"""you don't have any gold because you spent it to get here
but the clerk would do a trade for the fire spell"""
# clerk will use flower to gain the love of a girl in town
# clerk says the flower can be found in a forest
# you leave rocket town to go to the forest
# you find flower
# you go deeper in the forest and encounter another monster
# you obtain a myrthil shard and LV3
# you go back to rocket town and trade the flower for a fire spell
# you leave the shop
# the clerk is rejected by girl cause hes too old
# you go to another town
# it's blocked by a huge spell
# luckily since you gained the spell, you burn the tree down and go in
# if you have master sword you kill cyclops
# if not your dead
# based on the choice you made in the cave, endings are different
# line 166 work on cave choice 3
# work on cave_monster scenario


def print_pause(string):
    print(string)
    time.sleep(1)


def inventory():
    for i in items:
        print_pause(i)


def stats():
    print_pause(level[len(level) - 1])


def tasks():
    for i in quest:
        print_pause(i)


def play_game():
    print_pause("welcome to the world of midgar")
    print_pause("you are a soldier of shinra")
    print_pause("todays' task is to take down a cyclops")
    print_pause("reported in a town in midgar")
    print_pause("the chief tells you \"good luck\"")
    print_pause("then proceeds to hand you your")
    items.append(random.choice(weapon))
    print_pause(items[0])
    print_pause("inventory updated")
    print_pause("whenever you see inventory updated ")
    print_pause("this means something was added or removed in "
                "your inventory")
    level.append("LV1")
    quest.append("main quest: kill cyclops")
    quest.append("main quest: go to rocket town")
    print_pause("quest log updated")
    print_pause("whenever you see quest log updated ")
    print_pause("this means either a side quest was added "
                "or removed")
    print_pause("or a main quest was added or removed")
    print_pause("to win the game you must complete "
                "all main quests")
    print_pause("throughout the game")
    print_pause("you have to choose what to do")
    print_pause("to choose, type the number next to "
                "the choice")
    print_pause("for example, type 1 for choice 1")
    print_pause("type 2 for choice 2, etc...")
    shinra()


def restart_game():
    response = input("would you like to restart? y or n\n").lower()
    if(response in "y"):
        items.clear()
        level.clear()
        choice.clear()
        quest.clear()
        play_game()
    elif(response in "n"):
        print_pause("I hope you enjoyed it")
    else:
        print_pause("sorry I don't understand, please type y or n")


def shinra():
    print_pause("you are currently in the city of shinra")
    print_pause("there appears to be a logo outside a building "
                "that appears to be an item shop")
    print_pause("there appears to be a scared lady, might be because "
                "of witnessing the cyclops")
    print_pause("a big gate that's labeled \"midger\" is guarded "
                "by shinra soldiers")
    shinra_question()


def shinra_question():
    response = input("what do you wanna do next?\n"
                     "1. go to item shop\n"
                     "2. speak to the lady\n"
                     "3. go to midgar\n"
                     "4. look at inventory\n"
                     "5. look at current level\n"
                     "6. look at quest log\n")
    if(response in "1"):
        item_shop()
    elif(response in "2"):
        if("side quest: bring penny family back" in quest):
            quest.remove("side quest: bring penny family back")
            print_pause("she turns around and can't believe her eyes")
            print_pause("her family appears before her")
            print_pause("they both cry tears of joy")
            print_pause("they are reunited")
            print_pause("penny: I CAN'T BELIEVE YOU FOUND THEM!!!!")
            print_pause("Penny: thank you")
            print_pause("Penny: here's a token of my appreciation")
            print_pause("acquired diamond")
            items.append("diamond")
            print_pause("inventory updated")
            print_pause("quest log updated")
            # use this to change penny's fate in the ending
            shinra_question()
        elif("diamond" in items):
            print_pause("penny: thanks again for making this possible")
            shinra_question()
        elif("side quest: find penny family" in quest):
            print_pause("Penny: the monster is big, better be "
                        "prepared before doing this")
            print_pause("Penny: it was at cosmo canyon")
            print_pause("Penny: I'm counting on you to find my family "
                        ", good luck")
            shinra_question()
        else:
            print_pause("you approach the lady")
            shinra_lady()
    elif(response in "3"):
        print_pause("you approach the big gate")
        print_pause("before you walk out, you show your employee ID "
                    "to the soldiers")
        print_pause("shinra soldier: good luck on your task, and "
                    "make shinra proud")
        # if you have korok forest quest, midgar function will change
        if("main quest: get hyrule herb in korok forest" in quest):
            midgar_version_2()
        elif("main quest: bring hyrule herb back "
             "to rocket town item shop clerk" in quest):
            midgar_version_2()
        elif("fire" in items):
            midgar_version_2()
        else:
            midgar()
    elif(response in "4"):
        inventory()
        shinra_question()
    elif(response in "5"):
        stats()
        shinra_question()
    elif(response in "6"):
        tasks()
        shinra_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        shinra_question()


def shinra_lady():
    print_pause("her whole body is shaking and her face has the look"
                " of terror")
    response = input("lady: what do you want?\n"
                     "1. what's wrong with you?\n"
                     "2. never mind\n")
    if(response in "1"):
        shinra_lady_response()
    elif(response in "2"):
        shinra()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        shinra_lady()


def shinra_lady_response():
    print_pause("lady: my town is being overrun by a giant thing with one eye")
    print_pause("lady: so many lives gone because of the "
                "incompetance of shinra")
    print_pause("lady: I hope my family were able to escape like I did")
    print_pause("lady: sorry where are my manners, my name is Penny Jenkins")
    response = input("1. what town is this occuring?\n")
    if(response in "1"):
        print_pause("Penny: in cosmo canyon")
        shinra_lady_response_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        shinra_lady_response()


def shinra_lady_response_question():
    response = input("1. I work for shinra and it's my task to end "
                     "this, and I'll go look for your family\n"
                     "2. sorry what town again?\n")
    if(response in "1"):
        print_pause("Penny: YOU WILL!!!")
        print_pause("Penny: thank you so much")
        print_pause("Penny: I was wrong, not all of the soldiers "
                    "are bad")
        print_pause("Penny: there's hope after all")
        print_pause("Penny: take this necklace and show it to them when"
                    " you find them")
        items.append("penny necklace")
        quest.append("side quest: find penny family")
        print_pause("Penny: I'm counting on you")
        print_pause("inventory updated")
        print_pause("quest log updated")
        print_pause("CONGRATULATIONS!!!")
        print_pause("you found a side quest")
        print_pause("completing these are not neccessary")
        print_pause("to win the game")
        print_pause("but, completing them")
        print_pause("will alter the ending")
        shinra_question()
    elif(response in "2"):
        print_pause("Penny: you deaf or something, in cosmo canyon")
        shinra_lady_response_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        shinra_lady_response_question()


def item_shop():
    print_pause("you are currently in the item shop")
    print_pause("you see a clerk at the counter")
    item_shop_question()


def item_shop_question():
    response = input("what do you wanna do next?\n"
                     "1. speak to clerk\n"
                     "2. go to shinra\n")
    if(response in "1"):
        print_pause("you approach the clerk")
        clerk_question()
    elif(response in "2"):
        shinra()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        item_shop_question()


def clerk_question():
    response = input("clerk: what can I help you with?\n"
                     "1. here to buy\n"
                     "2. any information on the cyclops attack\n"
                     "3. is there another town nearby?\n"
                     "4. Nothing thank you\n")
    if(response in "1"):
        clerk_items()
    elif(response in "2"):
        clerk_speak()
    elif(response in "3"):
        clerk_speak2()
    elif(response in "4"):
        print_pause("you can collect materials by defeating monsters ")
        print_pause("and level up as well")
        print_pause("I heard a report of one in a cave")
        print_pause("and another in some kind of forest")
        item_shop()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        clerk_question()


def clerk_speak():
    print_pause("clerk: A CYCLOPS ATTACK!,")
    print_pause("clerk: man midgar needs a force field to keep away"
                " these monsters")
    print_pause("clerk: sorry kid first time i'm hearing about this")
    print_pause("clerk: I really hope shinra is on its way to stop it")
    print_pause("clerk: I can't imagine what they're going through")
    clerk_question()


def clerk_speak2():
    print_pause("clerk: ahh yes")
    print_pause("clerk: there's a town called rocket town")
    print_pause("clerk: once you go to midgar")
    print_pause("clerk: it's the next town after us")
    print_pause("clerk: you can't miss it")
    clerk_question()


def clerk_items():
    if("master sword" in items):
        print_pause("clerk: you already bought everything I have")
        clerk_question()
    else:
        response = input("clerk: splendid here's what I have\n"
                         "1. master sword\n"
                         "2. never mind\n")
        if(response in "1"):
            master_sword()
        elif(response in "2"):
            clerk_question()
        else:
            print_pause("I don't understand,\n"
                        "please type the number next to the choice\n"
                        "for example, type 1 for choice 1\n"
                        "type 2 for choice 2, etc...")
            clerk_items()


def master_sword():
    if("titanium" in items):
        if("myrthil shard" in items):
            if("LV3" in level):
                items.remove("titanium")
                items.remove("myrthil shard")
                quest.remove("main quest: buy master sword from "
                             "shinra item shop")
                print_pause("clerk: I CAN'T BELIEVE IT!!!!!")
                print_pause("clerk: you must've grinded alot to do "
                            "this")
                print_pause("you have acquired the master sword")
                items.append("master sword")
                print_pause("inventory updated")
                print_pause("quest log updated")
                clerk_question()
            else:
                print_pause("you need to be a high level to be able "
                            "to wield it")
        else:
            print_pause("you need a myrthil shard and be a high "
                        "level to be able to wield it")
            clerk_question()
    else:
        print_pause("you need to acquire titanium, a myrthil shard, "
                    "and a high level to be able to wield it")
        clerk_question()


def midgar():
    print_pause("you are currently in midgar")
    print_pause("you breath the fresh air")
    print_pause("you take a second to appreciate the vast world ")
    print_pause("in the distance you see a town ")
    print_pause("you also see a cave")
    print_pause("you also see a gate that leads to shinra")
    midgar_question()


def midgar_question():
    response = input("where do you go next\n"
                     "1. go to town 1\n"
                     "2. go to cave\n"
                     "3. go to shinra\n"
                     "4. look at inventory\n"
                     "5. look at current level\n"
                     "6. look at quest log\n")
    if(response in "1"):
        if("pass" in items):
            rocket_town()
        else:
            town_1()
    elif(response in "2"):
        cave()
    elif(response in "3"):
        if("cyclops eye" in items):
            # ending
            """ add an if statement based on the cave choice
                which will change the ending """
            # if acquired diamond, penny fate changes
            if("carry him back to base" in choice):
                ending_one()
            elif("slay the monster for him" in choice):
                ending_two()
            elif("end him, he'll die with honor" in choice):
                ending_three()
        else:
            shinra()
    elif(response in "4"):
        inventory()
        midgar_question()
    elif(response in "5"):
        stats()
        midgar_question()
    elif(response in "6"):
        tasks()
        midgar_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        midgar_question()


def town_1():
    print_pause("you approach the town")
    print_pause("unfortunately you get stopped by a guard")
    print_pause("guard: noone goes in here without paying with gold")
    if("gold" in items):
        if("main quest: go to town 1" in quest):
            quest.remove("main quest: go to town 1")
            quest.remove("main quest: go to rocket town")
            quest.append("main quest: buy fire from rocket town item clerk")
            print_pause("guard: Thank you, hope you enjoy your visit")
            print_pause("guard: and welcome to rocket town")
            print_pause("guard: take this pass")
            print_pause("acquired rocket town pass")
            items.append("pass")
            print_pause("guard: now you have unlimited access to the town")
            print_pause("inventory updated")
            print_pause("quest log updated")
            rocket_town()
        else:
            quest.remove("main quest: go to rocket town")
            quest.append("main quest: buy fire from rocket town item clerk")
            print_pause("guard: Thank you, hope you enjoy your visit")
            print_pause("guard: and welcome to rocket town")
            print_pause("guard: take this pass")
            print_pause("acquired rocket town pass")
            items.append("pass")
            print_pause("guard: now you have unlimited access to the town")
            print_pause("inventory updated")
            print_pause("quest log updated")
            rocket_town()
    elif("main quest: investigate the cave" in quest):
        print_pause("I might get lucky and find it")
        print_pause("in the cave")
        midgar_question()
    else:
        print_pause("maybe showing that you're from shinra will "
                    "persuade them to let you in")
        print_pause("guard: I don't care who you work with, rules "
                    "are rules")
        print_pause("I should explore other areas to obtain it")
        quest.append("main quest: investigate the cave")
        print_pause("quest log updated")
        midgar_question()


def rocket_town():
    print_pause("you are currently in rocket town")
    print_pause("you see a huge rusted rocket in the center")
    print_pause("you see an item shop")
    if("diamond" in items):
        rocket_town_2_question()
    elif("side quest: bring penny family back" in quest):
        rocket_town_2_question()
    else:
        print_pause("you see a family sitting on a bench looking "
                    "terrified")
        rocket_town_question()


def rocket_town_2_question():
    response = input("what do you do next?\n"
                     "1. go to item shop\n"
                     "2. back to midgar\n"
                     "3. look at inventory\n"
                     "4. look at current level\n"
                     "5. look at quest log\n")
    if(response in "1"):
        rocket_town_item_shop()
    elif(response in "2"):
        # if you have korok forest quest, midgar function will change
        if("main quest: get hyrule herb in korok forest" in quest):
            midgar_version_2()
        elif("main quest: bring hyrule herb back "
             "to rocket town item shop clerk" in quest):
            midgar_version_2()
        elif("fire" in items):
            midgar_version_2()
        else:
            midgar()
    elif(response in "3"):
        inventory()
        rocket_town_2_question()
    elif(response in "4"):
        stats()
        rocket_town_2_question()
    elif(response in "5"):
        tasks()
        rocket_town_2_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        rocket_town_2_question()


def rocket_town_question():
    response = input("what do you do next?\n"
                     "1. go to item shop\n"
                     "2. speak to family\n"
                     "3. back to midgar\n"
                     "4. look at inventory\n"
                     "5. look at current level\n"
                     "6. look at quest log\n")
    if(response in "1"):
        rocket_town_item_shop()
    elif(response in "2"):
        # if you have find penny family quest, this function should change
        print_pause("you approach the family")
        penny_family()
    elif(response in "3"):
        # if you have korok forest quest, midgar function will change
        if("main quest: get hyrule herb in korok forest" in quest):
            midgar_version_2()
        elif("main quest: bring hyrule herb back "
             "to rocket town item shop clerk" in quest):
            midgar_version_2()
        elif("fire" in items):
            midgar_version_2()
        else:
            midgar()
    elif(response in "4"):
        inventory()
        rocket_town_question()
    elif(response in "5"):
        stats()
        rocket_town_question()
    elif(response in "6"):
        tasks()
        rocket_town_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        rocket_town_question()


def midgar_version_2():
    print_pause("you are currently in midgar")
    print_pause("you breath the fresh air")
    print_pause("you take a second to appreciate the vast world")
    print_pause("in the distance you see rocket town")
    print_pause("you also see a cave")
    print_pause("you also see a forest")
    print_pause("you also see another town")
    print_pause("you also see a gate that leads to shinra")
    midgar_version_2_question()


def midgar_version_2_question():
    response = input("where do you go next\n"
                     "1. go to rocket town\n"
                     "2. go to cave\n"
                     "3. go to town 2\n"
                     "4. go to shinra\n"
                     "5. go to forest\n"
                     "6. look at inventory\n"
                     "7. look at current level\n"
                     "8. look at quest log\n")
    if(response in "1"):
        rocket_town()
    elif(response in "2"):
        cave()
    elif(response in "3"):
        town_2()
    elif(response in "4"):
        if("cyclops eye" in items):
            # ending
            """ add an if statement based on the cave
            choice which will change the ending """
            # if acquired diamond, penny fate changes
            if("carry him back to base" in choice):
                ending_one()
            elif("slay the monster for him" in choice):
                ending_two()
            elif("end him, he'll die with honor" in choice):
                ending_three()
        else:
            shinra()
    elif(response in "5"):
        # this is where you get the hyrule herb and destroy the monster for LV3
        korok_forest()
    elif(response in "6"):
        inventory()
        midgar_version_2_question()
    elif(response in "7"):
        stats()
        midgar_version_2_question()
    elif(response in "8"):
        tasks()
        midgar_version_2_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        midgar_version_2_question()


def ending_one():
    print_pause("as soon as you enter Shinra HQ")
    print_pause("the chief approaches you ")
    print_pause("you tell him the task has been taken care of")
    print_pause("chief: well done, I didn't doubt you for one bit")
    print_pause("chief promotes you to lieutenant")
    print_pause("a group of rookies approaches you")
    print_pause("chief: they are now under your wing")
    print_pause("chief: whatever you say, they'll do")
    print_pause("you appreciate and accept your role as lieutenant")
    print_pause("the group salutes you and they accept you as their "
                "lieutenant")
    if("side quest: find penny family" in quest):
        if("diamond" in items):
            print_pause("you leave the HQ, and penny and her family "
                        "approach you")
            print_pause("penny: we were wondering if you wanna come "
                        "to our place for dinner")
            print_pause("you accept the offer")
            print_pause("penny: this is our way of fully thanking "
                        "you for reuniting us")
            print_pause("you didn't realize how important this was "
                        "for penny until today")
            print_pause("you go back to your house to sleep and can't "
                        "wait to start your first day as lieutenant")
            print_pause("in the middle of the night")
            print_pause("you wake up to the sound of footsteps")
            print_pause("the sound is coming closer to you")
            print_pause("you hide against the wall quickly grabbing "
                        "your sword")
            print_pause("you see your door slowly opening")
            print_pause("you see him coming slowly to your bed with "
                        "a knife in his hand")
            print_pause("you bust out your sword and stab the "
                        "intruder in the stomach")
            print_pause("you turn on the lights")
            print_pause("you can't believe who the intruder is")
            print_pause("it's the soldier back in the cave")
            print_pause("you wonder why he would want to kill you")
            print_pause("the sound of the scream from the soldier")
            print_pause("caused Shinra security to barge in your "
                        "door")
            print_pause("they come to your room")
            print_pause("security: sir are you okay? we could've "
                        "sworn we heard screami-")
            print_pause("they were shocked to find out that it "
                        "wasn't you who needed saving")
            print_pause("rather it was a fellow soldier")
            print_pause("you try to explain it's not what it looks "
                        "like")
            print_pause("security: don't even bother you just "
                        "murdered a comrade")
            print_pause("security: I can't believe I'm saying this")
            print_pause("you're under arrest, you are no longer a "
                        "part of Shinra")
            print_pause("they put you in handcuffs and also seize "
                        "your weapon")
            print_pause("but why would a soldier whose life I saved "
                        "want to kill me?")
            print_pause("you go to court")
            print_pause("judge: I see you recently saved the town "
                        "of cosmo canyon from the terror of a monster")
            print_pause("judge: for that, I'll change the punishment "
                        " from terminated of shinra")
            print_pause("judge: to one year suspension")
            restart_game()
        else:
            print_pause("there's a news breaking on tv")
            print_pause("reporter: a girl is seen on the ground "
                        "confirmed dead")
            print_pause("you can't believe it, that girl is penny")
            print_pause("reporter: we see her window open, this "
                        "seems like a suicide")
            print_pause("reporter: in her room, there is a note "
                        "which reads")
            print_pause("\"I will see my family soon\"")
            print_pause("you feel devastated, because this could've"
                        " been prevented by reuniting the family")
            print_pause("you go back to your house feeling "
                        "disappointed you didn't keep your promise")
            print_pause("you think about what her parents might "
                        "be feeling right now")
            print_pause("you blame yourself for this happening")
            print_pause("you go to sleep to try to forget about this")
            print_pause("in the middle of the night")
            print_pause("you wake up to the sound of footsteps")
            print_pause("the sound is coming closer to you")
            print_pause("you hide against the wall quickly grabbing "
                        "your sword")
            print_pause("you see your door slowly opening")
            print_pause("you see him coming slowly to your bed with "
                        "a knife in his hand")
            print_pause("you bust out your sword and stab the "
                        "intruder in the stomach")
            print_pause("you turn on the lights")
            print_pause("you can't believe who the intruder is")
            print_pause("it's the soldier back in the cave")
            print_pause("you wonder why he would want to kill you")
            print_pause("the sound of the scream from the soldier")
            print_pause("caused shinra security to barge in your door")
            print_pause("they come to your room")
            print_pause("security: sir are you okay? we could've "
                        "sworn we heard screami-")
            print_pause("they were shocked to find out that it "
                        "wasn't you who needed saving")
            print_pause("rather it was a fellow soldier")
            print_pause("you try to explain it's not what it looks like")
            print_pause("security: don't even bother you just "
                        "murdered a fellow comrade")
            print_pause("security: I can't believe I'm saying this")
            print_pause("you're under arrest, you are no longer a "
                        "part of shinra")
            print_pause("they put you in handcuffs and also seize "
                        "your weapon")
            print_pause("but why would a soldier whose life I saved "
                        "want to kill me?")
            print_pause("you go to court")
            print_pause("judge: I see you recently saved the town of"
                        " cosmo canyon from the terror of a monster")
            print_pause("judge: for that I'll change the punishment "
                        "from terminated of shinra")
            print_pause("judge: to one year suspension")
            restart_game()
    else:
        print_pause("there's a news breaking on tv")
        print_pause("reporter: a girl is seen on the ground confirmed dead")
        print_pause("reporter: we see her window open, this seems "
                    "like a suicide")
        print_pause("reporter: in her room, there is a note which reads ")
        print_pause("\"I will see my family soon\"")
        print_pause("you go back to your house to sleep and can't "
                    "wait to start your first day as lieutenant")
        print_pause("in the middle of the night")
        print_pause("you wake up to the sound of footsteps")
        print_pause("the sound is coming closer to you")
        print_pause("you hide against the wall quickly grabbing "
                    "your sword")
        print_pause("you see your door slowly opening")
        print_pause("you see him coming slowly to your bed with a "
                    "knife in his hand")
        print_pause("you bust out your sword and stab the intruder "
                    "in the stomach")
        print_pause("you turn on the lights")
        print_pause("you can't believe who the intruder is")
        print_pause("it's the soldier back in the cave")
        print_pause("you wonder why he would want to kill you")
        print_pause("the sound of the scream from the soldier")
        print_pause("caused Shinra security to barge in your door")
        print_pause("they come to your room")
        print_pause("security: sir are you okay? we could've sworn "
                    "we heard screami-")
        print_pause("they were shocked to find out that it wasn't "
                    "you who needed saving")
        print_pause("rather it was a fellow soldier")
        print_pause("you try to explain it's not what it looks like")
        print_pause("security: don't even bother you just murdered "
                    "a comrade")
        print_pause("security: I can't believe I'm saying this")
        print_pause("you're under arrest, you are no longer a part "
                    "of Shinra")
        print_pause("they put you in handcuffs and also seize your "
                    "weapon")
        print_pause("but why would a soldier whose life I saved "
                    "want to kill me?")
        print_pause("you go to court")
        print_pause("judge: I see you recently saved the town of "
                    "cosmo canyon from the terror of a monster")
        print_pause("judge: for that I'll change the punishment "
                    "from terminated of Shinra")
        print_pause("judge: to one year suspension")
        restart_game()


def ending_two():
    print_pause("as soon as you enter Shinra HQ")
    print_pause("the chief approaches you ")
    print_pause("you tell him the task has been taken care of")
    print_pause("chief: well done, I didn't doubt you for one bit")
    print_pause("chief promotes you to lieutenant")
    print_pause("a group of rookies approaches you")
    print_pause("chief: they are now under your wing")
    print_pause("chief: whatever you say, they'll do")
    print_pause("you appreciate and accept your role as lieutenant")
    print_pause("the group salutes you and they accept you as their "
                "lieutenant")
    if("side quest: find penny family" in quest):
        if("diamond" in items):
            print_pause("you leave the HQ, and penny and her family "
                        "approach you")
            print_pause("penny: we were wondering if you wanna come "
                        "to our place for dinner")
            print_pause("you accept the offer")
            print_pause("penny: this is our way of fully thanking "
                        "you for reuniting us")
            print_pause("you didn't realize how important this was "
                        "for penny until today")
            print_pause("as you walk toward your house, you see the "
                        "soldier you rescued back in the cave")
            print_pause("come toward you")
            print_pause("soldier: I just came by to say thank you, "
                        "I want you to meet my family")
            print_pause("the soldiers' wife comes up to you and "
                        "hugs you")
            print_pause("soldier wife: I don't care whether he "
                        "finished the task or not")
            print_pause("soldier wife: all I care for is his return"
                        " and you made that possible")
            print_pause("although you feel accomplished by being "
                        "promoted to lieutenant")
            print_pause("you realize reuniting pennies family and "
                        "saving the soldier")
            print_pause("is a much bigger accomplishment")
            print_pause("you go home and can't wait to start your "
                        "first day as lieutenant")
            restart_game()
        else:
            print_pause("there's a news breaking on tv")
            print_pause("reporter: a girl is seen on the ground "
                        "confirmed dead")
            print_pause("you can't believe it, that girl is penny")
            print_pause("reporter: we see her window open, this "
                        "seems like a suicide")
            print_pause("reporter: in her room, there is a note"
                        " which reads")
            print_pause("\"I will see my family soon\"")
            print_pause("you feel devastated because this could've "
                        "been prevented by reuniting the family")
            print_pause("as you walk toward your house, you see the "
                        "soldier you rescued back in the cave")
            print_pause("come toward you")
            print_pause("soldier: I just came by to say thank you I "
                        "want you to meet my family")
            print_pause("the soldiers' wife comes up to you and hugs "
                        "you")
            print_pause("soldier wife: I don't care whether he "
                        "finished the task or not")
            print_pause("soldier wife: all I care for is his return "
                        "and you made that possible")
            print_pause("you go back to your house feeling disappointed "
                        "you didn't keep your promise")
            print_pause("you think about what her parents might be "
                        "feeling right now")
            print_pause("you blame yourself for this happening")
            print_pause("but seeing the soldier happy made the "
                        "feeling lessen")
            print_pause("at the end of the day you're only human")
            print_pause("you can't solve everyone's problems")
            print_pause("you go to sleep to try to forget about this")
            restart_game()
    else:
        print_pause("there's a news breaking on tv")
        print_pause("reporter: a girl is seen on the ground confirmed dead")
        print_pause("reporter: we see her window open, this seems "
                    "like a suicide")
        print_pause("reporter: in her room, there is a note which reads")
        print_pause("\"I will see my family soon\"")
        print_pause("as you walk toward your house, you see the "
                    "soldier you rescued back in the cave")
        print_pause("come toward you")
        print_pause("soldier: I just came by to say thank you I "
                    "want you to meet my family")
        print_pause("the soldiers' wife comes up to you and hugs you")
        print_pause("soldier wife: I don't care whether he finished "
                    "the task or not")
        print_pause("soldier wife: all I care for is his return and "
                    "you made that possible")
        print_pause("you go back to your house to sleep and can't "
                    "wait to start your first day as lieutenant")
        restart_game()


def ending_three():
    print_pause("as soon as you enter shinra HQ")
    print_pause("there's an announcement for a funeral for one of "
                "our fellow brother")
    print_pause("you recognize the man back in the cave")
    print_pause("you try to act normal")
    print_pause("the chief approaches you")
    print_pause("you tell him the task has been taken care of")
    print_pause("chief: well done, I didn't doubt you for one bit")
    print_pause("chief promotes you to lieutenant")
    print_pause("a group of rookies approach you")
    print_pause("chief: they are now under your wing")
    print_pause("chief: whatever you say, they'll do")
    print_pause("the feeling of guilt takes over your body")
    print_pause("you don't feel you deserve the rank of lieutenant")
    print_pause("although you appreciate the offer, you respectfully"
                " decline it")
    print_pause("everyone in the office is silent and stare at "
                "each other with confusion")
    print_pause("even the chief was confused")
    print_pause("chief: I don't understand, I already set up this"
                " group assuming you'll take the role")
    print_pause("this is not an offer I just give to everyone")
    print_pause("you tell the chief you just don't feel ready yet "
                "and need to take down more tasks before feeling so")
    print_pause("the chief digests your words for a bit and gives "
                "you a smile")
    print_pause("chief: I understand, you don't have to explain why")
    print_pause("chief: the offer will be on the table")
    print_pause("the group is still confused")
    print_pause("chief: well what are you just standing there for?")
    print_pause("GET BACK TO WORK!!!!!")
    if("side quest: find penny family" in quest):
        if("diamond" in items):
            print_pause("you leave the HQ, and penny and her family "
                        "approach you")
            print_pause("penny: we were wondering if you wanna come"
                        " to our place for dinner")
            print_pause("you really want to go")
            print_pause("but feel it'd be best if you attended the "
                        "funeral instead")
            print_pause("you tell them that you appreciate the offer"
                        " but you have somewhere important to be")
            print_pause("penny: it's fine, I understand, another time then")
            print_pause("you are at the funeral")
            print_pause("this soldier must've been loved in the "
                        "shinra community")
            print_pause("even people I recognized from rocket town "
                        "and cosmo canyon attended")
            print_pause("A mother and daughter by the tombstone "
                        "must be his wife and kid")
            print_pause("chief: based on body analysis, we have "
                        "concluded that this man wasn't murdered "
                        "by a monster")
            print_pause("rather by one of our own")
            print_pause("a big cut by his heart looks to be he was "
                        "stabbed")
            print_pause("the whole crowd is surprised to hear this")
            print_pause("chief: I know, the fact that our own brothers "
                        "would kill each other")
            print_pause("this surprised me as well")
            print_pause("chief: the suspect may very well be here "
                        "at this moment")
            print_pause("all the soldiers look around here for "
                        "suspicious faces")
            print_pause("you try to act your cool and not raise "
                        "suspicions")
            print_pause("the mother shouts")
            print_pause("soldier wife: whoever you are, WHY DON'T "
                        "YOU COME HERE AND FACE US LIKE A MAN!!!!")
            print_pause("chief: I agree, if you are here and confess"
                        " to the crime, the consequence will be far "
                        "less")
            print_pause("the chief stops talking and the funeral "
                        "proceeds")
            print_pause("but after hearing this, everyone is switching "
                        "their focus now on figuring out who the "
                        "suspect may be")
            print_pause("the funeral ends")
            print_pause("chief: this man was one of the most "
                        "loyal soldiers I know")
            print_pause("chief: A man who would never betray us")
            print_pause("then proceeds to look at you while saying this")
            print_pause("chief: that will be all folks have a good "
                        "day and remember")
            print_pause("chief: he may be gone, but he'll never "
                        "leave our hearts")
            print_pause("everyone leaves and you head back to your"
                        " house")
            print_pause("you go to sleep and try to forget what you "
                        "did")
            print_pause("at the end of the day, this is what he wanted")
            print_pause("I just wish people realize this")
            print_pause("in the middle of the night")
            print_pause("you wake up to banging on the door")
            print_pause("soldier: COME OUT COME OUT")
            print_pause("you're confused as to why they're here in "
                        "the middle of the night")
            print_pause("you open the door, and they quickly grab "
                        "you")
            print_pause("soldier: you're under arrest for the murder "
                        "of our fellow brother")
            print_pause("the chief approaches you")
            print_pause("chief: I knew my suspicions of you were true")
            print_pause("you can't believe they figured it out")
            print_pause("but you still try to act normal")
            print_pause("you tell them what's the meaning of this")
            print_pause("chief: quit acting like you're innocent")
            print_pause("chief: The whole time I was thinking why "
                        "you would decline such a big offer")
            print_pause("chief: then it hit me, it's the guilt of "
                        "murdering a soldier is what caused you to "
                        "decline it")
            print_pause("chief: but I was still thinking maybe I'm "
                        "being irrational")
            print_pause("chief: which is why I had to be sure by "
                        "doing a size analysis of your sword and "
                        " the cut of the body")
            print_pause("chief: it was an exact match, I couldn't "
                        "believe one of my prodigies would do such "
                        "a thing")
            print_pause("chief: but this is the right thing, you "
                        "are under arrest")
            print_pause("chief: and is sentenced to life in prison")
            print_pause("chief: from this day, you're no longer "
                        "considered a Shinra soldier")
            restart_game()
        else:
            print_pause("there's a news breaking on tv")
            print_pause("reporter: a girl is seen on the ground "
                        "confirmed dead")
            print_pause("you can't believe it, that girl is penny")
            print_pause("reporter: we see her window open, this "
                        "seems like a suicide")
            print_pause("reporter: in her room, there is a note "
                        "which reads")
            print_pause("\"I will see my family soon\"")
            print_pause("you feel devastated because this could've"
                        " been prevented by reuniting the family")
            print_pause("you think about what her parents might be "
                        "feeling right now")
            print_pause("you blame yourself for this happening")
            print_pause("you are at the funeral")
            print_pause("this soldier must've been loved in the"
                        " Shinra community")
            print_pause("even people I recognized from rocket town and"
                        "cosmo canyon attended")
            print_pause("A mother and daughter by the tombstone must "
                        "be his wife and kid")
            print_pause("chief: based on body analysis, we have concluded"
                        " that this man wasn't murdered by a monster")
            print_pause("rather by one of our own")
            print_pause("a big cut by his heart looks to be he was "
                        "stabbed")
            print_pause("the whole crowd is surprised to hear this")
            print_pause("chief: I know, the fact that our brothers"
                        " would kill each other")
            print_pause("this surprised me as well")
            print_pause("chief: the suspect may very well be here "
                        "at this moment")
            print_pause("all the soldiers look around here for "
                        "suspicious faces")
            print_pause("you try to act your cool and not raise "
                        "suspicions")
            print_pause("the mother shouts")
            print_pause("soldier wife: whoever you are, WHY DON'T "
                        "YOU COME HERE AND FACE US LIKE A MAN!!!!")
            print_pause("chief: I agree, if you are here and confess"
                        " to the crime, the consequence will be far less")
            print_pause("the chief stops talking and the funeral proceeds")
            print_pause("but after hearing this, everyone is "
                        "switching their focus now on figuring out "
                        "who the suspect may be")
            print_pause("the funeral ends")
            print_pause("chief: this man was one of the most loyal "
                        "soldiers I know")
            print_pause("chief: A man who would never betray us")
            print_pause("then proceeds to look at you while saying "
                        "this")
            print_pause("chief: that will be all folks have a good "
                        "day and remember")
            print_pause("chief: he may be gone, but he'll never"
                        " leave our hearts")
            print_pause("everyone leaves and you head back to your"
                        " house")
            print_pause("you go to sleep and try to forget what you did")
            print_pause("at the end of the day, this is what he wanted")
            print_pause("I just wish people realize this")
            print_pause("in the middle of the night")
            print_pause("you wake up to banging on the door")
            print_pause("soldier: COME OUT COME OUT")
            print_pause("you're confused as to why they're here in"
                        " the middle of the night")
            print_pause("you open the door, and they quickly grab you")
            print_pause("soldier: you're under arrest for the murder"
                        "of our fellow brother")
            print_pause("the chief approaches you")
            print_pause("chief: I knew my suspicions of you were true")
            print_pause("you can't believe they figured it out")
            print_pause("but you still try to act normal")
            print_pause("you tell them what's the meaning of this")
            print_pause("chief: quit acting like you're innocent")
            print_pause("chief: The whole time I was thinking why "
                        "you would decline such a big offer")
            print_pause("chief: then it hit me, it's the guilt of "
                        "murdering a soldier is what caused you to decline it")
            print_pause("chief: but I was still thinking maybe I'm "
                        "being irrational")
            print_pause("chief: which is why I had to be sure by "
                        "doing a size analysis of your sword and "
                        "the cut of the body")
            print_pause("chief: it was an exact match, I couldn't "
                        "believe one of my prodigies would do such "
                        "a thing ")
            print_pause("chief: but this is the right thing, you are"
                        " under arrest")
            print_pause("chief: and are sentenced to life in prison")
            print_pause("chief: from this day, you're no longer "
                        "considered a Shinra soldier")
            restart_game()
    else:
        print_pause("there's a news breaking on tv")
        print_pause("reporter: a girl is seen on the ground confirmed dead")
        print_pause("reporter: we see her window open, this seems "
                    "like a suicide")
        print_pause("reporter: in her room, there is a note which reads")
        print_pause("\"I will see my family soon\"")
        print_pause("you are at the funeral")
        print_pause("this soldier must've been loved in the Shinra "
                    "community")
        print_pause("even people I recognized from rocket town and "
                    "cosmo canyon attended")
        print_pause("A mother and daughter by the tombstone must be "
                    "his wife and kid")
        print_pause("chief: based on body analysis, we have concluded"
                    " that this man wasn't murdered by a monster")
        print_pause("rather by one of our own")
        print_pause("a big cut by his heart looks to be he was "
                    "stabbed")
        print_pause("the whole crowd is surprised to hear this")
        print_pause("chief: I know, the fact that our brothers "
                    "would kill each other")
        print_pause("this surprised me as well")
        print_pause("chief: the suspect may very well be here at "
                    "this moment")
        print_pause("all the soldiers look around here for suspicious"
                    " faces")
        print_pause("you try to act your cool and not raise suspicions")
        print_pause("the mother shouts")
        print_pause("soldier wife: whoever you are, WHY DON'T YOU "
                    "COME HERE AND FACE US LIKE A MAN!!!!")
        print_pause("chief: I agree, if you are here and confess to"
                    " the crime, the consequence will be far less")
        print_pause("the chief stops talking and the funeral proceeds")
        print_pause("but after hearing this, everyone is switching "
                    "their focus now on figuring out who the suspect"
                    " may be")
        print_pause("the funeral ends")
        print_pause("chief: this man was one of the most loyal "
                    "soldiers I know")
        print_pause("chief: A man who would never betray us")
        print_pause("then proceeds to look at you while saying this")
        print_pause("chief: that will be all folks have a good day "
                    "and remember")
        print_pause("chief: he may be gone, but he'll never leave "
                    "our hearts")
        print_pause("everyone leaves and you head back to your house")
        print_pause("you go to sleep and try to forget what you did")
        print_pause("at the end of the day, this is what he wanted")
        print_pause("I just wish people realize this")
        print_pause("in the middle of the night")
        print_pause("you wake up to banging on the door")
        print_pause("soldier: COME OUT COME OUT")
        print_pause("you're confused as to why they're here in the "
                    "middle of the night")
        print_pause("you open the door, and they quickly grab you")
        print_pause("soldier: you're under arrest for the murder of "
                    "our fellow brother")
        print_pause("the chief approaches you")
        print_pause("chief: I knew my suspicions of you were true")
        print_pause("you can't believe they figured it out")
        print_pause("but you still try to act normal")
        print_pause("you tell them what's the meaning of this")
        print_pause("chief: quit acting like you're innocent")
        print_pause("chief: The whole time I was thinking why you "
                    "would decline such a big offer")
        print_pause("chief: then it hit me, it's the guilt of "
                    "murdering a soldier is what caused you to "
                    "decline it")
        print_pause("chief: but I was still thinking maybe I'm "
                    "being irrational")
        print_pause("chief: which is why I had to be sure by doing "
                    "a size analysis of your sword and the cut of "
                    "the body")
        print_pause("chief: it was an exact match, I couldn't "
                    "believe one of my prodigies would do such a "
                    "thing")
        print_pause("chief: but this is the right thing, you are "
                    "under arrest")
        print_pause("chief: and is sentenced to life in prison")
        print_pause("chief: from this day, you're no longer "
                    "considered a Shinra soldier")
        restart_game()


def town_2():
    print_pause("you feel the town shaking as if an earthquake is "
                "occuring")
    print_pause("you hear screams within the walls")
    print_pause("numerous people yelling 'help!!!'")
    print_pause("so many body parts scattered")
    print_pause("you realize this is the town the cyclops is "
                "terrorizing")
    town_2_question()


def town_2_question():
    response = input("what do you do?\n"
                     "1. go to cosmo canyon\n"
                     "2. go to midgar\n")
    if(response in "1"):
        if("fire" in items):
            if("cyclops eye" in items):
                print_pause("you enter cosmo canyon")
                cosmo_canyon()
            else:
                print_pause("with the cast of fire")
                print_pause("you burn the big tree")
                print_pause("after it burning to ash")
                print_pause("you enter cosmo canyon")
                print_pause("prepared to take down this beast")
                cosmo_canyon()
        else:
            print_pause("the entrance is blocked by a big tree")
            print_pause("you try using your sword to cut it open")
            print_pause("unforunately, it was ineffective")
            print_pause("you need the cast of fire to burn it down")
            print_pause("it can be found in the rocket town item shop")
            town_2_question()
    elif(response in "2"):
        midgar_version_2()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        town_2_question()


def cosmo_canyon():
    if("cyclops eye" in items):
        print_pause("the whole town cheers for you")
        print_pause("it's currently working on rebuilding the town")
        print_pause("although the people are happy for shinra to "
                    "take care of this")
        print_pause("there are some people who are angry that they "
                    "didn't come sooner")
        print_pause("if they had come sooner, there family members "
                    "would've lived")
        town_2_question()
    else:
        print_pause("countless bodies everywhere")
        print_pause("screaming children and adults leaving the town")
        print_pause("buildings are destroyed")
        print_pause("up ahead you see the cyclops")
        print_pause("it picks up someone and directs him into his "
                    "mouth chewing him to death")
        print_pause("you can't believe what you just witnessed")
        print_pause("you approach it quickly")
        print_pause("and get into fighting position")
        cosmo_canyon_monster()


def cosmo_canyon_monster():
    if("master sword" in items):
        print_pause("you try to get it's attention")
        print_pause("it drops someone out of its hands")
        print_pause("while roaring, it runs towards you")
        print_pause("you bust out the new sword")
        print_pause("you perform a special move")
        print_pause("that makes you travel super fast")
        print_pause("you go through random direction")
        print_pause("slicing through various body parts")
        print_pause("the cyclops is screaming in pain")
        print_pause("until you do one final blow")
        print_pause("which is you launch up in the air aiming your"
                    " sword downwards")
        print_pause("piercing its skull")
        print_pause("the whole town is so relieved to know the "
                    "monster is vanquished")
        print_pause("it evaporates except for one thing")
        print_pause("acquired cyclops eye")
        print_pause("now you report your task completion")
        print_pause("back at shinra HQ")
        items.append("cyclops eye")
        print_pause("inventory updated")
        quest.remove("main quest: go to cosmo canyon")
        quest.remove("main quest: kill cyclops")
        quest.append("main quest: report back to shinra")
        print_pause("quest log updated")
        town_2_question()
    else:
        print_pause("you try to get it's attention")
        print_pause("it drops someone out of its hands")
        print_pause("while roaring, it runs towards you")
        print_pause("you bust out your sword")
        print_pause("you run towards it dodging it's first attack")
        print_pause("you slice it's legs")
        print_pause("but the swords seems ineffective")
        print_pause("you try hitting it's legs as hard as you can")
        print_pause("unfortunately, the sword breaks")
        print_pause("you are shocked at what happaned")
        print_pause("so shocked, you lose your focus")
        print_pause("which gave the cyclops an opportunity to grab "
                    "you and chew you to death")
        print_pause("your current weapon won't work with this monster")
        print_pause("you must wield the master sword to vanquish it")
        print_pause("it can be obtained in the shinra item shop")
        quest.append("main quest: buy master sword from shinra item shop")
        print_pause("quest log updated")
        town_2_question()


def korok_forest():
    print_pause("you are currently in korok forest")
    print_pause("there isn't alot of sunlight")
    print_pause("due to the amount of trees")
    print_pause("while it may be dark, there is a light up ahead")
    korok_forest_question()


def korok_forest_question():
    response = input("what do you do?\n"
                     "1. go to the light\n"
                     "2. back to midgar\n")
    if(response in "1"):
        korok_forest_2()
    elif(response in "2"):
        midgar_version_2()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        korok_forest_question()


def korok_forest_2():
    print_pause("you walk towards the light")
    korok_forest_2_question()


def korok_forest_2_question():
    if("hyrule herb" in items):
        print_pause("there are a countless number of trees")
        print_pause("you see a trail of footsteps that lead to a tunnel")
        response = input("what do you do?\n"
                         "1. investigate tunnel\n"
                         "2. back to forest\n")
        if(response in "1"):
            print_pause("you enter the tunnel")
            korok_forest_tunnel()
        elif(response in "2"):
            korok_forest()
        else:
            print_pause("I don't understand,\n"
                        "please type the number next to the choice\n"
                        "for example, type 1 for choice 1\n"
                        "type 2 for choice 2, etc...")
            korok_forest_2_question()
    elif("fire" in items):
        print_pause("there are a countless number of trees")
        print_pause("you see a trail of footsteps that lead to a tunnel")
        response = input("what do you do?\n"
                         "1. investigate tunnel\n"
                         "2. back to forest\n")
        if(response in "1"):
            print_pause("you enter the tunnel")
            korok_forest_tunnel()
        elif(response in "2"):
            korok_forest()
        else:
            print_pause("I don't understand,\n"
                        "please type the number next to the choice\n"
                        "for example, type 1 for choice 1\n"
                        "type 2 for choice 2, etc...")
            korok_forest_2_question()
    else:
        print_pause("there are a countless number of trees")
        print_pause("you see something grown by the tree")
        print_pause("you see a trail of footsteps that lead to a tunnel")
        response = input("what do you do?\n"
                         "1. grab the item\n"
                         "2. investigate tunnel\n"
                         "3. back to forest\n")
        if(response in "1"):
            print_pause("this must be what the clerk wanted")
            print_pause("acquired hyrule herb")
            items.append("hyrule herb")
            print_pause("inventory updated")
            quest.remove("main quest: get hyrule herb in korok forest")
            quest.append("main quest: bring hyrule herb back "
                         "to rocket town item shop clerk")
            print_pause("quest log updated")
            korok_forest_2_question()
        elif(response in "2"):
            print_pause("you enter the tunnel")
            korok_forest_tunnel()
        elif(response in "3"):
            korok_forest()
        else:
            print_pause("I don't understand,\n"
                        "please type the number next to the choice\n"
                        "for example, type 1 for choice 1\n"
                        "type 2 for choice 2, etc...")
            korok_forest_2_question()


def korok_forest_tunnel():
    print_pause("there seems to be alot of bones")
    if("myrthil shard" in items):
        response = input("what do you do?\n"
                         "1. back to forest\n"
                         "2. investigate more\n")
        if(response in "1"):
            korok_forest_2_question()
        elif(response in "2"):
            print_pause("you go deeper in the tunnel")
            korok_forest_monster_gone()
        else:
            print_pause("I don't understand,\n"
                        "please type the number next to the choice\n"
                        "for example, type 1 for choice 1\n"
                        "type 2 for choice 2, etc...")
            korok_forest_tunnel()
    else:
        response = input("what do you do?\n"
                         "1. go to forest\n"
                         "2. investigate more\n")
        if(response in "1"):
            korok_forest_2_question()
        elif(response in "2"):
            print_pause("you go deeper in the tunnel")
            korok_forest_monster()
        else:
            print_pause("I don't understand,\n"
                        "please type the number next to the choice\n"
                        "for example, type 1 for choice 1\n"
                        "type 2 for choice 2, etc...")
            korok_forest_tunnel()


def korok_forest_monster_gone():
    print_pause("there's nothing here")
    korok_forest_tunnel()


def korok_forest_monster():
    print_pause("you see a minotaur eating a man")
    print_pause("you are spotted")
    print_pause("it runs towards you, with its horns out")
    response = input("what do you do?\n"
                     "1. attack\n")
    if(response in "1"):
        print_pause("you evade the attack")
        print_pause("you quickly bust out your sword")
        print_pause("and cut off its legs")
        print_pause("then go cut off its head")
        print_pause("the monster is vanquished, and evaporates "
                    "leaving something")
        print_pause("acquired myrthil shard")
        print_pause("level up")
        items.append("myrthil shard")
        print_pause("inventory updated")
        level.append("LV3")
        korok_forest_tunnel()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        korok_forest_monster()


def penny_family():
    print_pause("they all look like they've seen a ghost")
    penny_family_response()


def penny_family_response():
    response = input("1. what's the matter?\n")
    if(response in "1"):
        print_pause("family: our town is being attacked by this monster")
        print_pause("family: how careless of shinra for not guarding"
                    " it properly,")
        print_pause("family: it's as if paying taxes wasn't beneficial")
        print_pause("family: and on top of that, we have seperated "
                    "from our daughter, and we can't seem to find her")
        if("side quest: find penny family" in quest):
            print_pause("this must be the family that penny was "
                        "trying to find")
            response = input("1. was her name penny?\n")
            if(response in "1"):
                quest.remove("side quest: find penny family")
                print_pause("the families eyes lit up like christmas"
                            " lights")
                print_pause("family: YES HOW DO YOU KNOW!!!")
                print_pause("you show them her necklace")
                print_pause("family: dear lord that's her necklace")
                print_pause("family: can you bring us to her?")
                print_pause("you accept there request")
                quest.append("side quest: bring penny family back")
                print_pause("quest log updated")
                rocket_town_2_question()
            else:
                print_pause("I don't understand,\n"
                            "please type the number next to the choice\n"
                            "for example, type 1 for choice 1\n"
                            "type 2 for choice 2, etc...")
                penny_family_response()
        else:
            response = input("1. where is your town located?\n")
            if(response in "1"):
                print_pause("family: the town's called cosmo canyon")
                print_pause("family: it's the next town after this one")
                print_pause("family: I see some survivors of that attack")
                print_pause("family: I hope the remaining people "
                            "survived wherever they are")
                print_pause("family: AND OUR BELOVED DAUGHTER")
                rocket_town_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        penny_family_response()


def rocket_town_item_shop():
    print_pause("you are currently in an item shop")
    print_pause("you see a clerk")
    response = input("what do you do next?\n"
                     "1. go to clerk\n"
                     "2. back to rocket town\n")
    if(response in "1"):
        print_pause("you approach the clerk")
        rocket_town_clerk()
    elif(response in "2"):
        if("diamond" in items):
            rocket_town_2_question()
        elif("side quest: bring penny family back" in quest):
            rocket_town_2_question()
        else:
            rocket_town()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        rocket_town_item_shop()


def rocket_town_clerk():
    response = input("clerk: what can I help you with?\n"
                     "1. here to buy\n"
                     "2. any information on the cyclops attack\n"
                     "3. Nothing thank you\n")
    if(response in "1"):
        if("fire" in items):
            print_pause("I gave you everything I have to sell")
            rocket_town_clerk()
        else:
            rocket_town_clerk_items()
    elif(response in "2"):
        rocket_town_clerk_speak()
    elif(response in "3"):
        print_pause("you can collect materials by defeating monsters")
        print_pause("and level up as well")
        print_pause("I heard a report of one in a cave")
        print_pause("and another in some kind of forest")
        rocket_town_item_shop()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        rocket_town_clerk()


def rocket_town_clerk_speak():
    print_pause("you know it's in cosmo canyon, but want to know where it is")
    print_pause("clerk: ahhh yes")
    print_pause("clerk: we have many survivors here of the cyclops "
                "attack in cosmo canyon")
    print_pause("clerk: it's located at the next town after us you "
                "can't miss it")
    print_pause("clerk: shinra better hurry")
    print_pause("clerk: the cyclops is still there terrorizing the town")
    rocket_town_clerk()


def rocket_town_clerk_items():
    print_pause("here's what I have")
    print_pause("fire")
    rocket_town_clerk_items_question()


def rocket_town_clerk_items_question():
    response = input("what do you do?\n"
                     "1. buy fire\n"
                     "2. never mind\n")
    if(response in "1"):
        fire()
    elif(response in "2"):
        rocket_town_clerk()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        rocket_town_clerk_item_question()


def fire():
    if("hyrule herb" in items):
        items.remove("hyrule herb")
        quest.remove("main quest: bring hyrule herb back "
                     "to rocket town item shop clerk")
        print_pause("clerk: splendid!!!")
        print_pause("clerk: I had zero faith you would come back alive")
        print_pause("clerk: as promised")
        print_pause("acquired fire")
        items.append("fire")
        print_pause("clerk: time to make my famous pie")
        print_pause("inventory updated")
        print_pause("quest log updated")
        quest.append("main quest: go to cosmo canyon")
        rocket_town_clerk()
    else:
        if("main quest: get hyrule herb in korok forest" in quest):
            print_pause("clerk: if you can get me a hyrule herb, "
                        "I'll give you the spell fire")
            rocket_town_clerk()
        else:
            quest.remove("main quest: buy fire from rocket town item clerk")
            print_pause("you look through your pockets for money")
            print_pause("you just remembered you used the last of "
                        "it to get here")
            print_pause("you explain to the clerk the situation")
            print_pause("clerk: I see, no worries you can still have it")
            print_pause("clerk: through a trade")
            print_pause("clerk: im currently working on making"
                        " something epic")
            print_pause("clerk: but it requires a hyrule herb, "
                        "which is found in korok forest")
            print_pause("clerk: unfortunately it's too dangerous "
                        "for me to go there")
            print_pause("clerk: you look like a man who can handle that")
            print_pause("clerk: if you can get me a hyrule herb, "
                        "I'll give you the spell fire")
            print_pause("if you go out to midgar you can't miss it")
            quest.append("main quest: get hyrule herb in korok forest")
            print_pause("quest log updated")
            rocket_town_clerk()


def cave():
    print_pause("you are inside a cave")
    print_pause("looks dark and depressing")
    print_pause("you see a door")
    cave_question()


def cave_question():
    response = input("what do you do next?\n"
                     "1. enter door\n"
                     "2. back to midgar\n")
    if(response in "1"):
        if("carry him back to base" in choice):
            cave_door_choice_one()
        elif("slay the monster for him" in choice):
            cave_door_choice_two()
        elif("end him, he'll die with honor" in choice):
            cave_door_choice_three()
        else:
            cave_door()
    elif(response in "2"):
        # if you have korok forest quest, midgar function will change
        if("main quest: get hyrule herb in korok forest" in quest):
            midgar_version_2()
        elif("main quest: bring hyrule herb back "
             "to rocket town item shop clerk" in quest):
            midgar_version_2()
        elif("fire" in items):
            midgar_version_2()
        else:
            midgar()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        cave_question()


def cave_door():
    print_pause("you enter, and you see a wounded soldier on the ground")
    print_pause("he's wearing a shinra uniform")
    print_pause("you approach him")
    cave_soldier_question()


def cave_door_choice_one():
    if("gold" in items):
        if("titanium" in items):
            print_pause("the room is empty")
            print_pause("the door is quiet")
            cave_door2_question()
        else:
            print_pause("you hear noise coming through the door "
                        "in front of you")
            print_pause("it's shaking like crazy")
            cave_door2_question()
    else:
        print_pause("it seems the soldier dropped something")
        print_pause("acquired gold")
        items.append("gold")
        print_pause("you hear noise coming through the door in front of you")
        print_pause("it's shaking like crazy")
        print_pause("inventory updated")
        cave_door2_question()


def cave_door_choice_two():
    if("gold" in items):
        print_pause("the soldier is no longer there")
        print_pause("you wonder where he is now?")
        cave_question()
    else:
        quest.remove("main quest: inform soldier that monster has "
                     "been vanquished")
        print_pause("soldier: YOU'RE BACK!!!")
        print_pause("soldier:I can't believe it")
        print_pause("soldier: now I can go back with peace of mind")
        print_pause("soldier: you didn't have to do this so I thank you")
        print_pause("soldier: a deal's a deal")
        print_pause("soldier: here's your reward")
        print_pause("acquired gold")
        items.append("gold")
        print_pause("inventory updated")
        print_pause("quest log updated")
        cave_question()


def cave_door_choice_three():
    if("gold" in items):
        if("titanium" in items):
            print_pause("the whole room smells of death")
            print_pause("the soldiers body is already rotting away "
                        "covered with flies")
            print_pause("the door is quiet")
            cave_door2_question()
        else:
            print_pause("the whole room smells of death")
            print_pause("the soldiers body is already rotting away "
                        "covered with flies")
            print_pause("you hear noise coming through the door in "
                        "front of you")
            print_pause("it's shaking like crazy")
            cave_door2_question()
    else:
        print_pause("it seems the soldier dropped something")
        print_pause("acquired gold")
        items.append("gold")
        print_pause("you hear noise coming through the door in front of you")
        print_pause("it's shaking like crazy")
        print_pause("inventory updated")
        cave_door2_question()


def cave_door2_question():
    response = input("what do you do next?\n"
                     "1. enter door\n"
                     "2. go back to cave\n")
    if(response in "1"):
        if("titanium" in items):
            cave_monster_dead()
        else:
            cave_monster()
    elif(response in "2"):
        cave()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        cave_door2_question()


def cave_monster_dead():
    print_pause("the room is empty")
    cave_door2_question()


def cave_monster():
    print_pause("as soon as you enter")
    print_pause("a gigantic scorpion pops out of the floor")
    print_pause("and tries to poisen you")
    print_pause("luckily you were able to react quickly and evade "
                "the attack")
    print_pause("you get into fighting position")
    cave_monster_question()


def cave_monster_question():
    response = input("what do you do?\n"
                     "1. attack\n")
    if(response in "1"):
        print_pause("scorpion goes for another attack")
        print_pause("you roll into the enemy dodging the attack")
        print_pause("while near it, you bust out your sword and stab it")
        print_pause("the scorpion is down, and the whole body evaporates")
        print_pause("leaving behind something")
        print_pause("acquired titanium")
        items.append("titanium")
        print_pause("inventory updated")
        print_pause("level up")
        level.append("LV2")
        if("carry him back to base" in choice):
            if("main quest: investigate the cave" in quest):
                quest.remove("main quest: investigate the cave")
                quest.remove("main quest: slay the cave monster")
                quest.append("main quest: go to town 1")
                print_pause("quest log updated")
                cave_question()
            else:
                quest.remove("main quest: slay the cave monster")
                quest.append("main quest: go to town 1")
                print_pause("quest log updated")
                cave_question()
        elif("end him, he'll die with honor" in choice):
            if("main quest: investigate the cave" in quest):
                quest.remove("main quest: investigate the cave")
                quest.remove("main quest: slay the cave monster")
                quest.append("main quest: go to town 1")
                print_pause("quest log updated")
                cave_question()
            else:
                quest.remove("main quest: slay the cave monster")
                quest.append("main quest: go to town 1")
                print_pause("quest log updated")
                cave_question()
        else:
            if("main quest: investigate the cave" in quest):
                quest.remove("main quest: investigate the cave")
                quest.append("main quest: go to town 1")
                print_pause("quest log updated")
                cave_question()
            else:
                quest.append("main quest: go to town 1")
                print_pause("quest log updated")
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        cave_monster_question()


def cave_soldier_question():
    response = input("1. how did you get like this?\n")
    if(response in "1"):
        print_pause("soldier: was tasked to take out a monster ")
        print_pause("soldier: I thought I was ready but he's too strong")
        print_pause("soldier: luckily I was able to run away before "
                    "he did anything drastic")
        print_pause("soldier: Now I lay here thinking whether I "
                    "should leave with the task failed or die with honor")
        print_pause("soldier: but how could I leave, it would be an "
                    "embarrassment to come back as a failure")
        print_pause("although the soldier thought he left before it "
                    "was too late")
        print_pause("he was wrong because the soldier is losing blood")

        response = input("once you make your decision, you can't undo it\n"
                         "choose wisely\n"
                         "1. carry him back to base\n"
                         "2. slay the monster for him\n"
                         "3. end him, he'll die with honor\n")
        if(response in "1"):
            cave_choice_one()
        elif(response in "2"):
            cave_choice_two()
        elif(response in "3"):
            cave_choice_three()
        else:
            print_pause("I don't understand,\n"
                        "please type the number next to the choice\n"
                        "for example, type 1 for choice 1\n"
                        "type 2 for choice 2, etc...")
            cave_soldier_question()
    else:
        print_pause("I don't understand,\n"
                    "please type the number next to the choice\n"
                    "for example, type 1 for choice 1\n"
                    "type 2 for choice 2, etc...")
        cave_soldier_question()


def cave_choice_one():
    print_pause("you grab him and bring him back to base quick")
    print_pause("soldier: hey what are you doing?")
    print_pause("soldier: I made up my mind, going back as a failure")
    print_pause("soldier: is worst than dying with honor")
    print_pause("you understand, but you think his family may be"
                " devestated, he'll thank you in the future")
    choice.append("carry him back to base")
    quest.append("main quest: slay the cave monster")
    print_pause("quest log updated")
    cave()


def cave_choice_two():
    print_pause("soldier: that's a great idea")
    print_pause("soldier: for all they know, I slayed it")
    print_pause("soldier: I appreciate it brother")
    print_pause("soldier: so much that I'll reward you for doing so")
    print_pause("good luck")
    choice.append("slay the monster for him")
    quest.append("main quest: inform soldier that monster has "
                 "been vanquished")
    print_pause("quest log updated")
    cave_monster()


def cave_choice_three():
    print_pause("you still stay to rethink what your about to do")
    print_pause("although this may seem immoral, his expression shows")
    print_pause("this is what he wants")
    print_pause("as a soldier, you understand that he'd rather do this")
    print_pause("coming back to be looked down upon and shamed")
    print_pause("for the rest of his life seems worse than dying with honor")
    print_pause("you take out your sword and give him a look of respect")
    print_pause("soldier: Thank you")
    print_pause("you can't believe what you did, you commited murder,"
                " but you did the right thing in his eyes")
    choice.append("end him, he'll die with honor")
    quest.append("main quest: slay the cave monster")
    print_pause("something falls out of his pocket")
    print_pause("acquired gold")
    items.append("gold")
    print_pause("inventory updated")
    print_pause("quest log updated")
    cave()


play_game()
