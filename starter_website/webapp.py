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

        return redirect('/browse_actor')

#the app for deleting one actor in a specific row
@webapp.route('/delete_actor/<int:id>')
def delete_actor(id):
    '''deletes a actor with the given id'''
    print ('delete a actor')
    db_connection = connect_to_database()
    query = "DELETE FROM actor WHERE actor_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)

    return redirect('/browse_actor')

#display update form and process any updates, using the same function
@webapp.route('/update_actor/<int:id>', methods=['POST','GET'])
def update_actor(id):
    print('update a actor')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        actor_query = 'SELECT actor_id, fname, lname from actor WHERE actor_id = %s'  % (id)
        actor_result = execute_query(db_connection, actor_query).fetchone()

        if actor_result == None:
            return "No such person found!"

        print('Returning the update html page')
        return render_template('actor_update.html', actor = actor_result)
    elif request.method == 'POST':
        print('The POST request')
        actor_id = request.form['actor_id']
        fname = request.form['fname']
        lname = request.form['lname']


        query = "UPDATE actor SET fname = %s, lname = %s WHERE actor_id = %s"
        data = (fname,lname,actor_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_actor')

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

        query = "SELECT fname, lname, actor_id from actor WHERE fname = %s and lname = %s ;"
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
        return redirect('/browse_director')

#the app for deleting one actor in a specific row
@webapp.route('/delete_director/<int:id>')
def delete_director(id):
    '''deletes a actor with the given id'''
    print ('delete a director')
    db_connection = connect_to_database()
    query = "DELETE FROM director WHERE director_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('/browse_director')

#display update form and process any updates, using the same function
@webapp.route('/update_director/<int:id>', methods=['POST','GET'])
def update_director(id):
    print('update a director')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        director_query = 'SELECT director_id, fname, lname from director WHERE director_id = %s'  % (id)
        director_result = execute_query(db_connection, director_query).fetchone()

        if director_result == None:
            return "No such person found!"

        print('Returning the update html page')
        return render_template('director_update.html', director = director_result)
    elif request.method == 'POST':
        print('The POST request')
        director_id = request.form['director_id']
        fname = request.form['fname']
        lname = request.form['lname']


        query = "UPDATE director SET fname = %s, lname = %s WHERE director_id = %s"
        data = (fname,lname,director_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_director')

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

        query = "SELECT  fname, lname, director_id from director WHERE fname = %s and lname = %s ;"
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
    query = "SELECT movie.movie_id, title, release_date, director.fname, director.lname from movie left JOIN movie_direct on movie.movie_id = movie_direct.movie_id left JOIN director on movie_direct.director_id = director.director_id;"
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
        return redirect('/browse_movie')
#the app for deleting one actor in a specific row
@webapp.route('/delete_movie/<int:id>')
def delete_movie(id):
    '''deletes a actor with the given id'''
    print ('delete a movie')
    db_connection = connect_to_database()
    query = "DELETE FROM movie WHERE movie_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('/browse_movie')

@webapp.route('/update_movie/<int:id>', methods=['POST','GET'])
def update_movie(id):
    print('update a movie')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        movie_query = 'SELECT movie_id, title, release_date from movie WHERE movie_id = %s'  % (id)
        movie_result = execute_query(db_connection, movie_query).fetchone()

        if movie_result == None:
            return "No such movie found!"

        print('Returning the update html page')
        return render_template('movie_update.html', movie = movie_result)
    elif request.method == 'POST':
        print('The POST request')
        movie_id = request.form['movie_id']
        title = request.form['title']
        release_date = request.form['release_date']


        query = "UPDATE movie SET title = %s, release_date = %s WHERE movie_id = %s"
        data = (title,release_date,movie_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_movie')

#the app for searching a movie with user's input
@webapp.route('/search_movie', methods=['POST','GET'])
def search_movie():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('movie_search.html')
    elif request.method == 'POST':
        print("found the movie")
        title = request.form['title']
        query = "SELECT movie.movie_id, title, release_date, director.fname, director.lname from movie left JOIN movie_direct on movie.movie_id = movie_direct.movie_id left JOIN director on movie_direct.director_id = director.director_id WHERE title = %s;"
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
    query = "SELECT movie_cast.movie_id, movie_cast.actor_id, title,fname,lname,role FROM actor JOIN movie_cast ON actor.actor_id=movie_cast.actor_id JOIN movie ON movie_cast.movie_id=movie.movie_id;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('movie_cast_browse.html', rows=result)

#the app for adding a new movie_cast relationship into database
@webapp.route('/add_new_movie_cast', methods=['POST','GET'])
def add_new_movie_cast():
    db_connection = connect_to_database()
    if request.method == 'GET':
        actor_query= "SELECT actor.actor_id, actor.fname,actor.lname FROM actor;"
        movie_query= "SELECT movie.movie_id, movie.title FROM movie;"
        actorList = execute_query(db_connection, actor_query).fetchall()
        movieList = execute_query(db_connection, movie_query).fetchall()
        print (actorList)
        print (movieList)
        return render_template('movie_cast_add_new.html', actors = actorList, movies = movieList)
    elif request.method == 'POST':
        print("add a movie cast relationship!")
        actor_id = request.form['actor_id']
        movie_id = request.form['movie_id']
        role = request.form['role']
        query = 'INSERT INTO `movie_cast`(`actor_id`, `movie_id`, `role`) VALUES (%s,%s,%s)'
        data = (actor_id,movie_id,role)
        execute_query(db_connection, query, data)
        return redirect('/browse_movie_cast')

#the app for deleting one movie_cast relationship in a specific row
@webapp.route('/delete_movie_cast/(<int:mid>,<int:aid>)')
def delete_movie_cast(mid,aid):
    '''deletes a actor with the given id'''
    print ('delete a movie_cast relationship')
    db_connection = connect_to_database()
    query = "DELETE FROM movie_cast WHERE movie_id = %s AND actor_id = %s;"
    data = (mid,aid)
    print(data)

    result = execute_query(db_connection, query, data)
    return redirect('/browse_movie_cast')




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

        query = "SELECT movie_cast.movie_id, movie_cast.actor_id, title,fname,lname,role FROM actor JOIN movie_cast ON actor.actor_id=movie_cast.actor_id JOIN movie ON movie_cast.movie_id=movie.movie_id WHERE fname = %s and lname = %s"
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


        query = "SELECT movie_cast.movie_id, movie_cast.actor_id, title,fname,lname,role FROM actor JOIN movie_cast ON actor.actor_id=movie_cast.actor_id JOIN movie ON movie_cast.movie_id=movie.movie_id WHERE title = %s"
        data = (title,)
        result = execute_query(db_connection, query, data).fetchall()
        print(result)
        return render_template('movie_cast_browse.html', rows=result)
