# Is You Is or Is You Ain't, My Baby? (A "Sinners" 🩸 Horror Quiz Game)

def main():
    
    # Sinners Opening (Introduction)
    print("In the horror film 'Sinners' dir. by Ryan Coogler, rootworker Annie states the following: \n") 
    print("'There are legends of people born with the gift of making music so true, it can pierce the veil between life and death; conjuring spirits from the past... and the future. In ancient Ireland, they were called Filí. In Choctaw land, they called them Fire Keepers. And in West Africa, they were called Griots. This gift can bring healing to their communities. But it also, attracts evil [...] How haints work: they switch places with the soul of a man. But vampires are different; maybe the worst kind [of evil creatures]. The soul gets stuck in the body. Can't rejoin the ancestors. Cursed to live here with all this hate. Can't even feel the warmth of a sunrise.' \n")
    print("Play the quiz game below to determine if your loved one has become a fanatic hive-minded member of The Vampire Remmick's undead cult. Answer 'Yes' or 'No' to each of the questions. \n")

    # The sinners_quest (short for questionnaire) is a list that stores the user's responses to the questions.
    sinners_quest = [
        "1) After arriving at the juke joint together, did they ever disappear for a lengthy period of time during the party?",
        "2) Do they speak differently, often referring to themselves as 'we' while conversing with others?",
        "3) Is their new favorite song suddenly 'Pick Poor Robin Clean'?",
        "4) Have you noticed any red blood stains on their clothing?",
        "5) Are there visible bite marks on their skin?",
        "6) Do their eyes glow like a cat's or look as pale, cloudy, and opaque as a moonstone gem?",
        "7) Do they drool uncontrollably?",
        "8) Do their teeth look as sharp as a shark's?",
        "9) Do they suddenly sound like a pacifist, preaching ideals such as 'Being kind to one another!'?",
        "10) Have they recently suffered from a fatal injury, but heal quickly and try to act like nothing's amiss?",
        "11) Do they witness the death of someone else in front of them but appear indifferent or unbothered?",
        "12) Has calling you 'Baby' in a seductive tone quickly become their new favorite pet name?",
        "13) Can they suddenly sense your emotions as if they're an empath?",
        "14) Do they have the ability to do something that they normally wouldn't know how to do (e.g. perform an Irish jig)?",
        "15) Despite having been in and out all day, do they suddenly need an invitation in order to re-enter the juke joint?"
    ]

    responses = []

    binary = ["yes", "no"]

    for question in sinners_quest:
        answer = input(f"{question}: ").strip().lower()
            
        while answer not in binary:
            answer = input(f"Please enter a valid response (Yes/No): ").strip().lower()

        responses.append(answer)

    # Counts the number "yes" and "no" responses from the user.
    count = responses.count("yes")

    if count > len(sinners_quest) / 2:
        vamp_id(count)
    else:
        not_vamp_id(count) 
    
def vamp_id(score):
    print("\n")
    print(f"Invite to the Cookout Declined (High Vamp Score): {score} / 15.")
    print("Warning: Don't let them in! If you do, you're dead. They're a vampire.")
    # Warning message to proceed with caution.

def not_vamp_id(score):
    print("\n")
    print(f"Invite to the Cookout (Low Vamp Score): {score} / 15.")
    print("You gon' be alright. Let them in! They're family.")
    # Reassuring message to calm the user.

if __name__ == "__main__":
    main()
