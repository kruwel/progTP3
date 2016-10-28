import os

for i in range(10000):

    f = open("python_"+str(i)+".py", 'w')

    f.write("print 'PYTHON RULES'")

    f.close()
