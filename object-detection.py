%cd ..
from google.colab import drive
drive.mount('/content/gdrive')

# this creates a symbolic link so that now the path /content/gdrive/My\ Drive/ is equal to /mydrive
!ln -s /content/gdrive/My\ Drive/ /mydrive

#Navigate to /mydrive/yolov4
%cd /mydrive/yolov5custom/

!git clone https://github.com/ultralytics/yolov5

 %cd yolov5/

%pip install -qr requirements.txt

import torch

!python train.py --img 640 --batch 16 --epochs 3 --data dataset.yaml --weights yolov5s.pt --cache

