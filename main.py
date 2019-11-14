from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    return render_template('echo.html')


@app.route('/echo', methods=['POST'])
def echo():
    if 'text' in request.form:
        echo = request.form.get('text')
        return render_template('echo.html', echo=echo)

    return render_template('echo.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
