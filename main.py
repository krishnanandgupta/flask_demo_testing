from flask import Flask,render_template,request,jsonify

app= Flask(__name__)
@app.route("/test",methods=['GET','POST'])
def test():
    #x=request.json['a']
    #=request.json['b']
    return "<h1> This is a flask application </h1>"
if __name__ == '__main__':
    app.run()