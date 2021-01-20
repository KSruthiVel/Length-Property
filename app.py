from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
      a = request.form.get("str")
      astr = a.strip()
      alen = 0
      for x in astr :
        if x != " ":
            alen += 1
    except:
      alen = 0
      astr = ''

    return render_template('index.html', strlen=alen, strtext=a)

app.run()
 