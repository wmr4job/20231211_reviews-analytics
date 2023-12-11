#reviews-analytics 留言分析

#每讀取1000筆就印出一次
# data = []
# count = 0
# with open('reviews.txt', 'r') as f: #讀取reviews檔
# 	for line in f:
# 		data.append(line)
# 		count += 1
# 		if count % 1000 == 0: # %是取餘數的運算符號，每1000筆印出一次
# 			print(len(data))
# print('檔案讀取完畢，總共有', len(data), '筆資料')

#計算每筆留言平均長度
sum_len = 0
data_len = []
filtering =[]
with open('reviews.txt', 'r') as f: #讀取reviews檔
	for line in f:
		data_len.append(len(line))
		sum_len += len(line)

		if len(line) < 100: #篩選留言長度小於100的
			filtering.append(line)

average = sum_len / len(data_len)
print('每筆留言平均長度：',average)
print('共有', len(filtering), '筆資料長度小於100')