from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def home():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html", count = session['count'])

# count = session['count'])
@app.route('/click', methods=['POST'])
def click():
    print("Got Post Info")
    session['count']+=int(request.form['total'])-1
    return redirect('/')

@app.route('/destroy', methods=['POST'])
def reset():
    session.clear()
    print(session)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
