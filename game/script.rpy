# Defining characters
define homer = Character("Homer", color="#F8347C")
define crewmen = Character("Odysseus' crewmen", color="#FFA630")
define crewman_1 = Character("Crewman 1", color="#B5FD39")
define crewman_2 = Character("Crewman 2", color="#B5FD39")
define crewman_3 = Character("Crewman 3", color="#B5FD39")
define odysseus = Character("Odysseus", color="#4DA1A9")
define polyphemus = Character("Polyphemus", color="#FF0000")
define scylla_and_charybdis = Character("Scylla and Charybdis", color="#FF0000")
define helios = Character("Helios", color="#A5B5BF")
define calypso = Character("Calypso", color="#FF0000")

# Defining variables for alternative paths
default bag_of_winds = False
default bag_of_endless_bread = False

# Defining variables for scene selection purposes
default last_scene = "start"
default scene_names = [
    "start",
    "lotus_flowers",
    "ate_lotus_flowers",
    "polyphemus",
    "blinded_polyphemus",
    "aeolus",
    "circe",
    "underworld",
    "sirens_choice",
    "sirens_correct",
    "monsters",
    "helios",
    "ogygia",
    "conclusion",
    "that_s_not_quite_how_it_went",
    "goodbye"
]

# Actual game

label start:

    $ last_scene = "start"

    scene bg ithaca

    show homer at left with dissolve

    homer "A long time ago, in the land of Greece, there lived a man named Odysseus."

    scene bg trojan war
    
    show homer at left with dissolve
    
    homer "When the Trojan War broke out, Odysseus left his home in Ithaca to go fight in Troy."
    
    homer "After the Trojan War ended, Odysseus hops up in his ship, together with his crewmen, in order to go back to Ithaca."
    
    homer "... but his journey back from the war took a little bit longer than expected..."

    hide homer with dissolve

    menu:

        "Wanna know how it went? :D"

        "HECK YEAH!":

            jump lotus_flowers

        "I'd rather not, I prefer maths...":

            jump goodbye

label lotus_flowers:

    $ last_scene = "lotus_flowers"

    scene bg djerba

    show homer at left with dissolve

    homer "\"10 days after leaving Ismarus, Odysseus and his men stop at Djerba, land of the \'Lotus Eaters\'\""

    hide homer at left with dissolve

    show odysseus at right with dissolve
    
    odysseus "Gentlemen, we'll stay here in Djerba for a very brief period, just to get some rest."

    hide odysseus at right with dissolve

    show crewmen at right with dissolve

    crewmen "Chief, we are hungry! Is there something to eat?"

    hide crewmen at right with dissolve

    show odysseus at right with dissolve

    odysseus "I don't know, let's find something to eat in the island!"

    hide odysseus

    show lotus flower at topleft

    show crewmen at right with dissolve

    menu:
        
        crewmen "Hey! Look! We found these lotus flowers! Shall we eat them?"

        "Uhm, better safe then sorry, let's find something more familiar...":

            jump that_s_not_quite_how_it_went

        "Yes, we are starving!":

            jump ate_lotus_flowers

label ate_lotus_flowers:

    $ last_scene = "ate_lotus_flowers"
    
    scene bg ate lotus

    show crewmen stunned at right with dissolve

    crewman_1 "GASP! what was there in those flowers?"

    crewman_2 "My head is spinnin' like crazy!"
    
    crewman_3 "I don't feel really well..."

    hide crewmen stunned

    show odysseus at right with dissolve

    odysseus "What is going on?!?"

    hide odysseus

    show crewmen stunned at right with dissolve

    crewmen "We ate the lotus flowers and now we are all sick..."

    hide crewmen
    
    show odysseus at right with dissolve

    odysseus "What?!? Really?!? Well, let's go back to our ship then, fast!"

    jump polyphemus


