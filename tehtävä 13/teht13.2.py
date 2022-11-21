from flask import Flask, Response
import json
import mysql.connector

connect = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password="RootWord1Salasana1",
         autocommit=True
         )
app = Flask(__name__)


@app.route('/kenttä/<Koodi>')
def kenttä(Koodi):
    try:
        sql = "select name, municipality from airport where ident = '" + Koodi +"' "
        cursor = connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        airport = (result[0][0])
        city = (result[0][1])
        statuscode = 200
        respond = {
            "ICAO": Koodi,
            "Name": airport,
            "Municipality": city
        }

    except ValueError:
        statuscode = 400
        respond = {
            "status": statuscode,
            "text": "Invalid summable"
        }

    jsonresponse = json.dumps(respond)
    return Response(response=jsonresponse, status=statuscode, mimetype="application/json")


@app.errorhandler(404)
def page_not_found():
    respond = {
        "status": "404",
        "text": "Invalid code"
    }
    jsonresponse = json.dumps(respond)
    return Response(response=jsonresponse, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)