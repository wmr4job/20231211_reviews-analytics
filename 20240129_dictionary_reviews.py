# dictionary_reviews

import time # 使用time的功能
import progressbar # 載入進度條的套件

# 每讀取1000筆就印出一次
data = [] # data存每筆留言內容
count = 0
with open('reviews.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		data.append(line)
		count += 1
print('檔案讀取完畢，總共有', len(data), '筆資料')

# 單字計數、計時
start_time = time.time()

wc = {} # 宣告字典 wc = word_count
for d in data: # 從所有留言中讀取單筆留言內容
	words = d.strip('\n').split(' ') # words清單存每筆留言切出來的單字['There', 'are', 'very'....]
	for word in words: # 從清單中讀取每個單字
		if word in wc: # 判斷這個單字是否出現過
			wc[word] += 1 # 有的話就+1
		elif word not in wc:
			wc[word] = 1 # 沒有就把字新增到wc字典中(新增key)計為1

end_time = time.time()
print('單字計數共花', end_time - start_time, 's')

# 印出每個字出現的次數
for word in wc:
	if wc[word] > 100: # 出現100次的印出來
		print(word, ':', wc[word])

# 讓使用者查字出現的次數
while True:
	word = input('請問你想查什麼字：(輸入q離開)')
	if word == 'q':
		print('離開！')
		break
	elif word not in wc:
		print('沒有這個字哦！')
	else:
		print(word, '出現次數為：', wc[word])
