from flask import Flask, render_template

#Create a flask instance

app = Flask(__name__)

#Create route decorator
@app.route('/')

#def index():
#    return "<h1>Hello, Thx for visit ! - Anil Bhatt !<h1>"

# Filters
#   lower
#   upper
#   capitalize
#   safe
#   striptags
#   trim

def index():
    first_name = 'Anil'
    msg = 'Nothing is <strong>impossible !</strong>'
    favorite_places = ['Yellow_stone', 'Lake_Tahoue','Yellow_Stone','Florida','Agasthyakoodam']
    return render_template("index.html",
                           first_name=first_name,
                           message = msg,
                           favorite_places = favorite_places,
                           last_visited = favorite_places[-1])
# localhost:5000/user/Anil
@app.route('/user/<name>')
def user(name):
#   return "<h1>Hello {} !!! </h1>" .format(name)
    return render_template('user.html', user_name=name)

#Create custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500