import os, os.path

path = 'image'
x = os.path.exists(path)

print (x)

path = 'download/text/'
total_doc = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

print (total_doc)