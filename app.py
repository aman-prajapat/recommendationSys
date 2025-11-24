from flask import Flask, request, jsonify, render_template
import sqlite3
from groq_query import translate_to_sql

app = Flask(__name__)

def run_sql(query):
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        conn.close()
        return results
    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_query = request.json.get("query")
    sql_query = translate_to_sql(user_query)
    results = run_sql(sql_query)
    return jsonify({"sql_query": sql_query, "results": results})

if __name__ == "__main__":
    app.run(debug=True)
