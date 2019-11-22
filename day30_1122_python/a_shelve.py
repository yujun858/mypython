import shelve
shv = shelve.open(r'shv.db')

shv['name'] = 'dana'
shv['age'] = 18

shv.close()
# 生成：shv.db.bak shv.db.dat shv.db.dir

#shelve读取：
shv = shelve.open(r'shv.db')
print(shv['name'],shv['age'])

shv.close()