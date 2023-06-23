from flask import Flask, render_template,request
import json

from module.get_user_info import*
from module.api import*


app = Flask(__name__)


@app.route('/')
def hello_world():
    user_tag_raw, tagIDs = user.get_song_style()
    user_tag =  json.dumps(user_tag_raw)
    
    return render_template("pie-borderRadius.html", user_tag = user_tag)

if __name__ == '__main__':
    app.run()
    