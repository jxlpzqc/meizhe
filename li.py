
with open('li.html','w') as f:
	for i in range(1,40):
		f.write("<li><a href='" + str(i) + ".html'>第" + str(i) +"集</a></li>\n")
