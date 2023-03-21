from flask import Flask, request,render_template
app = Flask(__name__)
from main import fun
@app.route('/encrypt', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        mode = request.form['mode']
        data = request.form['data']
        return fun(password,mode,data)
        # return 
    return render_template('index.html')
# print(fun("mohit","e","raja"))
# print(fun("mohit","d","e-99045.png"))
if __name__ == "__main__":
    app.run(debug=True)