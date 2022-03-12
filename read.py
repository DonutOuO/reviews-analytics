data=[]
count=0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0 :
			print(len(data))

print('檔案讀取完了,總共有',len(data),'筆資料')

sum=0
for lengh in data:
	sum=sum+len(lengh)
print('留言的平均為',sum/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆留言 長度小於100')
print(new[0])

good=[]
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言提到good')




#文字計數
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 100:
		print(word,wc[word])

while True:
	word = input('請輸入想查詢的字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:',wc[word])
	else:
		print('此字沒出現過')
print('感謝使用本查詢功能')








