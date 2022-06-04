from crypt import methods
import imp
from itertools import Predicate
from flask import Flask, escape, request, render_template

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
madel = pickle.load(open("finalized_model.pkl",'rb'))

app = Flask(__name__)

@app.route('/templates/index.html')
def home():
    return render_template("index.html")

app = Flask(__name__)

@app.route('/template/prediction.html', methods=['GET', 'POST'])
def predeiction():
    if request.method=="POST":
        news= request.form['news']
        Predicate= model.predict(vector.transform([news]))
        print(predict)

        return render_template("prediction.html",prediction_text="News headline is -> {}".format(predict))

    else:
        return render_template("prediction.html")
    



if __name__ == '__main__':
    app.run()
