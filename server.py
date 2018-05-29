from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
@app.route('/list', methods=["POST", "GET"])
def index():
    return render_template("list_of_question.html")

@app.route("/addanswer")
def addanswer():
   return render_template("addanswer.html")

@app.route("/addquestion", methods=['POST'])
def addquestion():
    return render_template('addquestion.html')

if __name__ == "__main__":
    app.run(debug=True,
            port = 5000)