#!/usr/local/Python-3.7/bin/python

import pymysql as pms
import sys
import cgi
import mysql.connector

import cgitb
cgitb.enable()

def scinot(name):
    return('<i>' + name[0].upper() + name[1:].lower() + '</i>')

# print content-type
print("Content-type: text/html\n")
print("<html>")
print("<title>Browse</title>")

#Navbar
print('''<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">''')
print('''<nav class="navbar navbar-inverse">
        <div class="container">
        <ul class="nav navbar-nav">
        <li class="navbar-nav"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_draft_1.py"><span class="glyphicon glyphicon-home" aria-hidden="true"></a></li>
        <li><a href="https://bioed.bu.edu/students_20/groupA/updated_about.html">About</a></li>
        <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/explore.py">Browse</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Search By <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_copy.py">Species</a></li>
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/transposon_order_page.py">Transposon Order</a></li>
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_evie.py">Transposon Class</a></li>
          </ul>
        </li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="http://www.bumc.bu.edu/biochemistry/lau-lab-2/">Lau Laboratory</a></li>
        
        <li><a href="https://bioed.bu.edu/students_20/groupA/help_page.html">Help</a></li>
      </ul>
    </div>
    </div>
</nav>
    ''')

#Header and Formatting
print('''
  <div class="jumbotron jumbotron-fluid">
    <div class="container">
      <h1 class="display-1 text-center">Browse Database</h1>
    </div>
  </div>
  ''')

# start connection sql
connection = pms.connect(host="bioed.bu.edu", user="makwana", password="makwana", db="groupA", port=4253)
cursor = connection.cursor()

# exploration table

print('''<div class="container"><table class="table">''')


print('''
    <div class="text-center">
    <h2 class="lead text-center">Explore All Uploaded Transposon Data</h2>
    <h2 class="lead text-center" style = "font-size: 1.2em">Select an entry classification (such as 'RNA') to search related transposable elements on the Dfam database</h2>
    <button type="button" class="btn btn-default"><a href="https://bioed.bu.edu/students_20/groupA/explore_results.txt" download>Download results as .txt</button>
    <button type="button" class="btn btn-default"><a href="https://bioed.bu.edu/students_20/groupA/explore_results.fa" download>Download results as .fa</button>
    <br></br>
    </div>

''')

# create output Files
t = open('/var/www/html/students_20/groupA/explore_results.txt', 'w')
t.seek(0)
t.truncate()

f = open('/var/www/html/students_20/groupA/explore_results.fa', 'w')
f.seek(0)
f.truncate()


### SPECIES DROPDOWN
print("<th scope='col'>")

query = "select distinct species_name from species;"
cursor.execute(query)
results = cursor.fetchall()

print('''
    <form id="form" action = 'https://bioed.bu.edu/cgi-bin/students_20/groupA/explore.py' method='POST'>
        <div class="form-group">
        <select id="species" name="species" class="dropdown">
            <option value="*" class="dropdown-item"> Species </option>
''')

for row in results:
    print("<option class='dropdown-item' value='" + row[0] + "'>" + row[0] + "</option>")

print('''</select></div></th>''')

### CLASS DROPDOWN
print("<th scope='col'>")

query = "select distinct class from transposon_relationship;"
cursor.execute(query)
results = cursor.fetchall()

print('''
        <label for="class"></label>
        <select id="class" name="class" class="dropdown">
            <option class='dropdown-item' value="*">Class</option>

''')

for row in results:
    print("<option class='dropdown-item' value='" + row[0] + "'>" + row[0] + "</option>")

print('''</select></th>''')

### ORDER DROPDOWN
print("<th scope='col'>")

query = "select distinct myorder from transposon_relationship;"
cursor.execute(query)
results = cursor.fetchall()

print('''
        <select id="order" name="order" class="dropdown">
            <option value="*" class='dropdown-item'>Order</option>
''')

for row in results:
    print("<option class='dropdown-item' value='" + row[0] + "'>" + row[0] + "</option>")

print('''</select></th>''')

### SUPERFAMILY DROPDOWN
print("<th scope='col'>")

query = "select distinct superfamily from transposon_relationship;"
cursor.execute(query)
results = cursor.fetchall()

print('''
        <select class='dropdown' id="superfamily" name="superfamily">
            <option class='dropdown-ite m' value="*">Superfamily</option>
''')

for row in results:
    print("<option class='dropdown-item' value='" + row[0] + "'>" + row[0] + "</option>")

print('''</select><input type="submit" id="superfamily" value="Filter" class="btn btn-primary"></th>''')

print("</form>")

### RETRIEVE DATA FROM DROP DOWNS
form = cgi.FieldStorage()
if form:
    species = form.getvalue("species")
    order = form.getvalue("order")
    myclass = form.getvalue("class")
    superfamily = form.getvalue("superfamily")

    # TABLE ROWS
    query = "select species_name, class, myorder, superfamily, header, sequence from transposon_relationship join species on (sid = species_id)"

    filter = False

    if species != '*':
        query += " where species_name = '" + species + "'"
        filter = True
    if myclass != '*':
        if filter == False:
            query += " where class = '" + myclass + "'"
            filter = True
        else:
            query += " and class = '" + myclass + "'"
    if order != '*':
        if filter == False:
            query += " where myorder = '" + order + "'"
            filter = True
        else:
            query += " and myorder = '" + order + "'"
    if superfamily != '*':
        if filter == False:
            query += " where superfamily = '" + superfamily + "'"
            filter = True
        else:
            query += " and superfamily = '" + superfamily + "'"

    query += ';'

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        specieslink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[0]) + "'</a>" + scinot(str(row[0]))
        classlink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[1]) + "'</a>" + str(row[1])
        orderlink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[2]) + "'</a>" + str(row[2])
        superfamilylink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[3]) + "'</a>" + str(row[3])
        print('<tr><td>' + specieslink + '</td><td>' + classlink + '</td><td>' + orderlink + '</td><td>' + superfamilylink + '</tf></tr>')
        t.write('>' + str(row[4]) + '\n' + str(row[5]) + '\n')
        f.write('>' + str(row[4]) + '\n' + str(row[5]) + '\n')
    t.close()
    f.close()
    print("</table>")



else:
    query = "select species_name, class, myorder, superfamily, header, sequence from transposon_relationship join species on (sid = species_id);"
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        specieslink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[0]) + "'</a>" + scinot(str(row[0]))
        classlink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[1]) + "'</a>" + str(row[1])
        orderlink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[2]) + "'</a>" + str(row[2])
        superfamilylink = "<a target='_blank'href = 'https://www.dfam.org/browse?keywords=" + str(row[3]) + "'</a>" + str(row[3])
        print('<tr><td>' + specieslink + '</td><td>' + classlink + '</td><td>' + orderlink + '</td><td>' + superfamilylink + '</tf></tr>')
        t.write('>' + str(row[4]) + '\n' + str(row[5]) + '\n')
        f.write('>' + str(row[4]) + '\n' + str(row[5]) + '\n')

    t.close()
    f.close()
    print("</table>")


print('</html>')

# Bootstrap and JQuery
print('''<script src="https://code.jquery.com/jquery-2.1.4.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>''')
print("</body></html>")
