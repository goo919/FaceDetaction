import cv2

# FaceTime HD 카메라를 직접 사용 (번호 변경 가능)
cap = cv2.VideoCapture(0)  # 또는 1, 2로 변경

if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다. 다른 번호를 시도해보세요.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 프레임을 가져올 수 없습니다.")
        break

    cv2.imshow("Face Detection Test", frame)

    # ESC 키(27)를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
