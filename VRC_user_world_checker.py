#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3.x Code

import os
import glob
import datetime

# 環境設定
LOG_FOLDER	= os.getenv('APPDATA') + "\../LocalLow\VRChat\VRChat"
LOG_FILE	= "output_log_*.txt"

LOG_OUTPUT_DIR	= ".\VRC_Log"

### start...
# ログファイルリスト確認
logfile = LOG_FOLDER + "\\" + LOG_FILE
#print(logfile)
file_list=glob.glob(logfile)

# ログ出力先フォルダ作成
if not os.path.exists(LOG_OUTPUT_DIR):
    os.mkdir(LOG_OUTPUT_DIR)

now = datetime.datetime.now()
outfilename = LOG_OUTPUT_DIR + '/log_' + now.strftime('%Y%m%d_%H%M%S') + '.log'
f = open(outfilename, 'w', encoding='utf-8', errors='ignore')

#ファイルの最終更新時刻順にソートする
file_list.sort(key=os.path.getmtime)

for file in file_list:
	#print(file)
	f.write(file)
	f.write("\n")

	ld = open(file, encoding='utf-8', errors='ignore')
	lines = ld.readlines()
	ld.close()

	for line in lines:
		if line.find("[RoomManager] Entering Room:") >= 0:
			#print(line[:-1])
			f.write(line[:-1])
			f.write("\n")
		elif line.find("[NetworkManager] OnPlayerJoined") >= 0:
			f.write(line[:-1])
			f.write("\n")
