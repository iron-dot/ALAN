import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from listToString import listToString

fourcc = cv2.VideoWriter_fourcc(*'XVID')    # 영상을 기록할 코덱 설정
font = ImageFont.truetype('dataset/SCDream6.otf', 20) # 글꼴파일을 불러옴
is_record = False
is_record2 = False
f = open('dataset/mp4.txt','w',encoding='utf-8')
f.write("False")
f = open('dataset/mp4.txt','r',encoding='utf-8')
mp4_file = listToString(f.readlines())

def input_real():
    # 첫 번째 카메라 열기
    global is_record
    global is_record2
    cap1 = cv2.VideoCapture(0)
    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 녹화상태는 처음엔 거짓으로 설정

    if not cap1.isOpened():
        print("Failed to open camera 1")
        return

    # 두 번째 카메라 열기
    cap2 = cv2.VideoCapture(1)
    cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    if not cap2.isOpened():
        print("Failed to open camera 2")
        return

    while True:
        # 카메라에서 프레임 읽기
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        nowDatetime_path = now.strftime('%Y-%m-%d %H_%M_%S') # 파일이름으로는 :를 못쓰기 때문에 따로 만들어줌
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        cv2.rectangle(img=frame1, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)     
    
        # 아래의 4줄은 글자를 영상에 더해주는 역할을 함    
        frame1 = Image.fromarray(frame1)    
        draw = ImageDraw.Draw(frame1)    
        # xy는 텍스트 시작위치, text는 출력할 문자열, font는 글꼴, fill은 글자색(파랑,초록,빨강)   
        draw.text(xy=(10, 15),  text="Camera 1"+nowDatetime, font=font, fill=(255, 255, 255))
        frame1 = np.array(frame1)

        cv2.rectangle(img=frame2, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)     
    
        # 아래의 4줄은 글자를 영상에 더해주는 역할을 함    
        frame2 = Image.fromarray(frame2)    
        draw = ImageDraw.Draw(frame2)    
        # xy는 텍스트 시작위치, text는 출력할 문자열, font는 글꼴, fill은 글자색(파랑,초록,빨강)   
        draw.text(xy=(10, 15),  text="Camera 2"+nowDatetime, font=font, fill=(255, 255, 255))
        frame2 = np.array(frame2)
        key = cv2.waitKey(30)   # 30ms 동안 키입력 대기
        if key == ord('r') and is_record == False:  # 현재 녹화상태가 아니며 r 키를 누르면
            is_record = True            # 녹화상태로 만들어줌
            # 비디오 객체에 (파일이름(한글가능), 인코더, 초당프레임률(정확하지 않음), 영상크기) 로 영상을 쓸 준비
            video = cv2.VideoWriter("dataset/input.avi", fourcc, 15, (frame1.shape[1], frame1.shape[0]))
            f = open('avi.txt','w',encoding='utf-8')
            f.write("dataset/input.avi")

        elif key == ord('r') and is_record == True: # 녹화중인 상태에서 다시 r키를 누르면
            is_record = False       # 녹화상태를 꺼줌
            video.release()         # 녹화 종료

        elif key == ord('c'):       # c 키를 누르면
            # (파일이름(한글불가, 영어만), 이미지)로 영상을 캡쳐하여 그림파일로 저장
            cv2.imwrite("capture " + nowDatetime_path + ".png", frame1)  # 파일이름(한글안됨), 이미지 

        elif key == ord('o') and is_record2 == False:  # 현재 녹화상태가 아니며 r 키를 누르면
            is_record2 = True            # 녹화상태로 만들어줌
            # 비디오 객체에 (파일이름(한글가능), 인코더, 초당프레임률(정확하지 않음), 영상크기) 로 영상을 쓸 준비
            video2 = cv2.VideoWriter("dataset/input2.avi", fourcc, 15, (frame2.shape[1], frame2.shape[0]))
            f = open('avi.txt','w',encoding='utf-8')
            f.write("dataset/input2.avi")

        elif key == ord('o') and is_record2 == True: # 녹화중인 상태에서 다시 r키를 누르면
            is_record2 = False       # 녹화상태를 꺼줌
            video2.release()         # 녹화 종료

        elif key == ord('f'):       # c 키를 누르면
            # (파일이름(한글불가, 영어만), 이미지)로 영상을 캡쳐하여 그림파일로 저장
            cv2.imwrite("capture " + nowDatetime_path + ".png", frame2)  # 파일이름(한글안됨), 이미지 

        elif key == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
                break
        if is_record == True:       # 현재 녹화상태이면 

            # 비디오 객체에 현재 프레임 저장
            video.write(frame1)

            # 녹화중이라는 것을 보여주기 위해 보여주는 화면에는 빨간색 점을 표시해줌
            cv2.circle(img=frame1, center=(620, 15), radius=5, color=(0,0,255), thickness=-1)
            mp4_file = "True"

            f = open('mp4.txt','w',encoding='utf-8')
            f.write(mp4_file)

        if is_record2 == True:       # 현재 녹화상태이면            

            # 비디오 객체에 현재 프레임 저장
            video2.write(frame2)
            # 녹화중이라는 것을 보여주기 위해 보여주는 화면에는 빨간색 점을 표시해줌
            cv2.circle(img=frame2, center=(620, 15), radius=5, color=(0,0,255), thickness=-1)

            mp4_file = "True"
            f = open('mp4.txt','w',encoding='utf-8')
            f.write(mp4_file)


        if not ret1 or not ret2:
            print("Failed to capture frame")
            break

        # 영상 처리 작업

        # 프레임 출력
        cv2.imshow("Camera 1", frame1)
        cv2.imshow("Camera 2", frame2)

        # 'q' 키를 누르면 종료

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 카메라 해제
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()


    