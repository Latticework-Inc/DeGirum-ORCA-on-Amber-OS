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
            _ = model.predict(frame)

            # 增加計數器
            frame_count += 1
        
            # 計算時間差
            elapsed_time = time.time() - start_time
        
            # 計算FPS
            fps = frame_count / elapsed_time
        
            # 應用低通濾波器
            fps_filtered = fps_filtered * 0.9 + fps * 0.1
        
            # 顯示平滑過的FPS
            print("\r", f'frame_count: {frame_count}, FPS: {int(fps_filtered)}',end="",flush=True) 

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

    # Connect to degirum server ###
    zoo = dg.connect(hw_location)
    # print(zoo.list_models())
    zoo_list = ['HumanVehicleV8n--512x512_quant_n2x_orca1_1',
                'NVRVehicleV8n--512x512_quant_n2x_orca1_1',
                'WeaponV8s--640x640_quant_n2x_orca1_1']
    model_name = zoo_list[2]
    # load dg model
    model = zoo.load_model(model_name)

    # file source
    video_path = '/Users/sam.latticework/lw2024/2_testData/Cam06_2024042.mp4'
    
    # inference
    main()

