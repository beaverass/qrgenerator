from flask import Flask, render_template, request, make_response
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

def generate_qrcode(link):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    output = BytesIO()
    img.save(output)
    img_data = output.getvalue()
    img_base64 = base64.b64encode(img_data).decode()
    return img_base64

@app.route('/', methods=['GET', 'POST'])
def home():
    link = None
    qr_image = None
    if request.method == 'POST':
        link = request.form.get('link')
        if link:
            qr_image = generate_qrcode(link)
    return render_template('index.html', qr_image=qr_image, linkk=link)

if __name__ == '__main__':
    app.run(debug=True)

