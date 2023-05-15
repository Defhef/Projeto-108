import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for tip in finger_tips:
            x,y = int(Im_list[tip].x*w), int(Im_list[tip].y*h)
            cv2.circle(img, (x,y), 15, (255,0,0), cv2.FILLIED)

        for hand_landmark in results.multi_hand_landmarks:
            #acessando os pontos de referência pela sua posição
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             #O código vai aqui  
            if Im_list[tip].x < Im_list[tip - 3].x:
                cv2.circle(img, (x,y), 15, (0,255,0), cv2.FILLIED)
            
            else:
                finger_fold_status.append(False)

            if all(finger_fold_status):
                if Im_list[thumb_tip].y < Im_list[thumb_tip-1].y < Im_list[thumb_tip-2].y:
                    print("CURTI")
                    cv2.putText(img, "CURTI", (20,30), cv2.FONT_HERSEY_SIMPLEX,1,(0,255,0),3)
            
            if all(finger_fold_status):
                if Im_list[thumb_tip].y < Im_list[thumb_tip-1].y < Im_list[thumb_tip-2].y:
                    print(" NAO CURTI")
                    cv2.putText(img, "NAO CURTI", (20,30), cv2.FONT_HERSEY_SIMPLEX,1,(0,255,0),3)

            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("detector de maos", img)
    cv2.waitKey(1)