from flask import Flask, request, render_template, redirect
import database_common
import database_manager



app=Flask(__name__)

@app.route("/")
@app.route('/list', methods=["POST", "GET"])
def index():
    list_of_headers=['id', 'submission_time','view_number', 'vote_number','title','message','image']
    list_of_dictionaries = database_manager.import_data_from_file_question()
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
    database_manager.add_data_question(new_title, new_message)
    return redirect('/')


@app.route("/list_of_answer",methods=["POST","GET"])
def list_of_answers():
    list_of_headers=['id', 'question_id', 'message', 'image']
    id_q=request.form['question_id']
    dict_title_q=database_manager.import_title_by_id(id_q)
    title_q = dict_title_q['title']
    list_of_answer = database_manager.import_data_from_file_answer(id_q)
    return render_template("list_of_answer.html", list_of_headers = list_of_headers, 
    list_of_answer = list_of_answer, title_q = title_q)

@app.route("/addanswer", methods=["GET"])
def addanswer():
   return render_template("addanswer.html")

@app.route("/submitanswer", methods=['POST'])
def submit_answer():
    new_message = request.form['message']
    print(new_message)
    database_manager.add_data_answer(new_message)
    return redirect('/list_of_answer')



# @app.route("/question/<int:id>", methods=["POST"])
# @app.route("/question/<int:id>/<slug>", methods=["POST"])
# def question(id, slug=None):
#     id = id
#     list_of_headers=['id', 'submission_time','view_number', 'vote_number','question_id','message','image']
#     list_of_answer = database_manager.import_data_from_file_answer()
#     return render_template("list_of_answer.html",list_of_answer = list_of_answer,list_of_headers=list_of_headers, id = id)




@app.route("/comment",methods=["GET","POST"])
# @app.route("/comment")
def comment():
    list_of_headers=['id', 'question_id','answer_id', 'message','submission_time','edited_counted']
    list_of_comment = database_manager.import_data_from_file_comment()
    return render_template("list_of_comments.html", list_of_headers = list_of_headers, list_of_comment = list_of_comment)


@app.route("/add_comment", methods = ["GET"])
def add_comment_template():
    return render_template("/add_comment.html")

@app.route("/submit_comment", methods = ["POST"])
def add_comment():
    new_message = request.form['comment']
    database_manager.add_data_comment(new_message)
    return redirect("/comment")



















@app.route("/question/<question_id>/delete", methods=['GET', 'POST'])
def delete_question(question_id):
    return redirect('/')

@app.route("/answer/<answer_id>/delete", methods=['GET', 'POST'])
def delete_answer(answer_id):
    return redirect('/')


@app.route("/add_answer_comment/<answer_id>", methods=['GET', 'POST'])
def add_comment_answer():
    return


if __name__ == "__main__":
    app.run(debug=True,
            port = 5001)