import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

drawing_spec = mp_drawing.DrawingSpec((0,255,255),thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        #mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_TESSELATION,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
        mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_CONTOURS,landmark_drawing_spec=None,connection_drawing_spec= mp_drawing.DrawingSpec((0,255,0),thickness=2, circle_radius=1))

    # Flip the image horizontally for a selfie-view display.
    mask = cv2.inRange(image, (0, 0, 0), (0, 255, 0));
    resul = cv2.bitwise_and(image, image, mask=mask)
    image2 = cv2.cvtColor(resul, cv2.COLOR_BGR2GRAY)
    cv2.threshold(image2, 15, 255, cv2.THRESH_BINARY, image2)
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(image2, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()