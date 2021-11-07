from flask import Flask, render_template, url_for
 
app = Flask(__name__)

app.add_url_rule('/photos/<path:filename>', endpoint='photos', view_func=app.send_static_file) 
@app.route('/')
def index():
   return render_template("index.html")
 
if __name__ == '__main__':
    app.run(debug=True)
