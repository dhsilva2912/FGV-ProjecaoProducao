from flask import Flask, request, jsonify, abort
import json
import s3fs
import settings

# Whitenoise enables Flask to serve static files efficiently.
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(
    app.wsgi_app, root="static/", index_file=True, autorefresh=True
)

@app.route("/api")
def get_file():
    fs = s3fs.S3FileSystem()
    try:
        with fs.open("{}/RomeMIRS-ProductionRecords/Prod_Records2019.json".format(settings.S3_BUCKET), 'rb') as f:
            data = json.load(f)
    except FileNotFoundError:
        abort(404)
    return jsonify(data)

if __name__ == "__main__":
    app.run()