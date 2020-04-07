from flask import Flask,render_template,request,send_file,make_response
from flask_qrcode import QRcode
import pdfkit
app = Flask(__name__)
qrcode = QRcode(app)
@app.route('/', methods=['POST'])
@app.route('/')
def hello_world():
    if request.method == 'POST':
        ssid=request.form['ssid']
        pwd=request.form['pwd']
        data= 'WIFI:S:'+ssid+';'+'T:WPA;'+'P:'+pwd+';;'
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # change this according to the path of wkhtmltopdf in your system.
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        rendered=render_template('op.html',ssid=ssid,pwd=pwd,data=data)
        pdf=pdfkit.from_string(rendered, False,configuration=config)
        response=make_response(pdf)
        response.headers['Content-Type']='application/pdf'
        response.headers['Content-Disposition']='attachment; filename=Print Me.pdf'
        return response
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)