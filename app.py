from flask import Flask, request
from flask import render_template
#from model import model

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    from model import renderReportOnPage
    
    if request.method=='POST':
        ticker = request.form['ticker']
        print(ticker)
        # Do something with the ticker
        
        # Pass in the text as variable var
        text = renderReportOnPage(ticker)

        
        return text
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run()