from flask import Flask, render_template, request
import ast
import search

ROWS_PER_PAGE = 4
app = Flask(__name__)
trigger = 0
@app.route('/')
@app.route('/index')
def index():
    return render_template('search.html')
# TODO: pass the dict not as a very long path
# TODO: Implement end of search table
@app.route('/results/<pagenum>', defaults={'input': None}, methods = ['POST', 'GET'])
@app.route('/results/<pagenum>/<path:input>', methods = ['GET'])
def results(pagenum, input):
    if request.method == 'POST':
        title = request.form['title']
        results_dict = search.retrieve_results(title)
        print(type(PageResult(results_dict, pagenum).data))
        return render_template('results.html', results_dict = PageResult(results_dict, pagenum))
    if request.method == 'GET':
        results_dict = ast.literal_eval(input) 
        print("2nd try")
        print(type(results_dict))
        print(results_dict)
        return render_template('results.html', results_dict = PageResult(results_dict, pagenum))

class PageResult:
    def __init__(self, data, page = 1, number = ROWS_PER_PAGE):
        # global trigger
        self.__dict__ = dict(zip(['data', 'page', 'number'], [data, page, number]))
        sorted_data = sorted(data.items())
        # if trigger == 0: sorted_data = sorted(data.items())
        # else: sorted_data = data
        self.full_listing = [sorted_data[i:i+number] for i in range(0, len(self.data), number)]
        trigger = 1
    def __iter__(self):
        for i in self.full_listing[int(self.page)-1]:
            yield i
    def __repr__(self): #used for page linking
        return "/{}".format(int(self.page)+1) #view the next page

app.run(debug=True, host='0.0.0.0', port=5000)