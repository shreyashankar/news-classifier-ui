from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('input.html')


@app.route('/submitarticle',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _article = request.form['article']

        return render_template('result.html',**locals())

    except Exception as e:
        return json.dumps({'error':str(e)})


if __name__ == "__main__":
    app.run()
