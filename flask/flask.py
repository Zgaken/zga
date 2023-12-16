from flask import Flask, render_template, request

app = Flask(__name__)

# 假設這是你的成績資訊，可以是從資料庫或其他來源取得
grades = {
    'Alice': {'Math': 90, 'Science': 85, 'History': 88},
    'Bob': {'Math': 78, 'Science': 80, 'History': 75},
    'Charlie': {'Math': 92, 'Science': 88, 'History': 95}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    student_name = request.form['student_name']
    if student_name in grades:
        student_grades = grades[student_name]
        return render_template('result.html', student_name=student_name, grades=student_grades)
    else:
        return render_template('not_found.html', student_name=student_name)

if __name__ == '__main__':
    app.run(debug=True)