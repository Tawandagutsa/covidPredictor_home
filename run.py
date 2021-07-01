from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/')
# def upload_file():
#     return render_template('file.html')
    
@app.route('/home')
def upload_file():
    return render_template('file.html')


if __name__ == '__main__':
    app.run(debug=True)