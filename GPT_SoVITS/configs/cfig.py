# cfig.py

import os
# change the exp_name to change model name
exp_name = "FZ"
inp_text = "/output/asr_opt/slicer_opt.list"
inp_wav_dir = "/output/slicer_opt"
# change i_part and all_parts to enables multi-thread processing
i_part = 0 
all_parts = 1
opt_dir = f"/logs/{exp_name}"
bert_pretrained_dir = "/GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large"
cnhubert_base_path= "/GPT_SoVITS/pretrained_models/chinese-hubert-base"
pretrained_s2G = "/GPT_SoVITS/pretrained_models/s2G488k.pth"
s2config_path = "/GPT_SoVITS/configs/s2.json"
is_half = eval(os.environ.get("is_half", "True"))
gpu_id = "0"
