# 1.setup
* conda create -n Centernet python==3.8
* pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
* pip install opencv-python==4.8.0.74
* pip install PyWavelets==1.4.1
* conda install matplotlib

# 2.prepare dataset

Please download the IMO dataset and extract it to the designated directory.

Directory structure:

<img src="media/image1.png" id="image1">

# 3.prepare model weights


Download the weights for diff. models in the paper, CNet refers to CenterNet, while WNet refers to CenterNet optimized with wavelet decomposition:

<table id="table1">
<tr>
<td>N</td>
<td>Model</td>
<td>Weights</td>
</tr>
<tr>
<td rowspan="2">512</td>
<td>CNet</td>
<td>Centernet_512.pth</td>
</tr>
<tr>
<td>WNet</td>
<td>CenterNet_Wav_512.pth</td>
</tr>
<tr>
<td rowspan="2">640</td>
<td>CNet</td>
<td>Centernet_640.pth</td>
</tr>
<tr>
<td>WNet</td>
<td>CenterNet_Wav_640.pth</td>
</tr>
<tr>
<td rowspan="2">768</td>
<td>CNet</td>
<td>Centernet_768.pth</td>
</tr>
<tr>
<td>WNet</td>
<td>CenterNet_Wav_768.pth</td>
</tr>
</table>

Additionally, the weight file centernet_512_voc.pth trained on the VOC2007 dataset in Figure 1 of our paper is available. Simply place these weight files in the directory 'model_data'.

# 4.execute locally

4.1Train the models:

(1)Centernet_512.pth:

python train.py --surfix 512 --fep 150 --ufep 300

python train.py --surfix 512 --fep 50 --ufep 100

python train.py --surfix 512 --fep 50 --ufep 100

(2)Centernet_640.pth:

python train.py --surfix 640--fep 150 --ufep 300

python train.py --surfix 640--fep 50 --ufep 100

python train.py --surfix 640--fep 50 --ufep 100

(3)Centernet_768.pth:

python train.py --surfix 768--fep 150 --ufep 300

python train.py --surfix 768--fep 50 --ufep 100

python train.py --surfix 768--fep 50 --ufep 100

python train.py --surfix 768--fep 50 --ufep 100

(4)CenterNet_Wav_512.pth:

python train.py --surfix 512--fep 150 --ufep 300

python train.py --surfix 512--fep 50 --ufep 100

python train.py --surfix 512--fep 50 --ufep 100

(5)CenterNet_Wav_640.pth:

python train.py --surfix 640--fep 150 --ufep 300

python train.py --surfix 640--fep 50 --ufep 100

python train.py --surfix 640--fep 50 --ufep 100

(6)CenterNet_Wav_768.pth:

python train.py --surfix 768--fep 150 --ufep 300

python train.py --surfix 768--fep 50 --ufep 100

python train.py --surfix 768--fep 50 --ufep 100

4.2Evaluation

(1) Centernet_512.pth:

python mAP.py model_data/Centernet_512.pth 512

(2) Centernet_640.pth:

python mAP.py model_data/Centernet_640.pth 640

(3) Centernet_768.pth:

python mAP.py model_data/Centernet_768.pth 768

(4) CenterNet_Wav_512.pth:

python mAP.py model_data/CenterNet_Wav_512.pth 512

(5) CenterNet_Wav_640.pth:

python mAP.py model_data/CenterNet_Wav_640.pth 640

(6) CenterNet_Wav_768.pth:

python mAP.py model_data/CenterNet_Wav_768.pth 768
