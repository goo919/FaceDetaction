import cv2

# 얼굴 탐지기 로드 (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 웹캠 연결 (0: 기본 웹캠)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 흑백 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 얼굴에 박스 표시
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 화면에 출력
    cv2.imshow("Face Detection", frame)

    # ESC 키(27)를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 종료 후 자원 해제
cap.release()
cv2.destroyAllWindows()
