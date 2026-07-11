tipIds = [4, 8, 12, 16, 20]


def countFingers(hand):

    lm = hand["lmList"]
    handType = hand["type"]

    fingers = 0

    # Thumb
    if handType == "Right":

        if lm[4]["x"] < lm[3]["x"]:
            fingers += 1

    else:

        if lm[4]["x"] > lm[3]["x"]:
            fingers += 1

    # Index
    if lm[8]["y"] < lm[6]["y"]:
        fingers += 1

    # Middle
    if lm[12]["y"] < lm[10]["y"]:
        fingers += 1

    # Ring
    if lm[16]["y"] < lm[14]["y"]:
        fingers += 1

    # Pinky
    if lm[20]["y"] < lm[18]["y"]:
        fingers += 1

    return fingers