#reviews-analytics 留言分析

data = []
count = 0
with open('reviews.txt', 'r') as f: #讀取reviews檔
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是取餘數的運算符號，每1000筆印出一次
			print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆資料')