f=open('a.txt','r')
g=open('c.txt','w')
st=f.read()
g.write(st)
f.close()
g.close()
