from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events.html')
def events():
    return render_template('events.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/industry.html')
def industry():
    return render_template('industry.html')

#make debug=False while production
if __name__ == "__main__":
    app.run(debug=False)
