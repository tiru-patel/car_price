from flask import Flask,render_template,request
import urllib.request
import json

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method=="POST":
        a = request.form['symboling']
        b = request.form['normalized-losses']
        c  = request.form['make']
        d = request.form['fuel-type']
        e = request.form['aspiration']
        f = request.form['num-of-doors']
        g = request.form['body-style']
        h = request.form['drive-wheels']
        i = request.form['engine-location']
        j = request.form['wheel-base']
        k = request.form['length']
        l = request.form['width']
        m = request.form['height']
        n = request.form['curb-weight']
        o = request.form['engine-type']
        p = request.form['num-of-cylinders']
        q = request.form['engine-size']
        r = request.form['fuel-system']
        s = request.form['bore']
        t = request.form['stroke']
        u = request.form['compression-ratio']
        v = request.form['horsepower']
        w = request.form['peak-rpm']
        x = request.form['city-mpg']
        y = request.form['highway-mpg']
        z = request.form['price']

        data = {
            "Inputs": {
                "WebServiceInput0":
                    [
                        {
                            'symboling': a,
                            'normalized-losses': b,
                            'make': c,
                            'fuel-type': d,
                            'aspiration': e,
                            'num-of-doors': f,
                            'body-style': g,
                            'drive-wheels': h,
                            'engine-location': i,
                            'wheel-base': j,
                            'length': k,
                            'width': l,
                            'height': m,
                            'curb-weight': n,
                            'engine-type': o,
                            'num-of-cylinders': p,
                            'engine-size': q,
                            'fuel-system': r,
                            'bore': s,
                            'stroke': t,
                            'compression-ratio': u,
                            'horsepower': v,
                            'peak-rpm': w,
                            'city-mpg': x,
                            'highway-mpg': y,
                            'price': z,
                        },
                    ],
            },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))
        url = 'http://104.215.116.226:80/api/v1/service/update-carprice-real-time-infere/score'
        api_key = 'fOveTUpXDqCZqVFsaMuMsPyiU7rsvMup'  # Replace this with the API key for the web service
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)
        result = response.read()

    return render_template("predict.html",message=result[-40:-4],actual=z)

if __name__=="__main__":
    print("Starting Python Flask server ...")
    #util.load_saved_artifacts()
    app.run(debug=True)









