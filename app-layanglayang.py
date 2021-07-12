from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("layanglayang.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        layanglayang = request.form["layanglayang"]
        layanglayang2 = request.form["layanglayang2"]
        layanglayang3 = request.form["layanglayang3"]
        layanglayang4 = request.form["layanglayang4"]
        sum = float(layanglayang)
        sum2= float(layanglayang2)
        sum3 = float(layanglayang3)
        sum4 = float(layanglayang4)
        result = (0.5 * sum3 * sum4)
        result2 = (sum + sum + sum2 + sum2)
        return render_template("layanglayang.html", sum=result, sum2=result2, sum3=sum2, sum4=sum3)
    else:
        return render_template("layanglayang.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
