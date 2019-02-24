for i in range(10,40):
	with open(str(i)+'.html','w') as f:
		f.write('<video src="http://vip.zuiku8.com/1808/M%E8%80%85%E6%97%A0%E7%96%86-'+ str(i) +'.mp4" controls="controls">您的浏览器不支持 video 标签。</video>')
	