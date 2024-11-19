# prompt: PATH_ZIPを解凍する

import zipfile
import os

PATH_ZIP = "raw/atmacup18_dataset.zip"

# 解凍先のディレクトリを指定
extract_dir = "raw"  # 解凍先ディレクトリ

# ディレクトリが存在しない場合は作成
if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

# zipファイルの解凍
with zipfile.ZipFile(PATH_ZIP, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print(f"ファイルを {extract_dir} に解凍しました。")