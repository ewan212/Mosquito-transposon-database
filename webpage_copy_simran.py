#!/usr/local/Python-3.7/bin/python

import pymysql as pms
import sys
import cgi
import mysql.connector

import cgitb
cgitb.enable()


# print content-type
print("Content-type: text/html\n")
print("<html>")
print("<title>Search By Species</title>")

#Navbar
print('''<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">''')
print('''<nav class="navbar navbar-inverse">
        <div class="container">
        <ul class="nav navbar-nav">
        <li class="navbar-nav"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_draft_1.py"><span class="glyphicon glyphicon-home" aria-hidden="true"></a></li>
        <li><a href="#">About</a></li>
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
        <li><a href="https://www.bumc.bu.edu/biochemistry/profiles/nelson-lau/">Lau Laboratory</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Additional Resources <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
          </ul>
        </li>
      </ul>
    </div>
        </div>
    </nav>
    ''')

#Jumbotron Header
print('''<div class="container">
        <div class="jumbotron">
            <h1><span class="glyphicon glyphicon-search" aria-hidden="true"></span> Mosquito Transposon Database</h1>
            <p>Daisy Han, Simran Makwana, Nick Mosca, Evie Wan</p>
        </div>''')

#CSS Links
print('''<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">''')

# style for Form fill and table
# print('''<style>
# body{width=device-width;}
# .frmSearch {border: 5px solid #474646;background-color: #ffffff;margin: 10px 10px;padding:20px;border-radius:30px;}
# #namelist{float:left;list-style:none;margin-top:-3px;padding:0;width:190px;position: absolute;}
# #namelist li{padding: 10px; background: #ffffff; border-bottom: #474646 5px solid;}
# #namelist li:hover{background:#dbdbdb;cursor: pointer;}
# #search-box{padding: 10px;border: #c71677  5px solid;border-radius:4px;}

# table.w3-table-all{border: 5px solid #474646;background-color: #ffffff;margin: 10px 10px;padding:20px;border-radius:30px;}

# table.charts{border: 5px solid #474646;}
# </style>
# ''')


# start connection sql
connection = pms.connect(host="bioed.bu.edu", user="makwana", password="makwana", db="groupA", port=4253)
cursor = connection.cursor()

#Print Form
print('''<form action="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_copy.py" method="GET">
    <h3>Search by Species</h3>

    <script src="https://code.jquery.com/jquery-2.1.1.min.js" type="text/javascript"></script>
    <script>
    $(document).ready(function(){
        $("#speciesname").keyup(function(){
            $.ajax({
            type: "POST",
            url: "webpage_copy_check.py",
            data:'keyword='+$(this).val(),
            beforeSend: function(){
                $("#speciesname").css("background","#FFF url(LoaderIcon.gif) no-repeat 165px");
            },
            success: function(data){
                $("#suggest").show();
                $("#suggest").html(data);
                $("#speciesname").css("background","#FFF");
            }
            });
        });
    });
    function selectName(val) {
    $("#speciesname").val(val);
    $("#suggest").hide();
    }

</script>
<body><div class="frmSearch">
<form action='https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_copy.py' method='POST'>
<input type='text' name='speciesname' id = 'speciesname' placeholder = 'species'>
<input type='submit' value='Search'> </form>
<div id="suggest"></div></div>
</body></div>

''')


# get the form
form = cgi.FieldStorage()

# css template for table
print('''<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">''')
print('''<div class="w3-container">''')


