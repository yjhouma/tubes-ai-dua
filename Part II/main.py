from flask import Flask, render_template, flash, request
from wtforms import Form, SubmitField, SelectField, IntegerField, validators
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
app.secret_key = 'development_key'

class predictForm(Form):
    age = IntegerField('Age', [validators.DataRequired])
    workclass = SelectField('Workclass',choices=[('Private','Private'),('Self-emp-not-inc','Self-emp-not-inc'),('Self-emp-inc','Self-emp-inc'),('Federal-gov','Federal-gov'),('Local-gov','Local-gov'),('State-gov','State-gov'),('Without-pay','Without-pay'),('Never-worked','Never-worked')])
    fnlwgt = IntegerField('Fnlwgt', [validators.DataRequired])
    education = SelectField('Education',choices=[('Bachelors','Bachelors'),('Some-college','Some-college'),('11th','11th'),('HS-grad','HS-grad'),('Prof-school','Prof-school'),('Assoc-acdm','Assoc-acdm'),('Assoc-voc','Assoc-voc'),('9th','9th'),('7th-8th','7th-8th'),('12th','12th'),('Masters','Masters'),('1st-4th','1st-4th'),('10th','10th'),('Doctorate','Doctorate'),('5th-6th','5th-6th'),('Preschool','Preschool')])
    educationnum = IntegerField('Education-num', [validators.DataRequired])
    maritalstatus = SelectField('Marital Status',choices=[('Married-civ-spouse','Married-civ-spouse'),('Divorced','Divorced'),('Never-married','Never-married'),('Separated','Separated'),('Widowed','Widowed'),('Married-spouse-absent','Married-spouse-absent'),('Married-AF-spouse','Married-AF-spouse')])
    occupation = SelectField('Occupation',choices=[('Tech-support','Tech-support'),('Craft-repair','Craft-repair'),('Other-service','Other-service'),('Sales','Sales'),('Exec-managerial','Exec-managerial'),('Prof-specialty','Prof-specialty'),('Handlers-cleaners','Handlers-cleaners'),('Machine-op-inspct','Machine-op-inspct'),('Adm-clerical','Adm-clerical'),('Farming-fishing','Farming-fishing'),('Transport-moving','Transport-moving'),('Priv-house-serv','Priv-house-serv'),('Protective-serv','Protective-serv'),('Armed-Forces','Armed-Forces')])
    relationship = SelectField('Relationship',choices=[('Wife','Wife'),('Own-child','Own-child'),('Husband','Husband'),('Not-in-family','Not-in-family'),('Other-relative','Other-relative'),('Unmarried','Unmarried')])
    race = SelectField('Race',choices=[('White','White'),('Asian-Pac-Islander','Asian-Pac-Islander'),('Amer-Indian-Eskimo','Amer-Indian-Eskimo'),('Other','Other'),('Black','Black')])
    sex = SelectField('Sex',choices=[('Female','Female'),('Male','Male')])
    capitalgain = IntegerField('Capital-gain', [validators.DataRequired])
    capitalloss = IntegerField('Capital-loss', [validators.DataRequired])
    hoursperweek = IntegerField('Hours-per-week', [validators.DataRequired])
    nativecountry = SelectField('Native Country', choices=[('United-States','United-States'),('Cambodia','Cambodia'),('England','England'),('Puerto-Rico','Puerto-Rico'),('Canada','Canada'),('Germany','Germany'),('Outlying-US(Guam-USVI-etc)','Outlying-US(Guam-USVI-etc)'),('India','India'),('Japan','Japan'),('Greece','Greece'),('South','South'),('China','China'),('Cuba','Cuba'),('Iran','Iran'),('Honduras','Honduras'),('Philippines','Philippines'),('Italy','Italy'),('Poland','Poland'),('Jamaica','Jamaica'),('Vietnam','Vietnam'),('Mexico','Mexico'),('Portugal','Portugal'),('Ireland','Ireland'),('France','France'),('Dominican-Republic','Dominican-Republic'),('Laos','Laos'),('Ecuador','Ecuador'),('Taiwan','Taiwan'),('Haiti','Haiti'),('Columbia','Columbia'),('Hungary','Hungary'),('Guatemala','Guatemala'),('Nicaragua','Nicaragua'),('Scotland','Scotland'),('Thailand','Thailand'),('Yugoslavia','Yugoslavia'),('El-Salvador','El-Salvador'),('Trinadad&Tobago','Trinadad&Tobago'),('Peru','Peru'),('Hong','Hong'),('Holand-Netherlands','Holand-Netherlands')])
    submit = SubmitField('Submit')

def changeSexToNumber(x):
    if x == 'Female':
        return 0
    elif x == 'Male':
        return 1
    else:
        return np.nan

def one_hot_encode(df, label):
    onehot = pd.get_dummies(df[label],prefix=label)
    df.drop(label, axis=1,inplace = True)
    return df.join(onehot)


