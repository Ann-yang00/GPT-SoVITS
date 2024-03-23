# Training commands tested on Linux

## Audio Slicer

To slice audio files, execute the following command from the initially cloned GPT-SoVITS directory:

```bash
"C:\Users\zsy\Desktop\GPT-SoVITS-beta0217\runtime\python.exe" tools/slice_audio.py "C:\Users\zsy\Desktop\edited" "output\slicer_opt" -34 4000 300 10 500 0.9 0.25 3 4
```
The original command enables multi-thread audio slicing with the last two parameters. If this is not desired, set these parameters to 0 and 1 respectively:
```bash
python tools/slice_audio.py /home/zsy/trainingSet/ "output/slicer_opt" -34 4000 300 10 500 0.9 0.25 0 1
```

## ASR

For Automatic Speech Recognition (ASR), use the following command:
```bash
"C:\Users\zsy\Desktop\GPT-SoVITS-beta0217\runtime\python.exe" tools/asr/funasr_asr.py -i "C:\Users\zsy\Desktop\GPT-SoVITS-beta0217\output\slicer_opt" -o "output/asr_opt" -s large -l zh -p float16
```


## 3 Step Formatting

Adjust the configurations in the `/GPT_SoVITS/configs/cfig.py` file accordingly, then execute the following commands:
```bash
"C:\Users\zsy\Desktop\GPT-SoVITS-beta0217\runtime\python.exe" GPT_SoVITS/prepare_datasets/1-get-text.py

"C:\Users\zsy\Desktop\GPT-SoVITS-beta0217\runtime\python.exe" GPT_SoVITS/prepare_datasets/2-get-hubert-wav32k.py

"C:\Users\zsy\Desktop\GPT-SoVITS-beta0217\runtime\python.exe" GPT_SoVITS/prepare_datasets/3-get-semantic.py
```


## SoVITS Training

Edit `TEMP/tmp_s2.json` as needed accordingly, then execute the following command:
```bash
"C:\Users\zsy\Desktop\GPT-SoVITS-beta0217\runtime\python.exe" GPT_SoVITS/s2_train.py --e_name TS
```
Pass the name that you have assigned to the model as in the previous cfig using `--e_name`.


## GPT Training

Edit `TEMP/tmp_s1.yaml` as needed, then execute the following command:
```bash
python '/home/azureuser/GPT-SoVITS/GPT_SoVITS/s1_train.py' --config '/home/azureuser/GPT-SoVITS/GPT_SoVITS/configs/tmp_s1.yaml' --e_name TS
```
Use the `--e_name` argument same as before to specify a name.
