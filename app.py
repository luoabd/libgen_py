from flask import Flask, render_template, request
import search

ROWS_PER_PAGE = 5
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('search.html')

@app.route('/results', methods = ['POST'])
def results():
    if request.method == 'POST':
        page = request.args.get('page', 1, type=int)
        title = request.form['title']
        results_dict = search.retrieve_results(title)
        return render_template('results.html', results_dict = results_dict)

app.run(debug=True, host='0.0.0.0', port=5000)