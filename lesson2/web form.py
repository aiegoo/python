#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
from time import strftime
from flask import flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = ''


# In[3]:


Class MyFirstForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    surname = TextField("Surname:", validators=[validators.required()])


# In[4]:


def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time
def write_to_dis(name, surname, email, telephone, rateme):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write("DateStamp={}, Name={}, Surname={}, Email={}, Telephone={}, Ratteme={} \n".format(timestamp, name, surname, email, number, number))
    data.close()


# In[5]:


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = MyFirstForm(request.form)
    
    if request.method == 'POST':
        name=request.form['name']
        surname=request.form['surname']
        email=request.form['email']
        password=request.form['password']
        telephone=request.form['telephone']
        rademe=request.form['rateme']
        if form.validate():
            wite_to_disk(name, surname, email)
            flash('Hello: {} {}'.format(name,surname))
        else:
            flash('Error: All Fields are required')
            
    return render_template('index.html', form=form)


# In[ ]:


if __name__ == "__main__"
app.run()

