import cv2, sys
import numpy as np

def draw_polygon(image, pts):
    """주어진 좌표들을 이용하여 다각형을 그립니다."""
    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(image, [pts], True, (0, 255, 0), 1)
    return image

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 20, (0, 0, 255), 1)
    elif flags & cv2.EVENT_FLAG_SHIFTKEY and event == cv2.EVENT_LBUTTONDOWN:
        param[1].append((x, y))
    elif not flags & cv2.EVENT_FLAG_SHIFTKEY:
        # Shift 키를 뗀 경우 다각형 그림
        if len(param[1]) > 2:  
            param[0] = draw_polygon(param[0], param[1])
            print("Polygon drawn.")
        param[1] = [] # 좌표 리스트 초기화

if __name__ == '__main__':
    img = np.ones((512, 512, 3), np.uint8) * 255
    vectors = list()
    
    cv2.namedWindow('img')
    cv2.moveWindow('img', 0, 0)
    cv2.setMouseCallback('img', onMouse, [img, vectors])
    while True:
        cv2.imshow('img', img)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    img2 = cv2.blur(img, (5, 5))
    img_cubic = cv2.resize(img2, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_CUBIC)
    cv2.namedWindow('img_cubic')
    cv2.moveWindow('img_cubic', 0, 600)
    cv2.imshow('img_cubic', img_cubic)
    
    img_blur_interarea = cv2.resize(img, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    cv2.namedWindow('img_blur_interarea')
    cv2.moveWindow('img_blur_interarea', 0, 600)
    cv2.imshow('img_blur_interarea', img_blur_interarea)
    
    cv2.waitKey()
    cv2.destroyAllWindows()