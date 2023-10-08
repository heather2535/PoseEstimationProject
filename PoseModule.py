import cv2
import mediapipe as mp
import time
import math



class poseDetector():
    def __init__(self, mode=False, upBody = False, smooth = True,
                 detectionCon = 0.5, trackCon = 0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackingCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth,

                                     self.detectionCon, self.trackingCon)
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS,
                                      self.mpDraw.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=2),
                                      self.mpDraw.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2))
        return img
    def find_position(self, img, draw=True):
        self.lmList = []



def main():
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture('PoseVideos/2.mp4')
    pTime = 0
    detector = poseDetector

    while True:
        detector = poseDetector
        success, img = cap.read()
        img = detector.findPose(img, draw=True)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0,), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()