from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import zipfile
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder_name = request.form.get('folder')
        files = request.files.getlist('images')
        if not folder_name or not files:
            return 'Please provide folder name and at least one image', 400
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                filename = secure_filename(file.filename)
                img = Image.open(file.stream)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                buf = io.BytesIO()
                img.save(buf, format='JPEG', optimize=True, quality=85)
                buf.seek(0)
                zipf.writestr(f"{folder_name}/{filename}", buf.read())
        memory_file.seek(0)
        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f"{folder_name}.zip"
        )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
