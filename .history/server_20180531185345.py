from flask import Flask, request, render_template
import persistence
import logic

app=Flask(__name__)

@app.route("/")
@app.route('/list', methods=["POST", "GET"])
def index():
    item = logic.find_by_id(id)
    list_of_headers=persistence.import_headers_from_file("sample_data/question.csv")
    list_of_dictionaries = persistence.import_data_from_file("sample_data/question.csv")
    return render_template("list_of_question.html", list_of_dictionaries=list_of_dictionaries, list_of_headers=list_of_headers, item = item)

@app.route("/addanswer", methods=["POST"])
def addanswer():
   return render_template("addanswer.html")

@app.route("/addquestion", methods=['POST','GET'])
def addquestion():
    if request.method == "POST":
        return render_template('addquestion.html')
    elif request.method == "GET":
        return redirect('/')

@app.route("/question", methods=["POST"])
def question():
    return render_template("question.")

@app.route("/question/<question_id>/delete", methods=['GET', 'POST'])
def delete_question(question_id):
    logic.delete_by_id("q", question_id)
    return redirect('/')

@app.route("/answer/<answer_id>/delete", methods=['GET', 'POST'])
def delete_answer(answer_id):
    logic.delete_by_id("a", question_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True,
            port = 5001)