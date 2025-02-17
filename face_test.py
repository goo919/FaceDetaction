import cv2

# FFmpeg 결과에 따라 카메라 번호 설정
camera_index = 0  # FaceTime HD 카메라 (필요에 따라 1, 2로 변경)

# AVFoundation 설정 추가
cap = cv2.VideoCapture(camera_index, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print(f"❌ 카메라 {camera_index}번을 열 수 없습니다. 다른 번호를 시도하세요.")
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
