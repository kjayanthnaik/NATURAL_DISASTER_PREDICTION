import numpy as np
import smtplib
from flask import Flask,request,render_template
import pickle
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/earth')
def earth():
   return render_template('earthquake.html')
@app.route('/cyclone')
def cyclone():
   return render_template('cyclone.html')
@app.route('/flood')
def flood():
   return render_template('flood.html')
@app.route('/contact')
def contact():
   return render_template('contactus.html')

@app.route('/esm')
def esm():
   return render_template('esm.html')
@app.route('/fs')
def fs():
   return render_template('FS.html')

@app.route('/cs')
def cs():
   return render_template('CS.html')
@app.route('/tech')
def tech():
   return render_template('tech.html')


@app.route('/pre',methods=['POST'])
def pre():
    model=pickle.load(open('model.pkl','rb'))
    val=[float(x) for x in request.form.values()]
    fival=[np.array(val)]
    prediction=model.predict(fival)
    pred=float(prediction)
    if(pred>0 and pred<1 ):
        a="moderate chances of earthquake"
    elif(pred >=1 ):
        a="high chances of earthquake"
    elif(pred<0):
        a="no chances of earthquake"
    else:
        a="no chances of earthquake"
    return render_template('earthquake.html',prediction_text="predicted value is:{0}and {1}".format(pred,a))

@app.route('/flo',methods=['POST'])
def flo():
    fmodel=pickle.load(open('fmodel.pkl','rb'))
    val=[float(x) for x in request.form.values()]
    fival=[np.array(val)]
    prediction=fmodel.predict(fival)
    pred=float(prediction)
    if(pred>0 and pred<0.9):
        a="less chances of flood"
    elif(pred>=1):
        a="high occurrence of flood"
    else:
        a="no chances of flood"
    return render_template('flood.html',prediction_text="predicted value is:{0}and {1}".format(pred,a))


@app.route('/cyl',methods=['POST'])
def cyl():
    cymodel=pickle.load(open('cmodel.pkl','rb'))
    val=[float(x) for x in request.form.values()]
    fival=[np.array(val)]
    prediction=cymodel.predict(fival)
    pred=float(prediction)
    if(pred>0 and pred<4.0):
        a="less chances of cyclone"
    elif(pred>=4 and pred<5.5):
        a="moderate cyclone and it is in tropical depression"
    elif(pred>=5.5 and pred<6):
        a="high chances of cyclone and it is in tropical strome"
    elif(pred>6):
        a="chances of extratropical cyclone"
    else:
        a="No chances of cyclone"
    return render_template('cyclone.html',prediction_text="predicted value is:{0}and {1}".format(pred,a))
if __name__ == "__main__":
    app.run(debug=True)
