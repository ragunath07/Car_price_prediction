# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:21:51 2021

@author: Acer
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
app=Flask (__name__)
pickle_in=open('model.pkl','rb')
regressor=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'welcome in'

@app.route('/')
def prediction():
    name=request.args.get('name')
    year=request.args.get('year')
    km_driven=request.args.get('km_driven')
    fuel=request.args.get('fuel')
    seller_type=request.args.get('seller_type')
    transmission=request.args.get('transmission')
    owner=request.args.get('owner')
    
    prediction=regressor.predict([[name,year,km_driven,fuel,seller_type,transmission,owner
                                   ]])
    return 'The predicted value is '+ str(prediction)

if __name__ == '__main__':
    app.run()