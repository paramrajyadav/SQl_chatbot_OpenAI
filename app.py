from Chatbot import ChatWithSql
from flask import Flask,jsonify

app=Flask(__name__)
obj = ChatWithSql("root","root","localhost","d1")

@app.route('/')
def home():
    return jsonify({"message": "Hello from SQL Chat Bot!"})

@app.route('/send-message',methods=['GET'])
def send_message():

    message=obj.message("How many tables rae there in the database")
    return jsonify({"message":message})

if __name__=='__main__':
    app.run(debug=True,port=5000)



