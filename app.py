from flask import Flask, render_template, send_from_directory, jsonify, request

from utils.IGdownload import IGDownloader

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/scripts/<path:path>')
def send_scripts(path):
    return send_from_directory("static/scripts/", path)


@app.route('/img/<path:path>')
def send_static_images(path):
    return send_from_directory("static/images/", path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory("./images/", path)


@app.route('/styles/<path:path>')
def send_styles(path):
    return send_from_directory("static/styles/", path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download/')
def download():
    img = request.args.get('url')
    Downloader = IGDownloader()
    try:
        img_info = Downloader.download_img(img)
        if img_info:
            return jsonify(
                status=200,
                name=img_info[0],
                path=img_info[1],
            )
        else:
            return jsonify(
                status=404
            )
    except Exception as e:
        return jsonify(
            status="500",
            error=e,
        )


if __name__ == "__main__":
    app.run(threaded=True)
