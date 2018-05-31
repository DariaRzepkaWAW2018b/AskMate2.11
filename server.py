from flask import Flask, request, render_template
import persistence
import logic

app=Flask(__name__)

@app.route("/")
@app.route('/list', methods=["POST", "GET"])
def index():
    list_of_headers=persistence.import_headers_from_file("sample_data/question.csv")
    list_of_dictionaries = persistence.import_data_from_file("sample_data/question.csv")
    return render_template("list_of_question.html", list_of_dictionaries=list_of_dictionaries, list_of_headers=list_of_headers, id =id)

@app.route("/addanswer", methods=["POST"])
def addanswer():
   return render_template("addanswer.html")

@app.route("/addquestion", methods=['POST','GET'])
def addquestion():
    if request.method == "POST":
        return render_template('addquestion.html')
    elif request.method == "GET":
        return redirect('/')

@app.route("/question/<int:id>", methods=["POST","GET"])
@app.route("/question/<int:id>/<slug>", methods=["POST","GET"])
def question(id, slug=None):
    id = str(id)
    title_q = logic.find_by_id_q(id)
    title_a = logic.find_by_id_a(id)
    return render_template("question.html", title_q = title_q, title_a = title_a)

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