from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#the index page for the project
@webapp.route('/')
def index():
    return render_template('index.html')


#the app for browsing all the  actors in the database
@webapp.route('/browse_actor')
#the name of this function is just a cosmetic thing
def browse_actor():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, actor_id from actor;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('actor_browse.html', rows=result)

#the app for adding a new actor into the database
@webapp.route('/add_new_actor', methods=['POST','GET'])
def add_new_actor():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('actor_add_new.html')
    elif request.method == 'POST':
        print("Add new people!")
        fname = request.form['fname']
        lname = request.form['lname']

        query = 'INSERT INTO actor (fname, lname) VALUES (%s,%s);'
        data = (fname, lname)
        execute_query(db_connection, query, data)
        return ('actor added!')

#the app for deleting one actor in a specific row
@webapp.route('/delete_actor/<int:id>')
def delete_actor(id):
    '''deletes a actor with the given id'''
    print ('delete a actor')
    db_connection = connect_to_database()
    query = "DELETE FROM actor WHERE actor_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")

#the app for searching one specific actor from user's input
@webapp.route('/search_actor', methods=['POST','GET'])
def search_actor():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('actor_search.html')
    elif request.method == 'POST':
        print("found the actor!")
        fname = request.form['fname']
        lname = request.form['lname']

        query = "SELECT actor_id, fname, lname from actor WHERE fname = %s and lname = %s ;"
        data = (fname,lname)
        result = execute_query(db_connection, query, data).fetchall()
        print(result)
        return render_template('actor_browse.html', rows=result)


#the app for browsing all the directors in the database
@webapp.route('/browse_director')
#the name of this function is just a cosmetic thing
def browse_director():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, director_id from director;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('director_browse.html', rows=result)

#the app for adding a new director into database
@webapp.route('/add_new_director', methods=['POST','GET'])
def add_new_director():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('director_add_new.html')
    elif request.method == 'POST':
        print("Add new director!")
        fname = request.form['fname']
        lname = request.form['lname']

        query = 'INSERT INTO director (fname, lname) VALUES (%s,%s)'
        data = (fname, lname)
        execute_query(db_connection, query, data)
        return ('director added!')

#the app for deleting one actor in a specific row
@webapp.route('/delete_director/<int:id>')
def delete_director(id):
    '''deletes a actor with the given id'''
    print ('delete a director')
    db_connection = connect_to_database()
    query = "DELETE FROM director WHERE director_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")

#the app for searching a director from user's input
@webapp.route('/search_director', methods=['POST','GET'])
def search_director():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('director_search.html')
    elif request.method == 'POST':
        print("found the director!")
        fname = request.form['fname']
        lname = request.form['lname']

        query = "SELECT director_id, fname, lname from director WHERE fname = %s and lname = %s ;"
        data = (fname,lname)
        result = execute_query(db_connection, query, data).fetchall()
        print(result)
        return render_template('director_browse.html', rows=result)

#the app for browsing movies in the database
@webapp.route('/browse_movie')
#the name of this function is just a cosmetic thing
def browse_movie():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT movie_id, title, release_date from movie;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('movie_browse.html', rows=result)
#the app for adding a new movie into database
@webapp.route('/add_new_movie', methods=['POST','GET'])
def add_new_movie():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('movie_add_new.html')
    elif request.method == 'POST':
        print("Add new movie!")
        title = request.form['title']
        release_date = request.form['release_date']

        query = 'INSERT INTO movie (title, release_date) VALUES (%s,%s)'
        data = (title, release_date)
        execute_query(db_connection, query, data)
        return ('movie added!')
#the app for searching a movie with user's input
@webapp.route('/search_movie', methods=['POST','GET'])
def search_movie():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('movie_search.html')
    elif request.method == 'POST':
        print("found the movie")
        title = request.form['title']
        query = "SELECT movie_id, title, release_date from movie WHERE title = %s;"
        data = (title,)
        result = execute_query(db_connection, query, data).fetchall()
        print(result)
        return render_template('movie_browse.html', rows=result)

#the app for browsing all the movie_cast relationship in the database
@webapp.route('/browse_movie_cast')
#the name of this function is just a cosmetic thing
def browse_movie_cast():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT title,fname,lname,role FROM actor JOIN movie_cast ON actor.actor_id=movie_cast.actor_id JOIN movie ON movie_cast.movie_id=movie.movie_id;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('movie_cast_browse.html', rows=result)
#the app for searching a actor in the movie cast table
@webapp.route('/search_actor_movie_cast', methods=['POST','GET'])
def search_movie_cast():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('movie_cast_actor_search.html')
    elif request.method == 'POST':
        print("found the actor in movie_cast")
        fname = request.form['fname']
        lname = request.form['lname']

        query = "SELECT title,fname,lname,role FROM actor JOIN movie_cast ON actor.actor_id=movie_cast.actor_id JOIN movie ON movie_cast.movie_id=movie.movie_id WHERE fname = %s and lname = %s"
        data = (fname,lname)
        result = execute_query(db_connection, query, data).fetchall()
        print(result)
        return render_template('movie_cast_browse.html', rows=result)

#the app for searching a movie in the movie cast table
@webapp.route('/search_movie_movie_cast', methods=['POST','GET'])
def search_movie_movie_cast():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('movie_cast_movie_search.html')
    elif request.method == 'POST':
        print("found the movie in movie_cast")
        title = request.form['title']


        query = "SELECT title,fname,lname,role FROM actor JOIN movie_cast ON actor.actor_id=movie_cast.actor_id JOIN movie ON movie_cast.movie_id=movie.movie_id WHERE title = %s"
        data = (title,)
        result = execute_query(db_connection, query, data).fetchall()
        print(result)
        return render_template('movie_cast_browse.html', rows=result)





#display update form and process any updates, using the same function
@webapp.route('/update_people/<int:id>', methods=['POST','GET'])
def update_people(id):
    print('In the function')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        people_query = 'SELECT id, fname, lname, homeworld, age from bsg_people WHERE id = %s'  % (id)
        people_result = execute_query(db_connection, people_query).fetchone()

        if people_result == None:
            return "No such person found!"

        planets_query = 'SELECT id, name from bsg_planets'
        planets_results = execute_query(db_connection, planets_query).fetchall()

        print('Returning')
        return render_template('people_update.html', planets = planets_results, person = people_result)
    elif request.method == 'POST':
        print('The POST request')
        character_id = request.form['character_id']
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = "UPDATE bsg_people SET fname = %s, lname = %s, age = %s, homeworld = %s WHERE id = %s"
        data = (fname, lname, age, homeworld, character_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_bsg_people')
