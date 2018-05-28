from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
@app.route('/list')
def index():
    return render_template("base.html")

@app.route("/addanswer")
def addanswer():
   return render_template("addanswer.html")



if __name__ == "__main__":
    app.run(debug=True)