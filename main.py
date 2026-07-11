import cv2

from hand_detector import HandDetector
from finger_counter import countFingers


cap = cv2.VideoCapture(0)

detector = HandDetector()

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    hands = detector.getHands()

    left = 0
    right = 0

    for hand in hands:

        fingers = countFingers(hand)

        if hand["type"] == "Left":
            left = fingers
        else:
            right = fingers

    total = left + right

    cv2.rectangle(img, (10, 10), (420, 90), (0, 0, 0), -1)

    cv2.putText(
        img,
        f"Left : {left}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        img,
        f"Right : {right}",
        (150, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        img,
        f"Total : {total}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 0),
        2
    )

    cv2.imshow("Gesture Calculator", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()