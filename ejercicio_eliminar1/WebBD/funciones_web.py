#Author: juana gutierrez
#Group: GITI9072-e
from flask import Flask, render_template, request, redirect, escape
from functions import area
import psycopg2

app = Flask(__name__)

#
def insertar_registro(l: float) -> None:
    configuracionDB = {'host': '127.0.0.1',
                           'port': '5433',
                           'user': 'postgres',
                           'password': '1234',
                           'database': 'test',}
    conexion = psycopg2.connect(**configuracionDB)
    tot = area(l)
    _SQL = ("INSERT INTO calculos(total) VALUES(%s)")
    cursor = conexion.cursor()
    cursor.execute(_SQL, (tot,))
    conexion.commit()
    cursor.close()
    conexion.close()


def delete_registros(id: int) -> None:
    """ delete part by part id """
    conn = None
    try:
        # read database configuration
        params = {'host': '127.0.0.1',
                           'port': '5433',
                           'user': 'postgres',
                           'password': '1234',
                           'database': 'test',}
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM calculos WHERE id = %s", (id,))

        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#@app.route('/')
#def hello()-> '302':
    #return redirect('/entry')

@app.route('/')
def inicio() -> '302':
    return redirect('/entry')


@app.route('/exec_equation', methods=['POST'])
def execute() -> 'html':
    l = float((request.form['l']))
    #y = int(request.form['y'])

    tot = float(area(l))
    title = 'This is the equation\'s result'
    insertar_registro(l)
    return render_template('results.html',
                           the_title=title,
                           #the_x=x,
                           the_l=l,
                           the_result=tot,)


@app.route('/delete_data', methods=['POST'])
def delete() -> 'html':
    id = int((request.form['id']))

    title = 'This is the equation\'s result'
    delete_registros(id)
    return render_template('entry.html',
                           the_title=title)


@app.route ('/entry')
def entry_page()->'html':
    return render_template('entry.html',
                           the_title='Functions in web')


@app.route('/data')
def view_data() -> 'html':
    params = {'host': '127.0.0.1',
                           'port': '5433',
                           'user': 'postgres',
                           'password': '1234',
                           'database': 'test',}
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()

    _SQL = ("SELECT * FROM calculos")
    cursor.execute(_SQL)
    rows = cursor.fetchall()
    contents = []
    for row in rows:
            contents.append(row)
    cursor.close()
    connection.close()
    titles = ('id', 'Resultado')
    return render_template('data.html',
                           the_title='calculos',
                           the_row_titles=titles,
                           the_data=contents, )

if __name__ == '__main__':
      app.run(debug=True, port=5002)

















