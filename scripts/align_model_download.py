from espnet_model_zoo.downloader import ModelDownloader
asr_model_name = "Shinji Watanabe/laborotv_asr_train_asr_conformer2_latest33_raw_char_sp_valid.acc.ave"
d = ModelDownloader()
model = d.download_and_unpack(asr_model_name)

import os
os.makedirs("./.asrmodel", exist_ok=True)

import shutil
shutil.copy(model['asr_train_config'], "./.asrmodel/")
shutil.copy(model['asr_model_file'], "./.asrmodel/")