if form:
    speciesname = form.getvalue("speciesname")

    print("<h2>results: ", speciesname, "</h2>")

    ##### pie chart of class distribution
    #generate a list of lists [class, #]
    query = "select class, count(*) from transposon_relationship join species on (sid = species_id) where species_name = '" + speciesname + "' group by class;"
    cursor.execute(query)
    results = cursor.fetchall()
    transposon_class = ['class']
    class_count = ['count']
    for r in results:
        transposon_class.append(r[0])
        class_count.append(r[1])
    classdata = list(zip(transposon_class, class_count))
    classdata = [list(i) for i in classdata]

    ##### pie chart of order distribution
    #generate a list of lists [order, #]
    query = "select myorder, count(*) from transposon_relationship join species on (sid = species_id) where species_name = '" + speciesname + "' group by myorder;"
    cursor.execute(query)
    results = cursor.fetchall()
    transposon_order = ['order']
    order_count = ['count']
    for r in results:
        transposon_order.append(r[0])
        order_count.append(r[1])
    orderdata = list(zip(transposon_order, order_count))
    orderdata = [list(i) for i in orderdata]

    ##### pie chart of superfamily distribution
    #generate a list of lists [superfamily, #]
    query = "select superfamily, count(*) from transposon_relationship join species on (sid = species_id) where species_name = '" + speciesname + "' group by superfamily;"
    cursor.execute(query)
    results = cursor.fetchall()
    transposon_superfamily = ['superfamily']
    superfamily_count = ['count']
    for r in results:
        transposon_superfamily.append(r[0])
        superfamily_count.append(r[1])
    superfamilydata = list(zip(transposon_superfamily, superfamily_count))
    superfamilydata = [list(i) for i in superfamilydata]

    ##### histogram of length distribution
    #generate a list of lengths
    query = "select length from transposon_relationship join species on (sid = species_id) where species_name = '" + speciesname + "' ;"
    cursor.execute(query)
    results = cursor.fetchall()
    lengths = ['length']
    len_name = ['transposon length']
    for r in results:
        lengths.append(r[0])
        len_name.append('transposon length')
    lengthdata = list(zip(lengths, len_name))
    lengthdata = [list(i) for i in lengthdata]

    print('''
    <html>
      <head>

        <!--Load the google charts-->
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">


          google.charts.load('current', {'packages':['corechart']});
          google.charts.setOnLoadCallback(drawClassChart);
          google.charts.setOnLoadCallback(drawOrderChart);
          google.charts.setOnLoadCallback(drawSuperfamilyChart);
          google.charts.setOnLoadCallback(drawLengthChart);

          function drawClassChart() {
            var data = google.visualization.arrayToDataTable(
    ''')
    print(classdata)
    print('''
            );
            var options = {
                width: 600,
                height: 400,
                title: 'Transposon Class Distribution'
            };

            var chart = new google.visualization.PieChart(document.getElementById('class_chart'));
            chart.draw(data, options);
          }

          function drawOrderChart() {
            var data = google.visualization.arrayToDataTable(
    ''')
    print(orderdata)
    print('''
            );
            var options = {
                width: 600,
                height: 400,
                title: 'Transposon Order Distribution'
            };
            var chart = new google.visualization.PieChart(document.getElementById('order_chart'));
            chart.draw(data, options);
          }

          function drawSuperfamilyChart() {
            var data = google.visualization.arrayToDataTable(
    ''')
    print(superfamilydata)
    print('''
            );
            var options = {
                width: 600,
                height: 400,
                title: 'Transposon Superfamily Distribution'
            };
            var chart = new google.visualization.PieChart(document.getElementById('superfamily_chart'));
            chart.draw(data, options);
          }

          function drawLengthChart() {
            var data = google.visualization.arrayToDataTable(
    ''')
    print(lengthdata)
    print('''
            );
            var options = {
                width: 600,
                height: 400,
                title: 'Transposon Length Distribution',
                legend: { position: 'none' },
                histogram: { lastBucketPercentile: 5 }

            };
            var chart = new google.visualization.Histogram(document.getElementById('length_chart'));
            chart.draw(data, options);
          }

        </script>
      </head>
      <body>
        <!--Table and divs that hold the pie charts-->
        <table class="charts">
          <tr>
            <td><div id="order_chart" ></div></td>
            <td><div id="class_chart" ></div></td>
          </tr>
          <tr>
            <td><div id="superfamily_chart" ></div></td>
            <td><div id="length_chart" ></div></td>
          </tr>
        </table>
      </body>
    </html>
    ''')


    ##res
    # init table
    print('''<table class="w3-table-all">''')
    # table column names
    print('''
        <tr class="w3"> 
        <th>species</th>
        <th>header</th>
    ''')
    query = "select species_name, header from transposon_relationship join species on (sid = species_id) where species_name = '" +  speciesname + "';"
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:

        print('<tr><td>' + str(row[0]) + '</td><td>' + str(row[1]) + '</td></tr>')



    print("</table>")

print("</div>")

print("</html>")


# Bootstrap and JQuery
print('''<script src="https://code.jquery.com/jquery-2.1.4.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>''')
print("</body></html>")
