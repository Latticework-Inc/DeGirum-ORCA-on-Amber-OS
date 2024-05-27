#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:41:44 2024

@author: sam.latticework

Requirements:
    !apt update
    !apt install ffmpeg -y

Function:
    Using ORCA video annotations
"""

import degirum as dg
import degirum_tools
from pathlib import Path
# import IPython.display

# Connect to AI inference engine
hw_location = '61.222.194.101' 
model_name = 'NVRVehicleV8n--512x512_quant_n2x_orca1_1'

zoo = dg.connect(hw_location)
# print(zoo.list_models())

# Inference video
model = zoo.load_model(model_name)
# set model parameters
model.overlay_show_probabilities = True
model.overlay_line_width = 1

srcRoot = '/Users/sam.latticework/lw2024/2_testData/VAISense/52920FP'
srcPath = srcRoot + '/'+ 'VAISenseTapo-Truck_video.mp4'
orig_path = Path(srcPath)
ann_path = srcRoot + orig_path.stem + "_annotated" + orig_path.suffix

degirum_tools.annotate_video(model, orig_path, ann_path)