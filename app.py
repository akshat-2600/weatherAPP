from flask import Flask , render_template , request #1
import requests                                     #2

app = Flask(__name__)                               #3

@app.route("/")                                     #5
def homepage():                                     #4
    return render_template("index.html")

@app.route("/weatherapp" , methods = ["POST",'GET'])  #8
def get_weather_data() :                              #7
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {                                    
        "q" : request.form.get("city") ,
        "appid" : request.form.get("appid")
        }

    response = requests.get(url , params = params)
    data = response.json()
    return f"data : {data}"

if __name__ == "__main__" :                         #6
    app.run(host="0.0.0.0" , port = 8888)        
    

