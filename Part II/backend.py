from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        age = request.form['age']
        workclass = request.form['workclass']
        fnlwgt = request.form['fnlwgt']
        education = request.form['education']
        education_num = request.form['education_num']
        marital_status = request.form['marital_status']
        occupation = request.form['occupation']
        relationship = request.form['relationship']
        race = request.form['race']
        gender = request.form['gender']
        capital_gain = request.form['capital_gain']
        capital_loss = request.form['capital_loss']
        hours_per_week = request.form['hours_per_week']
        native_country = request.form['native_country']

        features = [('age', [age]),
                    ('workclass', [workclass]), 
                    ('fnlwgt', [fnlwgt]), 
                    ('education', [education]),
                    ('education_num', [education_num]),
                    ('marital_status', [marital_status]),
                    ('occupation', [occupation]),
                    ('relationship', [relationship]), 
                    ('race', [race]), 
                    ('gender', [gender]),
                    ('capital_gain', [capital_gain]), 
                    ('capital_loss', [capital_loss]), 
                    ('hours_per_week', [hours_per_week]),
                    ('native_country', [native_country])]

        import pandas as pd
        df = pd.DataFrame.from_items(features)

        # Replacing '?' data with its prior
        # for value in ['workclass', 'education', 'marital_status', 'occupation',
        #         'relationship','race', 'sex', 'native_country', 'income']:
        #     df[value].replace(['?'], [df.describe(include='all')[value][2]],inplace=True)

        # Labelling data
        from sklearn import preprocessing
        from sklearn.preprocessing import OneHotEncoder

        le = preprocessing.LabelEncoder()

        # workclass_cat = le.fit_transform(df.workclass)
        marital_cat   = le.fit_transform(df.marital_status)
        occupation_cat = le.fit_transform(df.occupation)
        relationship_cat = le.fit_transform(df.relationship)
        # income_cat = le.fit_transform(df.income)
        # race_cat = le.fit_transform(df.race)
        native_country_cat = le.fit_transform(df.native_country)
        education_cat = le.fit_transform(df.education)

        # Override every non-number data with its label
        df.marital_status = marital_cat
        df.occupation = occupation_cat
        df.relationship = relationship_cat
        df.native_country = native_country_cat

        # drop income attribute for features-extracting purpose
        # del df['income']

        # # drop less-related attribute
        del df['age']
        del df['education']
        del df['fnlwgt']
        del df['hours_per_week']

        print(df)

        # # perform one hot encoder for some invalueable attributes
        encoded = pd.get_dummies(df, prefix=['gender', 'race', 'workclass'])

        from sklearn.externals import joblib
        model = joblib.load('best_model.pkl')

        print(encoded)

        print(model.predict(encoded))

        return "ok"
    else:
        return '<h1>Failed to run the process due to invalid request.<h1>'

if __name__ == '__main__':
   app.run(debug = True)