label polyphemus:

    $ last_scene = "polyphemus"

    scene bg cave of polyphemus

    show homer at left with dissolve

    homer "After recovering from the lotus flowers' intoxication, Odysseus and his men reach the land of the Cyclopes."
    
    homer "Here lives Polyphemus"

    homer "The travelers assume Polyphemus would understand them and be gentle and welcoming with them"

    homer "But..."

    hide homer

    show polyphemus at left with dissolve

    polyphemus "WHO ARE YOU? WHAT DO YOU WANT?!?"
    
    polyphemus "YOU ENTERED MY CAVE WITHOUT MY PERMISSION, NOW I WILL EAT YOU ALIVE!"

    hide polyphemus

    show homer at left with dissolve

    homer "Polyphemus actually proceeds to eat four crewmen alive"
    
    homer "Odysseus is saddened and angry about this loss, so he decides to hide, in order to organize his thoughts..."

    hide homer

    show odysseus at right with dissolve

    menu:

        odysseus "Uhm... what do I do?"

        "Make Polyphemus drunk and kill him, cutting his head with a giant sharp rock":

            jump that_s_not_quite_how_it_went

        "Make Polyphemus drunk and blind him, sticking a burning stake into his eye while he's asleep":

            jump blinded_polyphemus
        
        "Take the loss. I'll never be able to counter a giant. I can not win.":

            jump aeolus
    

label blinded_polyphemus:

    $ last_scene = "blinded_polyphemus"

    scene bg blinded polyphemus

    hide odysseus

    show homer at left with dissolve

    homer "Odysseus and his men take advantage of the situation and manage to escape"

    hide homer

    show crewmen at right with dissolve

    jump aeolus

label aeolus:

    $ last_scene = "aeolus"

    scene bg land of aeolus

    show homer at left with dissolve

    homer "In Aeolia, Odysseus and the crewmen meet Aeolus, the God of the Winds."

    show antique sack at topleft

    homer "Aeolus is very gentle with the men. He decides to gift the a bag full of wind, which would be useful to steer them towards Ithaca, during their sailing."

    hide antique sack

    scene bg ithaca

    hide homer

    show crewmen at right with dissolve

    crewmen "Chief, sailing is proceeding greatly."
    
    crewmen "Ithaca is now in plain sight, just right in front of us!"

    crewmen "We should arrive there tomorrow morning, at worse!"

    hide crewmen

    show odysseus at right with dissolve
    
    odysseus "That's fantastic news!"
    
    odysseus "Since everything seems smooth, I'll take a quick nap, so as I will be well rested for my return home."

    hide odysseus
    
    scene bg bag of winds

    show homer at left with dissolve
    
    homer "Excited by the prospect of getting back home, the crewmen decide to open the bag gifted to them by Aeolus"

    hide homer 

    jump circe

label circe:

    $ last_scene = "circe"
    
    scene bg circe

    show homer at left with dissolve
    
    homer "Little did the men know!"

    homer "The bag of winds released a windstorm, which actually pushes them far away from Ithaca"

    homer "As a result, they get pushed towards Aeaea, lands of Circe goddess"
    
    homer "In Aeaea, Odysseus meets with Hermes, who is very gentle with the travelers."

    hide homer

    show odysseus at right with dissolve

    odysseus "Crew, go explore the island!"
    
    odysseus "Look for food and a place where to rest, so as we can continue our journey back home well rested"

    hide odysseus

    show homer at left with dissolve
    
    scene bg circe turns men into pigs
    
    homer "Circe is not welcoming of the men in the lands"

    homer "She uses to turn men into pigs, and so it does with Odysseus and his men"

    hide homer

    show odysseus at right with dissolve

    odysseus "What is happening?!?"

    odysseus "There must be an explanation, I'll look for Circe..."

    hide odysseus

    scene bg circe together odysseus

    show homer at left with dissolve

    homer "Odysseus indeed finds Circe"

    homer "They actually end up together, spending an entire year in a relationship in the island"

    homer "Eventually, Circe understands that Odysseus has to go home, so she advises him to what route to take"

    homer "Specifically, she tells him to visit the Underworld..."

    hide homer

    jump underworld

label underworld:

    $ last_scene = "underworld"

    scene bg underworld

    show homer at left with dissolve

    homer "Following the Circe's advice, the men arrive in the Underworld"

    homer "Here Odysseus meets the ghosts of numerous people, including: his mother, Teiresias and Agamemnon"

    jump sirens_choice

    
