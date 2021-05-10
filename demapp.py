import pandas as pd
import flask
import pickle

app = flask.Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        noofveh1 = flask.request.form['noofveh']
        roveg1 = flask.request.form['roveh']
        roadsurf1 = flask.request.form['roadsurf']
        light1 = flask.request.form['light']
        wether1 = flask.request.form['wether']
        cclass1 = flask.request.form['cclass']
        sex1 = flask.request.form['sex']
        age1 = flask.request.form['age']
        typeveg1 = flask.request.form['typeveh']


        input_variables = pd.DataFrame([[noofveh1, roveg1, roadsurf1, light1, wether1, cclass1, sex1, age1, typeveg1]],
                                       columns=['Number of Vehicles', '1st Road Class', 'Road Surface','Lighting Conditions','Weather Conditions','Casualty Class','Sex of Casualty','Age of Casualty','Type of Vehicle'], dtype=float)
        prediction = model.predict(input_variables)[0]
        
        if prediction==1:
            prediction="Looks like the Accident is serious one"
        else:
            prediction="Looks like the Accident is slight one"

        return flask.render_template('main.html',
                                     original_input={'Number of Vehicles':noofveh1,
                                                     '1st Road Class':roveg1,
                                                     'Road Surface':roadsurf1,
                                                     'Lighting Conditions':light1,
                                                     'Weather Conditions':wether1,
                                                     'Casualty Class':cclass1,
                                                     'Sex of Casualty':sex1,
                                                     'Age of Casualty':age1,
                                                     'Type of Vehicle':typeveg1},result=prediction)


if __name__ == '__main__':
    app.run()
