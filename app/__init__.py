# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:31:43 2023

@author: Notis
"""

from flask import Flask

app = Flask(__name__)

from app import views
