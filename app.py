# flask app url routing
from flask import Flask,render_template,request,redirect,url_for,jsonify
# render_template is used when there is get request
# request is used  

app=Flask(__name__)

    
    
@app.route("/",methods=["GET"])
def welcome():
    return render_template('home.html',content=['happy','sad','not sad'])

@app.route("/index",methods=['GET'])
def index():
    return "it is index page"

@app.route("/success/<int:score>")
def success(score):
    return "the person has passes with score"+str(score)

@app.route("/fail/<float:score>")
def fail(score):
    return "The person has failed with score " + str(score)

@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=='GET':
        return render_template('form.html')
    # this form.html file should be under templates folder
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        res=""
        if average_marks>50:
            res="success"
        else:
            res="fail"
        return  redirect(url_for(res,score=average_marks))
        
        # return render_template('form.html',score=average_marks)
@app.route("/api",methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)

    
if __name__=="__main__":
    app.run(debug=True)
