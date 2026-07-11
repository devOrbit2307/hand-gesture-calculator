import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.draw = mp.solutions.drawing_utils
        self.results = None

    def findHands(self, img):

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb)

        if self.results.multi_hand_landmarks:

            for hand in self.results.multi_hand_landmarks:

                self.draw.draw_landmarks(
                    img,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

        return img

    def getHands(self):

        hands = []

        if self.results and self.results.multi_hand_landmarks:

            for idx, hand in enumerate(self.results.multi_hand_landmarks):

                lmList = []

                hType = self.results.multi_handedness[idx].classification[0].label

                for id, lm in enumerate(hand.landmark):

                    lmList.append({
                        "id": id,
                        "x": lm.x,
                        "y": lm.y
                    })

                hands.append({
                    "type": hType,
                    "lmList": lmList
                })

        return hands