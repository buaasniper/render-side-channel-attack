import os

def mkd():
    path = "/home/ubuntu/Sites/FlaskApp/FlaskApp/data/gpu_win/"
    for i in range(1 , 101):
        file_name = path + str(i)
        os.makedirs(file_name)
mkd()