from database import Database_Tools
import sort

from flask import Flask, render_template, request


app = Flask(__name__)
database_tools = Database_Tools()

@app.route('/')
def view_stats():

    return render_template('view_stats.html')

@app.route('/new_install/', methods=['POST'])
def get_stats():
    stats = request.get_json()

    database_tools.database_store(stats)

    return "Doop!"


if __name__ == '__main__':
    app.run( 
        host="0.0.0.0"
    )
