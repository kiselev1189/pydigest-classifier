from flask import Flask, request
import json
from sklearn.externals import joblib

app = Flask(__name__)

classifier = joblib.load("classifier_64.pkl")


@app.route("/api/v1.0/classify/", methods=["POST"])
def classify():
    json_data = request.get_json(force=True)["links"]
    links = []
    for entity in json_data:
        links.append(entity["link"])

    predicted = classifier.predict(json_data)

    out = {"links": [{i[0]: bool(i[1])} for i in zip(links, predicted)]}
    return json.dumps(out)

if __name__ == '__main__':
    app.run(debug=True)