def changeClassToNumber(x):
    if x == 0:
        return '<=50K'
    elif x == 1:
        return '>50K'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = predictForm(request.form)

    if request.method == 'POST':
        features = [('age', [form.age.data]),
                    ('workclass', [form.workclass.data]),
                    ('fnlwgt', [form.fnlwgt.data]),
                    ('education', [form.education.data]),
                    ('education-num', [form.educationnum.data]),
                    ('marital-status', [form.maritalstatus.data]),
                    ('occupation', [form.occupation.data]),
                    ('relationship', [form.relationship.data]),
                    ('race', [form.race.data]),
                    ('sex', [form.sex.data]),
                    ('capital-gain', [form.capitalgain.data]),
                    ('capital-loss', [form.capitalloss.data]),
                    ('hours-per-week', [form.hoursperweek.data]),
                    ('native-country', [form.nativecountry.data])]
        df = pd.DataFrame.from_items(features)
        df.sex = df.sex.map(lambda x: changeSexToNumber(x))
        df = one_hot_encode(df, 'workclass')
        df = one_hot_encode(df, 'education')
        df = one_hot_encode(df, 'marital-status')
        df = one_hot_encode(df, 'occupation')
        df = one_hot_encode(df, 'relationship')
        df = one_hot_encode(df, 'race')
        df = one_hot_encode(df, 'native-country')
        all_features = [('age', [0]), ('fnlwgt', [0]), ('education-num', [0]), ('sex', [0]), ('capital-gain', [0]),
                        ('capital-loss', [0]), ('hours-per-week', [0]), ('workclass_Federal-gov', [0]),
                        ('workclass_Local-gov', [0]), ('workclass_Never-worked', [0]), ('workclass_Private', [0]),
                        ('workclass_Self-emp-inc', [0]), ('workclass_Self-emp-not-inc', [0]),
                        ('workclass_State-gov', [0]), ('workclass_Without-pay', [0]), ('education_10th', [0]),
                        ('education_11th', [0]), ('education_12th', [0]), ('education_1st-4th', [0]),
                        ('education_5th-6th', [0]), ('education_7th-8th', [0]), ('education_9th', [0]),
                        ('education_Assoc-acdm', [0]), ('education_Assoc-voc', [0]), ('education_Bachelors', [0]),
                        ('education_Doctorate', [0]), ('education_HS-grad', [0]), ('education_Masters', [0]),
                        ('education_Preschool', [0]), ('education_Prof-school', [0]), ('education_Some-college', [0]),
                        ('marital-status_Divorced', [0]), ('marital-status_Married-AF-spouse', [0]),
                        ('marital-status_Married-civ-spouse', [0]), ('marital-status_Married-spouse-absent', [0]),
                        ('marital-status_Never-married', [0]), ('marital-status_Separated', [0]),
                        ('marital-status_Widowed', [0]), ('occupation_Adm-clerical', [0]),
                        ('occupation_Armed-Forces', [0]), ('occupation_Craft-repair', [0]),
                        ('occupation_Exec-managerial', [0]), ('occupation_Farming-fishing', [0]),
                        ('occupation_Handlers-cleaners', [0]), ('occupation_Machine-op-inspct', [0]),
                        ('occupation_Other-service', [0]), ('occupation_Priv-house-serv', [0]),
                        ('occupation_Prof-specialty', [0]), ('occupation_Protective-serv', [0]),
                        ('occupation_Sales', [0]), ('occupation_Tech-support', [0]),
                        ('occupation_Transport-moving', [0]), ('relationship_Husband', [0]),
                        ('relationship_Not-in-family', [0]), ('relationship_Other-relative', [0]),
                        ('relationship_Own-child', [0]), ('relationship_Unmarried', [0]), ('relationship_Wife', [0]),
                        ('race_Amer-Indian-Eskimo', [0]), ('race_Asian-Pac-Islander', [0]), ('race_Black', [0]),
                        ('race_Other', [0]), ('race_White', [0]), ('native-country_Cambodia', [0]),
                        ('native-country_Canada', [0]), ('native-country_China', [0]), ('native-country_Columbia', [0]),
                        ('native-country_Cuba', [0]), ('native-country_Dominican-Republic', [0]),
                        ('native-country_Ecuador', [0]), ('native-country_El-Salvador', [0]),
                        ('native-country_England', [0]), ('native-country_France', [0]),
                        ('native-country_Germany', [0]), ('native-country_Greece', [0]),
                        ('native-country_Guatemala', [0]), ('native-country_Haiti', [0]),
                        ('native-country_Holand-Netherlands', [0]), ('native-country_Honduras', [0]),
                        ('native-country_Hong', [0]), ('native-country_Hungary', [0]), ('native-country_India', [0]),
                        ('native-country_Iran', [0]), ('native-country_Ireland', [0]), ('native-country_Italy', [0]),
                        ('native-country_Jamaica', [0]), ('native-country_Japan', [0]), ('native-country_Laos', [0]),
                        ('native-country_Mexico', [0]), ('native-country_Nicaragua', [0]),
                        ('native-country_Outlying-US(Guam-USVI-etc)', [0]), ('native-country_Peru', [0]),
                        ('native-country_Philippines', [0]), ('native-country_Poland', [0]),
                        ('native-country_Portugal', [0]), ('native-country_Puerto-Rico', [0]),
                        ('native-country_Scotland', [0]), ('native-country_South', [0]), ('native-country_Taiwan', [0]),
                        ('native-country_Thailand', [0]), ('native-country_Trinadad&Tobago', [0]),
                        ('native-country_United-States', [0]), ('native-country_Vietnam', [0]),
                        ('native-country_Yugoslavia', [0])]
        all_df = pd.DataFrame.from_items(all_features)
        for x in all_df.columns:
            for y in df.columns:
                if x == y:
                    all_df[x] = df[y]
        filename = 'model.pkl'
        loaded_model = pickle.load(open(filename, 'rb'))
        y_predict = loaded_model.predict(all_df.values)
        hasil = changeClassToNumber(y_predict)
        return render_template("answer.html",hasil=hasil)
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)