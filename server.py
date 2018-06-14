from flask import Flask, request, render_template, redirect
import database_common
import database_manager



app=Flask(__name__)

@app.route("/")
@app.route('/list', methods=["POST", "GET"])
def index():
    list_of_headers=['id', 'submission_time','view_number', 'vote_number','title','message','image']
    list_of_dictionaries = database_manager.import_data_from_file()
    return render_template("list_of_question.html", list_of_dictionaries=list_of_dictionaries, list_of_headers=list_of_headers, id =id)



@app.route("/addquestion", methods=['POST','GET'])
def addquestion():
    if request.method == "POST":
        return render_template('addquestion.html')
    elif request.method == "GET":
        return redirect('/')

@app.route("/submitquestion", methods=['POST'])
def submit_question():
    new_title = request.form['title']
    new_message = request.form['question']
    database_manager.add_data(new_title, new_message)
    return redirect('/')

@app.route("/addanswer", methods=['POST','GET'])
def addanswer():
    if request.method == "POST":
        return render_template('addanswer.html')
    elif request.method == "GET":
        return redirect('/')

@app.route("/submitanswer", methods=['POST'])
def submit_answer():
    new_title = request.form['title']
    new_message = request.form['question']
    database_manager.add_data(new_title, new_message)
    return redirect('/')

@app.route("/question/<int:id>", methods=["POST","GET"])
@app.route("/question/<int:id>/<slug>", methods=["POST","GET"])
def question(id, slug=None):
    id = str(id)
    # title_q = logic.find_by_id_q(id)
    # list_of_dictionaries = logic.find_by_id_a(id)
    # list_of_answer_headers = persistence.import_headers_from_file("sample_data/answer.csv")
    return render_template("single_question.html", title_q = title_q, list_of_dictionaries = list_of_dictionaries, list_of_answer_headers=list_of_answer_headers)

@app.route("/question/<question_id>/delete", methods=['GET', 'POST'])
def delete_question(question_id):
    # logic.delete_by_id("q", question_id)
    return redirect('/')

@app.route("/answer/<answer_id>/delete", methods=['GET', 'POST'])
def delete_answer(answer_id):
    # logic.delete_by_id("a", question_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True,
            port = 5001)