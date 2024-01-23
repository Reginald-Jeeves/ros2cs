#!/usr/bin/env python3

import mediapipe as mp  # Import mediapipe
import cv2  # Import opencv
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import pickle
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from hsi_interfaces.msg import Gesture


class GestureNode(Node):

    def __init__(self):
        super().__init__("gesture_node")
        self.publisher_ = self.create_publisher(Gesture, "/gesture", 10)

        #mp_drawing = mp.solutions.drawing_utils  # Drawing helpers
        mp_holistic = mp.solutions.holistic  # Mediapipe Solutions
        # model = make_pipeline(StandardScaler(), GradientBoostingClassifier())
        with open('/home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/src/sensors/gesture/gesture/models/body_language_gb_1.pkl', 'rb') as f:
            model = pickle.load(f)
        cap = cv2.VideoCapture(0)
        # Initiate holistic model
        with mp_holistic.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.8) as holistic:
            # commands = []

            while cap.isOpened():

                # Read feed
                ret, frame = cap.read()

                # Make detections
                self.mediapipe_detection(frame, holistic)

                # Draw landmarks
                self.draw_styled_landmarks()

                # Export coordinates
                try:

                    # Concatenate rows
                    row = self.extract_keypoints()
                    distance_absolute = self.distance_calculation()

                    # Make Predictions
                    X = pd.DataFrame([row])
                    body_language_class = model.predict(X)[0]
                    body_language_prob = model.predict_proba(X)[0]
                    # print(body_language_class, body_language_prob)

                    # Logic to create drone commands list
                    prob = body_language_prob[np.argmax(body_language_prob)]
                    self.command_publisher(body_language_class, round(prob, 2), distance_absolute)

                    # Get status box
                    cv2.rectangle(self.image, (0, 0), (300, 60), (245, 117, 16), -1)

                    # Display Class
                    cv2.putText(self.image, 'CLASS'
                                , (95, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(self.image, body_language_class
                                , (90, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                    # Display Probability
                    cv2.putText(self.image, 'PROB'
                                , (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(self.image, str(round(body_language_prob[np.argmax(body_language_prob)], 2))
                                , (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                except Exception as err:
                    print(f"Unexpected {err=}, {type(err)=}")
                    #pass

                cv2.imshow('Gesture Detection', self.image)
                

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()
        self.destroy_node()
        


    def mediapipe_detection(self, frame, model):
        self.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
        self.image.flags.writeable = False  # self.image is no longer writeable
        self.results = model.process(self.image)  # Make prediction
        self.image.flags.writeable = True  # self.image is now writeable
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR



    def extract_keypoints(self):
        pose = list(np.array([[res.x, res.y, res.z, res.visibility] for res in
                            self.results.pose_landmarks.landmark]).flatten() if self.results.pose_landmarks else np.zeros(33 * 4))
        lh = list(np.array([[res.x, res.y, res.z] for res in
                            self.results.left_hand_landmarks.landmark]).flatten() if self.results.left_hand_landmarks else np.zeros(
            21 * 3))
        rh = list(np.array([[res.x, res.y, res.z] for res in
                            self.results.right_hand_landmarks.landmark]).flatten() if self.results.right_hand_landmarks else np.zeros(
            21 * 3))

        return pose + lh + rh
    

    def command_publisher(self, body_language_class, prob, distance_absolute):
        # comm_dict = {3: 'takeoff', 0: 'land', 2: 'formation'}
        msg = Gesture()
        if prob > 0.95:
            if body_language_class == 'land':
                msg = Gesture()
                msg.gesture = 2
                msg.probability = prob
                msg.distance_hands = distance_absolute
                #print('land')
                self.publisher_.publish(msg)
            elif body_language_class == 'formation':
                msg = Gesture()
                msg.gesture = 3
                msg.probability = prob
                msg.distance_hands = distance_absolute
                #print('formation')
                self.publisher_.publish(msg)
            elif body_language_class == 'takeoff':
                msg = Gesture()
                msg.gesture = 1
                msg.probability = prob
                msg.distance_hands = distance_absolute
                #print('takeoff')
                self.publisher_.publish(msg)
            

    def draw_styled_landmarks(self):
        # Draw face connections
        mp_drawing = mp.solutions.drawing_utils
        mp_holistic = mp.solutions.holistic
        # mp_drawing.draw_landmarks(self.image, self.results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                                #mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
                                #mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1)
                                #)
        # Draw pose connections
        mp_drawing.draw_landmarks(self.image, self.results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                                mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
                                )
        # Draw left hand connections
        mp_drawing.draw_landmarks(self.image, self.results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2)
                                )
        # Draw right hand connections
        mp_drawing.draw_landmarks(self.image, self.results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                                mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                )
        
    def distance_calculation(self):
        mp_holistic = mp.solutions.holistic
        try:
            if self.results.pose_landmarks.landmark:

                # Set the points to extract distance between
                keypoint_1 = self.results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST]
                keypoint_2 = self.results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST]

                # Get the distance between the points
                k1 = np.array([keypoint_1.x, keypoint_1.y])
                k2 = np.array([keypoint_2.x, keypoint_2.y])
                distance_absolute = np.linalg.norm(k1-k2)

                # Show distance and draw line
                start_point = (int(keypoint_1.x * self.image.shape[1]), int(keypoint_1.y * self.image.shape[0]))
                end_point = (int(keypoint_2.x * self.image.shape[1]), int(keypoint_2.y * self.image.shape[0]))
                cv2.line(self.image, start_point, end_point, (130, 0, 75), 2)
                mid_point = (int((keypoint_1.x+keypoint_2.x)/2 * self.image.shape[1]), int((keypoint_1.y+keypoint_2.y)/2 * self.image.shape[0] - 10))
                cv2.putText(self.image, str(round(distance_absolute, 1)), mid_point, cv2.FONT_HERSHEY_SIMPLEX, 1.0 , (255, 0, 0), 2, cv2.LINE_AA)

                # Return distance
                return distance_absolute
            
        except Exception as e:
            print('an exception occured: ' + str(e))



def main(args=None):
    rclpy.init(args=args)
    node=GestureNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
