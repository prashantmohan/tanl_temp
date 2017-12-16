from flask import Flask
from flask import request
import stockPrice
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

'''
#SAMPLE JSON
{
	"startDate":"2017-09-25",
	"endDate":"2017-12-30",
	"ticker":"BAC",
	"interval":"mon" POSSIBEL Value: M/W/D : Month/Week/Day
}
'''
@app.route('/price', methods = ['POST'])
def getPrice():
    print (request.json)
    dat = stockPrice.StockPrice()
    return dat.getPrice(request.json).to_json(orient='records')

if __name__ == '__main__':
    app.run(port=80, debug=True)