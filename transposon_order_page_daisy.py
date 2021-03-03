#!/usr/local/Python-3.7/bin/python

import pymysql
import sys
import cgi
import mysql.connector

import cgitb
cgitb.enable()

# convert names to scientific notation
def scinot(name):
    return('<i>' + name[0].upper() + name[1:].lower() + '</i>')
def scinot_noital(name):
    return(name[0].upper() + name[1:].lower())

connection = pymysql.connect(host="bioed.bu.edu", user="daisyhan", password="daisyhan", db="groupA", port=4253)
cursor = connection.cursor()

# print content-type
print("Content-type: text/html\n")
print("<html><head><title>Search By Order</title></head>")

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
      <h1 class="display-1 text-center">Search By Transposon Order</h1>
    </div>
  </div>
  ''')

#Create form
print('''
  <div class="container">
  <form name="input_order" action="https://bioed.bu.edu/cgi-bin/students_20/groupA/transposon_order_page.py" method="get">
  <div class="form-group">
    <label for= "input_order">Search By Transposon Order </label>
    <div class="frmSearch">
      <input type="text" id = "input_order" name="input_order" class="form-control" placeholder="LINE | SINE | LTR" required>
      <div id="suggesstion-box"></div>
      <hr>
      <small id="input_help" class="form-text text-muted">RNA Transposons are divided into five orders: Long Terminal Repeat (LTR) retrotransposons, DIRS-like elements, Penelope-like elements (PLEs), LINEs (long interspersed elements), and SINEs (short interspersed elements). <br>
       DNA transposons are divided into four orders: CMC, Crypton, Helitron, and Maverick. <br>
      To search for a particular transposable element within this database, begin typing in the search box. The orders present will autopopulate in the drop-down bar as you type.</small>
    </div>
  </div>
  <input type="submit" name="submit" class="btn btn-primary">
  </form>
  </div>''')

# Get the Form
form = cgi.FieldStorage()
input_order = form.getvalue("input_order")

# Javascript Ajax Stuff
print('''<script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  <script type = "text/javascript">
  $(document).ready(function(){
    $("#input_order").keyup(function(){
      $.ajax({
      type: "POST",
      url: "transposon_order_page_ajax.py",
      data:'input_order='+$(this).val(),
      beforeSend: function(){
        $("#input_order").css("background","#FFF url(LoaderIcon.gif) no-repeat 165px");
      },
      success: function(data){
        $("#suggesstion-box").show();
        $("#suggesstion-box").html(data);
        $("#input_order").css("background","#FFF");
      }
    });
  });
});

function selectOrder(val) {
  $("#input_order").val(val);
  $("#suggesstion-box").hide();
}
</script>''')

#All SQL Queries
#List of all orders, and respective counts
query1 = '''
  SELECT myorder, count(*)
  FROM species JOIN transposon_relationship ON sid = species_id
  GROUP BY myorder
  '''
#Orders by species
query2 = '''
  SELECT species_name, myorder, count(*) AS 'Order By Species'
  FROM species JOIN transposon_relationship ON sid = species_id
  GROUP BY myorder, sid
  ORDER BY species_name ASC, myorder ASC;
  '''

  #Specific Order By Species
query3 = """
    SELECT species_name, myorder, count(*) AS 'Order By Species'
    FROM species JOIN transposon_relationship ON sid = species_id
    WHERE myorder = '%s'
    GROUP BY sid;
  """%(input_order)


#If order is entered

if input_order:

  #Query 1
  print("<div class='container'>")
  print("<h3>Order Summary Information</h3>")
  print('''<table id ="query1_table" class="table">
        <tr>
          <th scope="col">Order Name</th>
          <th scope="col">Order Count</th>
        </tr>''')
  cursor.execute(query1)
  records_1 = cursor.fetchall()
  transposon_order = []
  order_count = []
  for row in records_1:
    print("<tr><td>%s</td><td>%s</td></tr>" % (row[0], row[1]))
    transposon_order.append(row[0])
    order_count.append(row[1])
  orderdata = list(zip(transposon_order, order_count))
  orderdata = [list(tuple) for tuple in orderdata]
  orderdata = [['Transposon Order', 'Count']] + orderdata
  print("<div id= 'order_chart'></div>")
  print('</div>')

  #Query 2
  print("<div>")
  print('<div class="col-md-6 col-lg-6">')
  print('''<table id ="query2_table" class="table"><h3>Order By Species</h3>
        <tr>
          <th scope="col">Species Name</th>
          <th scope="col">Order Name</th>
          <th scope="col">Number Within Order Per Species</th>
        </tr>''')
  cursor.execute(query2)
  records_2 = cursor.fetchall()
  for row in records_2:
    print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (scinot(row[0]), row[1], row[2]))
  print('</div>')

  #Query 3
  print("<div>")
  print('''<table id ="query3_table" class="table"><h3>Order By Species For %s</h3>'''%input_order)
  print('''
        <tr>
          <th scope="col">Species Name</th>
          <th scope="col">Order Name</th>
          <th scope="col">Number Within Order Per Species</th>
        </tr>''')
  cursor.execute(query3)
  records_3 = cursor.fetchall()
  transposon_order_3 = []
  order_count_3 = []
  for row in records_3:
    print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (scinot(row[0]), row[1], row[2]))
    transposon_order_3.append(scinot_noital(row[0]))
    order_count_3.append(row[2])
  orderdata_3 = list(zip(transposon_order_3, order_count_3))
  orderdata_3 = [list(tuple) for tuple in orderdata_3]
  orderdata_3 = [['Transposon Order', 'Count']] + orderdata_3
  print("<div id= 'order_chart_3'></div>")
  print('</div>')
  print('</div></div></div>')


  # #Charts
  print("""<script type = 'text/javascript' src = 'https://www.gstatic.com/charts/loader.js'></script>
         <script type = 'text/javascript'>
            google.charts.load('current', {
                'packages' : ['corechart']});
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {
              var data = google.visualization.arrayToDataTable(%s);
              var chart = new google.visualization.PieChart(document.getElementById('order_chart'));
              chart.draw(data);
            };
          </script>""" %(orderdata))
  print("""<script type = 'text/javascript' src = 'https://www.gstatic.com/charts/loader.js'></script>
         <script type = 'text/javascript'>
            google.charts.load('current', {
                'packages' : ['corechart']});
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {
              var data = google.visualization.arrayToDataTable(%s);
              var chart = new google.visualization.PieChart(document.getElementById('order_chart_3'));
              chart.draw(data);
            };
          </script>""" %(orderdata_3))

#CSS Links
print('''<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">''')

# Bootstrap and JQuery
# Bootstrap and JQuery
print('''<script src="https://code.jquery.com/jquery-2.1.4.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>''')
print("</body></html>")
print("</body></html>")