label sirens_choice:

    $ last_scene = "sirens_choice"

    scene bg sirens

    show homer at left with dissolve

    homer "Next up for the crew, the Sirens!"

    menu:

        homer "What is the peculiarity of the Sirens?"

        "Getting by the Sirens requires at least a woman to be present in the ship":

            jump that_s_not_quite_how_it_went

        "Getting by the Sirens was an impossible task, as their beautiful song drew anyone who heard it in":

            jump sirens_correct


label sirens_correct:

    $ last_scene = "sirens_correct"

    scene bg sirens
        
    hide homer

    show odysseus at right with dissolve 

    odysseus "Gentlemen, Teiresias told me in the underworld what is the deal with the Sirens."

    odysseus "For these reason, you'll tie me to this pole and cover my ears with wax."

    odysseus "This way, I'll be able to conduct you pass the Sirens and we'll be able to continue our navigation"

    odysseus "All clear?"

    hide odysseus

    show crewmen at right with dissolve 

    crewmen "YES, SIR!"

    hide crewmen

    jump monsters

label monsters:

    $ last_scene = "monsters"

    scene bg monsters

    show homer at left with dissolve

    homer "Passing the Sirens was no joke, but what's coming next is totally unexpected..."

    hide homer

    show sc at left with dissolve

    scylla_and_charybdis "You are not allowed to pass through any of the paths of this bifurcation, unless a sacrifice is made"

    scylla_and_charybdis "We want you to sacrifice 6 men of your crew, otherwise, we are going to kill them all."

    jump helios
                

label helios:

    $ last_scene = "helios"

    hide sc

    scene bg helios

    show homer at left with dissolve

    homer "Odysseus is comprehensibly destroyed by his loss"
    
    homer "He regroups with the survivors and stars, once again, to plan their journey towards Ithaca."

    homer "The men manage to arrive to Thrinakia, land of Helios"

    hide homer

    show helios at right with dissolve

    helios "Hi everyone, and welcome in Thrinakia!"

    helios "I am very happy to host you."

    helios "Here you can find food, rest and comfort"

    helios "Just one thing: never, EVER, touch my cattle!"

    hide helios
    
    menu:

        "What does the crew do?"

        "They respect Helios' orders and they avoid eating the cows":

            jump that_s_not_quite_how_it_went
        
        "They end up eating Helios' cattle":

            jump ogygia

label ogygia:

    $ last_scene = "ogygia"

    scene bg ogygia

    show homer at left with dissolve

    homer "Helios' rage is immense"

    homer "Odysseus organizes an escape from Thrinakria, which brings him in Ogygia"

    homer "Here lives Calypso"

    hide homer

    show calypso at right with dissolve

    calypso "Hi Odysseus, I have a proposition for you."

    calypso "Spend some time with me here and I will make you immortal"

    hide calypso

    show odysseus at right with dissolve

    menu:

        "That's a very tempting offer... what should I do?"

        "Accept":

            jump that_s_not_quite_how_it_went

        "Refuse":

            jump conclusion
    
    
label conclusion:

    $ last_scene = "conclusion"

    scene bg ogygia

    show odysseus at right with dissolve

    odysseus "I'm sorry, Calypso."

    odysseus "Thank you for your kind offer, but I want to get back to my wife and my people in Ithaca."

    odysseus "I hope you will understand me."

    hide odysseus

    show calypso at right with dissolve

    calypso "NO, I DO NOT!"

    calypso "TELL YOU WHAT, YOU'LL STILL SPEND TIME HERE!"

    calypso "I'M GONNA KEEP YOU AS A PRISONER HERE, FOREVER!"

    hide calypso

    show homer at left with dissolve

    homer "Calypso will keep Odysseus prisoner for 7 years."

    homer "Eventually, Nausicaa will come in help of the hero and free him."

    scene bg the end

    homer "Odysseus will return back to Ithaca, where, after some trials, he will be able to finally reconcile with his spouse."

    return

label that_s_not_quite_how_it_went:

    scene bg that s
    
    show homer at left with dissolve

    homer "Uhm... I'm sorry... that's not quite how the story went..."

    menu:

        "What do you want to do?"

        "Retry from my last scene":
            
            jump expression last_scene

        "Go study maths...":
            jump goodbye

label goodbye:

    scene bg goodbye

    menu:

        "Would you like to...?"

        "Exit":

            return 
        
        "Play again from the start":

            jump start