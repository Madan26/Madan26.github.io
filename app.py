from flask import Flask, request
from gevent.pywsgi import WSGIServer
import openpyxl
app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    input_string = request.form['inputString']
    input_time=int(request.form['inputtime'])
    print("Received string:", input_string)
    print("Recieved time :",input_time)
    file_path = 'mainduration list.xlsx'
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    
    
    
    # Search for the string in column 1
    for row in sheet.iter_rows(values_only=True):
            if row[0] == input_string:
                #print(row[1])
                s=row[1]
                s=s[:-3]
                finalstring=int(s)/input_time
                return  "Total Number of days that would be taken to watch the movie is  "+str(finalstring)+" days."
             else:
                return "Sorry the movie or tv show not available in dataset right now,updating for you......."

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    app.run()
