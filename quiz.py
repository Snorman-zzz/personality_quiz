def take_quiz():
    print("Welcome to my quiz!")
    print("How to play:")
    print("Answer the questions to find out what kind of programmer you are.")
    rules = "I will ask multiple choice questions. After the question, press " \
            + "the key that corresponds with the best answer for you.\n" \
            + "Any invalid answer is assumed to be A. Your answer can be "\
            + "upper or lower case."
    print(rules)
    input("Press enter when ready to start")
    print()

    answers = []
    question1 = "1) How do you usualy behave at a party?\n" \
                + "\tA - Get blackout drunk, no matter the occasion.\n" \
                + "\tB - Survey the room. Who is here? What kinds of groups have formed?\n" \
                + "\tC - Figure out how to leave as early as possible.\n" \
                + "\tD - Show up early to help decorate.\n"
    answers.append(input(question1).lower())
    print()
    question2 = "2) What is your fashion sense?\n" \
                + "\tA - I only wear underwear because I never leave the house.\n" \
                + "\tB - I follow fashion trends and try to get ahead of the curve.\n" \
                + "\tC - I wear whatever is functional that day.\n" \
                + "\tD - I like to make a splash, anything to turn heads!\n"
    answers.append(input(question2).lower())
    print()
    question3 = "3) What do you like to eat for dinner?\n" \
                + "\tA - Microwave dinners.\n" \
                + "\tB - An optimally balanced meal in taste and nutrition.\n" \
                + "\tC - A recipe followed exactly.\n" \
                + "\tD - Doesn't matter as long as it's presented well.\n"
    answers.append(input(question3).lower())
    print()
    question4 = "4) What is your favorite type of art?\n" \
                + "\tA - Memes\n" \
                + "\tB - Creative Infographics\n" \
                + "\tC - Sculpture\n" \
                + "\tD - Paintings\n"
    answers.append(input(question4).lower())
    print()
    question5 = "5) What about your home are you most proud of?\n" \
                + "\tA - I have none\n" \
                + "\tB - It's a smarthome that tracks everything\n" \
                + "\tC - It's sturdiness\n" \
                + "\tD - The interior decorations\n"
    answers.append(input(question5).lower())

    ### Process results
    sum = 0
    for response in answers:
        if response.strip() == "a":
            continue
        elif response.strip() == "b":
            sum += 1
        elif response.strip() == "c":
            sum += 2
        elif response.strip() == "d":
            sum += 3
        else:
            continue

    result = "Thanks for taking the quiz!\nBased on your answers you should be a "
    if sum == 0:
        result += "...\nCriminal hacker!?! Uh oh, think of turning your interests "\
                  + "to more productive persuits!"
    elif 0 < sum <= 5:
        result += "Data Scientist!"
    elif 5 < sum <= 10:
        result += "Back-End Engineer!"
    elif 10 < sum <= 15:
        result += "Front-End Engineer!"
    else:
        result = "Something went wrong! Please play again."
    return result

print(take_quiz())
