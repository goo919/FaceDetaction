import cv2

# 카메라 연결 (0번부터 테스트)
for i in range(3):  # 0, 1, 2 번 카메라 테스트
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ 카메라 {i}번 연결 성공!")
        cap.release()
    else:
        print(f"❌ 카메라 {i}번 연결 실패!")

cap.release()
cv2.destroyAllWindows()
