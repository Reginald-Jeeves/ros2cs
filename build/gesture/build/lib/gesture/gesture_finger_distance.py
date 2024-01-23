#!/usr/bin/env python3

import mediapipe as mp  # Import mediapipe
import cv2  # Import opencv
import numpy as np
import math


def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    
    
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                            mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                            mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
                            )
    # Draw left hand connections
    #mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                            #mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                            #mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2)
                            #)
    # Draw right hand connections
    #mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                            #mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                            #mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                            #)



mp_drawing = mp.solutions.drawing_utils  # Drawing helpers
mp_holistic = mp.solutions.holistic  # Mediapipe Solutions

cap = cv2.VideoCapture(0)
# Initiate holistic model  
with mp_holistic.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.6) as holistic:
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detections
        results = holistic.process(frame)

        # Recolor back to BGR   
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      
        

        # Extract landmarks
        try:
            if results.pose_landmarks.landmark:

                # Set the points to extract distance between
                keypoint_1 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST]
                keypoint_2 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST]

                # Get the distance between the points
                k1 = np.array([keypoint_1.x, keypoint_1.y, keypoint_1.z])
                k2 = np.array([keypoint_2.x, keypoint_2.y, keypoint_2.z])
                distance_absolute = np.linalg.norm(k1-k2)

                # Show distance and draw line
                start_point = (int(keypoint_1.x * image.shape[1]), int(keypoint_1.y * image.shape[0]))
                end_point = (int(keypoint_2.x * image.shape[1]), int(keypoint_2.y * image.shape[0]))
                cv2.line(image, start_point, end_point, (130, 0, 75), 2)
                mid_point = (int((keypoint_1.x+keypoint_2.x)/2 * image.shape[1]), int((keypoint_1.y+keypoint_2.y)/2 * image.shape[0] - 10))
                cv2.putText(image, str(round(distance_absolute, 1)), mid_point, cv2.FONT_HERSHEY_SIMPLEX, 1.0 , (255, 0, 0), 2, cv2.LINE_AA)

        except Exception as e:
            print('an exception occured: ' + str(e))
       

        # Draw landmarks
        draw_styled_landmarks(image, results)

        
        # Show to screen
        cv2.imshow('Mediapipe Feed', image)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()