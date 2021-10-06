from flask import Flask, json, request, Response

from resources.db_util import DBUtil

app = Flask(__name__)
app.config["DEBUG"] = True
db_util = DBUtil()


@app.route('/db_preprocessing/<table_name>', methods=['POST'])
def clean_data(table_name):
    db_api = os.environ['TRAININGDB_API']
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    data_cleaner.clean(df)
    return json.dumps({'message': 'data is cleaned'}, sort_keys=False, indent=4), 200


app.run(host='0.0.0.0', port=5005)
