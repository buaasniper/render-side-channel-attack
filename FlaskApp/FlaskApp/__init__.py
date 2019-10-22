from flask import Flask, render_template, request, jsonify
import os,sys
import time
import csv
import numpy as np
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./aquarium/aquarium.html')

@app.route("/iframe")
def iframe():
    return render_template('./aquarium/load.html')

@app.route('/server_test',methods=['POST'])
def server_test():
    data1 = request.form.getlist('post_data1[]')
    data2 = request.form.getlist('post_data2[]')
    data3 = request.form.getlist('post_data3[]')
    data4 = request.form.getlist('post_data4[]')
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    fname = "/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/Youtube/cache/" + now +r".csv"
    csvFile = open(fname,'wb')
    writer = csv.writer(csvFile)
    writer.writerows([data1,data2,data3,data4])
    csvFile.close()

    s1 = list(map(float, data1))
    t1 = range(len(s1))

    s2 = list(map(float, data2))
    t2 = range(len(s2))

    s3 = list(map(float, data3))
    t3 = range(len(s3))

    s4 = list(map(float, data4))
    t4 = range(len(s4))
    fig, axs = plt.subplots()
    axs.plot(t1, s1, t2, s2, t3, s3, t4, s4)
    axs.set_xlabel('Real Time')
    axs.set_ylabel('Render Time')
    axs.grid(True)
    plt.legend(('First Time(D)', 'Second Time', 'Third Time', 'Fourth Time'),loc='upper right')
    fig.tight_layout()
    plt.savefig("/home/ubuntu/Sites/FlaskApp/FlaskApp/templates/Data/Youtube/cache/" + now +r".png")


    return jsonify(otstr=[1,2,3,4,5,6,7])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)