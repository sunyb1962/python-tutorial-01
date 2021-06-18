from flask import Flask, jsonify, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>Hello, world.</h1>'

# The no. of spacing between the two parameters must be considered! 
@app.route('/home/<string:nm>   <string:nm2>')
@app.route('/home/',defaults={'nm':'my friend','nm2':'hi there'})
def home(nm,nm2):
   return '<h1>Hello {} and {}, welcome to Home Page!</h1>'.format(nm,nm2)

@app.route('/json')
def json():
#   return jsonify({'key':'value','listkeys':['This','is','a','tuple','!']})
   return {'key':'value','listkeys':['This','is','not','a','tuple','!',1,2,3,4.5]}

@app.route('/query')
def query():
   location =  request.args.get('location')
   nm = request.args.get('name')
   if nm == None or location == None:
      return '<h1>Query Page.</h1>'
   return '<h1>Query Page. {} is from {}.</h1>'.format(nm,location)

# Try using method POST or GET
#@app.route('/theform')
#def theform():
#   return '''
#      <form method='post' action='/processing'>
#         <input type='text' name='name'>
#         <input type='text' name='location'>
#         <input type='submit' value='Submit'>
#      </form>'''

#@app.route('/processing',methods=['POST','GET'])
#def processing():
#   if request.method == 'POST':
#      name = request.form['name']
#      location = request.form['location']
#   else:
#      name = request.args.get('name')
#      location = request.args.get('location')
#   return '<h2>{} from {} says hello to all. \
#   This message is sent through {}.</h2>'.format(name,location,request.method.upper())

#######################################################################################
# The following two pieces of code serve the same purpose
#######################################################################################

# Code ONE
#@app.route('/theform',methods=['POST','GET'])
#def theform():
#   if request.method == 'GET':
#      return '''
#         <form method='post' action='/theform'>
#            <input type='text' name='name'>
#            <input type='text' name='location'>
#            <input type='submit' value='Submit'>
#         </form>'''
#   elif request.method == 'POST':
#      nm = request.form['name']
#      loc = request.form['location']
#      return '<h2>{} from {} says hello to all.'.format(nm,loc)
#'''

# Code TWO
@app.route('/theform')
def theform():
   return '''
   <form method='post' action='/theform'>
      <input type='text' name='name'>
      <input type='text' name='location'>
      <input type='submit' value='Submit'>
   </form>'''

@app.route('/theform',methods=['POST'])
def processing():
   nm = request.form['name']
   loc = request.form['location']
#   return '<h2>{} from {} says hello to all.'.format(nm,loc)
   return redirect(url_for('home',nm=nm,nm2=loc))

if __name__ == '__main__':
   app.run(debug=True)

