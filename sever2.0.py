from flask import Flask,request,jsonify
import util

app=Flask(__name__)
@app.route("/sex_options",methods=['GET'])
def get_sex_names():
    response=jsonify({
        "sex":util.get_sex_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response
@app.route("/chest_options",methods=['GET'])
def get_chest_names():
    response=jsonify({
        "chestpaintype":util.get_chestpaintype_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response
@app.route("/rest_options",methods=['GET'])
def get_restingecg_names():
    response=jsonify({
        "restingecg":util.get_restingecg_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response
@app.route("/rest_options",methods=['GET'])
def get_stslope_names():
    response=jsonify({
        "stslope":util.get_stslope_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route('/is_heart_disease',methods=['GET',"POST"])
def is_heartdisease():
    Age=float(request.form['Age']),
    Sex=request.form['Sex'],
    ChestPainType=(request.form['ChestPainType']),
    RestingBP=float(request.form['RestingBP']),
    Cholesterol=float(request.form['Cholesterol']),
    FastingBS=float(request.form['FastingBS']),
    RestingECG=request.form['RestingECG'],
    MaxHR=float(request.form['MaxHR']),
    ExerciseAngina=request.form['ExerciseAngina'],
    Oldpeak=float(request.form['Oldpeak']),
    ST_Slope=request.form['ST_Slope']
    response=jsonify({
        "is_HeartDisease":util.is_heartdisease(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope)
    })
    print(util.is_heartdisease(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope))

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__=='__main__':
 print("Creating a flask server for Price Predictions")
 util.load_artifacts()
 app.run()
