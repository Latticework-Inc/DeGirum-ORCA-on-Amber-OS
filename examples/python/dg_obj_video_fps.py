#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:56:07 2024

@author: sam.latticework

Function:
    Test the speed of ORCA inference, expressed in FPS
"""

import cv2
import time
import degirum as dg


def draw_label(frame, label, left, top):
    """Draw text onto image at location."""
    # Get text size.
    text_size = cv2.getTextSize(label, FONT_FACE, FONT_SCALE, THICKNESS)
    dim, baseline = text_size[0], text_size[1]
    # Use text size to create a BLACK rectangle.
    cv2.rectangle(frame, (left, top), (left + dim[0], top + dim[1] + baseline), BLACK, cv2.FILLED);
    # Display text inside the rectangle.
    cv2.putText(frame, label, (left, top + dim[1]), FONT_FACE, FONT_SCALE, YELLOW, THICKNESS, cv2.LINE_AA)

def draw_bbox(frame, dets):
    """Draw bbox on frame.

    Args:
        frame       (np.array): The frame array.
        dets        (list): The list contain detection results.
        example:
                    [{'bbox': [719.8341369628906,
                       530.6585693359375,
                       1343.5263061523438,
                       1218.5697937011719],
                      'category_id': 1,
                      'label': 'car',
                      'score': 0.9236121773719788},
                     ...}]
    """
    # print('frame type:', type(frame)) # numpy.ndarray
    # h, w, _ = frame.shape
    # print('frame h, w:', h, w)
    for result in dets:
        # create a mask with object
        label = result["label"]
        score = result["score"]
        label_score = "{}: {:.2f}".format(label, score)
        # print(label_score)
        # bbox = result['bbox']    # (x1, y1, x2, y2)
        left, top, width, height = result['bbox']
        left, top, width, height = round(left), round(top), round(width), round(height)
        # print(left, top, width, height)

        # # draw bbox
        label_color = RED
        cv2.rectangle(frame, (left, top), ( width, height), label_color, THICKNESS)
        draw_label(frame, label_score, left, top)

def main():
        # 打開視訊流
    # cap = cv2.VideoCapture(0) #CCD
    cap = cv2.VideoCapture(video_path)
    
    # 初始化計數器
    frame_count = 0
    start_time = time.time()
    
    # 初始化平滑過濾器
    fps_filtered = 30
    
    
    while True:
        # 讀取每個影像
        ret, frame = cap.read()
    
        if ret:
            # ### You must use model.predict() to get results ###
            res = model.predict(frame)
            results = res.results
            draw_bbox(frame, results)
    
            # 增加計數器
            frame_count += 1
        
            # 計算時間差
            elapsed_time = time.time() - start_time
        
            # 計算FPS
            fps = frame_count / elapsed_time
        
            # 應用低通濾波器
            fps_filtered = fps_filtered * 0.9 + fps * 0.1
        
            # 顯示平滑過的FPS
            cv2.putText(frame, f"FPS: {int(fps_filtered)}", (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        
            # 顯示影像
            cv2.imshow('Video Stream', frame)
    
        else:
            # Break the loop if the end of the video is reached
            break
    
        # 檢測按鍵輸入，按下 'q' 停止循環
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # 釋放視訊流
    cap.release()
    
    # 關閉窗口
    cv2.destroyAllWindows()
    
    # 要加這一行避免關視窗時被卡住
    cv2.waitKey(2)


if __name__ == "__main__":
    
    # Text parameters.
    FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
    FONT_SCALE = 0.7
    THICKNESS = 3
    
    # Colors
    BLACK  = (0,0,0)
    BLUE   = (255,178,50)
    YELLOW = (0,255,255)
    RED    = (0,0,255)
    
    # Connect to AI inference engine
    hw_location = '172.17.0.1' 
    model_name = 'HumanVehicleV8n--512x512_quant_n2x_orca1_1'
    # model_name = 'NVRVehicleV8n--512x512_quant_n2x_orca1_1'
    
    # Connect to degirum server ###
    zoo = dg.connect(hw_location)
    # print(zoo.list_models())
    
    # load dg model
    model = zoo.load_model(model_name)

    # file source
    video_path = '/Users/sam.latticework/lw2024/2_testData/Cam06_2024042.mp4'
    
    # inference
    main()

