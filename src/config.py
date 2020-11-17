import os
from flask import Flask, request
import telebot
from flask_sqlalchemy import SQLAlchemy



token = "1309595418:AAG36P4Kkmey-DR_caODLEVRGKGRwIPYGzg"
DATABASE_URL = 'postgres+psycopg2://postgres:031003@localhost:5432/bot'

server = Flask(__name__)
bot = telebot.TeleBot(token)
server.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
server.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(server)