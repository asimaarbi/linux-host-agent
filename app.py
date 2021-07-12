from flask import Flask, render_template


@app.route('/', methods=['Get'])
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
