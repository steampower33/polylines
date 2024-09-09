import cv2, sys
import numpy as np

def draw_polygon(image, pts):
    """주어진 좌표들을 이용하여 다각형을 그립니다."""
    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(image, [pts], True, (0, 255, 0), 2)
    return image

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 20, (0, 0, 255), 3)
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
        
    img_2x = cv2.resize(img, None, fx=2.0, fy=2.0)
    img_05x_nearest = cv2.resize(img_2x, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    img_05x_linear = cv2.resize(img_2x, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    img_05x_area = cv2.resize(img_2x, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    img_05x_cubic = cv2.resize(img_2x, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    img_05x_lanczos4 = cv2.resize(img_2x, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)
    
    cv2.namedWindow('img_2x')
    cv2.moveWindow('img_2x', 512 * 3, 0)
    cv2.imshow('img_2x', img_2x)
    
    cv2.namedWindow('img_05x_nearest')
    cv2.moveWindow('img_05x_nearest', 512, 0)
    cv2.imshow('img_05x_nearest', img_05x_nearest)
    
    cv2.namedWindow('img_05x_linear')
    cv2.moveWindow('img_05x_linear', 512 * 2, 0)
    cv2.imshow('img_05x_linear', img_05x_linear)
    
    cv2.namedWindow('img_05x_area')
    cv2.moveWindow('img_05x_area', 0, 600)
    cv2.imshow('img_05x_area', img_05x_area)
    
    cv2.namedWindow('img_05x_cubic')
    cv2.moveWindow('img_05x_cubic', 512, 600)
    cv2.imshow('img_05x_cubic', img_05x_cubic)
    
    cv2.namedWindow('img_05x_lanczos4')
    cv2.moveWindow('img_05x_lanczos4', 512 * 2, 600)
    cv2.imshow('img_05x_lanczos4', img_05x_lanczos4)
    
    cv2.waitKey()
    cv2.destroyAllWindows()