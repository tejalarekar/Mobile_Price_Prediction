from flask import Flask ,request,render_template,jsonify
import config
import numpy as np
import json
import pickle

app=Flask(__name__)

with open(config.MODEL_FILE_PATH,"rb") as file:
    model=pickle.load(file)
with open(config.JSON_FILE_PATH,"r") as file:
    json_data=json.load(file)

@app.route("/")
def home_api():
    return render_template("login.html")

@app.route("/predict1")
def predict1():
    data=request.form 
    test_array=np.zeros(20)
    print(test_array) 
    test_array[0]=int(data["battery_power"])
    test_array[1]=int(data["blue"])
    test_array[2]=int(data["clock_speed"])
    test_array[3]=int(data["dual_sim"])
    test_array[4]=int(data["fc"])
    test_array[5]=int(data["four_g"])
    test_array[6]=int(data["int_memory"])
    test_array[7]=int(data["m_dep"])
    test_array[8]=int(data["mobile_wt"])
    test_array[9]=int(data["n_cores"])
    test_array[10]=int(data["pc"])
    test_array[11]=int(data["px_height"])
    test_array[12]=int(data["px_width"])
    test_array[13]=int(data["ram"])
    test_array[14]=int(data["sc_h"])
    test_array[15]=int(data["sc_w"])
    test_array[16]=int(data["talk_time"])
    test_array[17]=int(data["three_g"])
    test_array[18]=int(data["touch_screen"])
    test_array[19]=int(data["wifi"]) 

    price=model.predict([test_array])
    return jsonify({"Result":f"the predicted mobile price:{price}"})
if __name__=="__main__":
    app.run()


    