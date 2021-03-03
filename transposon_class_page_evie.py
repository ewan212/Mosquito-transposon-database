#!/usr/local/Python-3.7/bin/python

import pymysql
import sys
import cgi
import mysql.connector

import cgitb
cgitb.enable()

# print content-type
print("Content-type: text/html\n")
print("<html>")
print("<title>Search By Class</title>")


connection = pymysql.connect(host="bioed.bu.edu", user="ewan212", password="ewan212", db="groupA", port=4253)
cursor = connection.cursor()


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



#form
print('''
</header>
<div class="page-content" style="background-image: url('')">
        <div class="browser-box">
        <div class="jumbotron jumbotron-fluid">
          <div class="container">
            <h1><center>Search By Transposon Class</center></h1>
          </div>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-sm-4 col-lg-6">

                    <div class="input-group">
                        <form id="singleSearchForm" action="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_evie.py" method="post">
                            <div>
                            <label for = "class">Search By Transposon Class: </label>
                            <select name='class.dropdown' id=searchbar>
                            <option class="dropdown-item">DNA</option>
                            <option class="dropdown-item">RNA</option>
                            <option class="dropdown-item">Other</option>
                            </select>
                            </div>
                            <input type='submit' value='Search' class="btn btn-primary">

                  </div>
                    <br><small>Class I: retrotransposons (RNA) </small></br>
                    <br><small>Class II: DNA Transposons </small></br>
                    <br><small>Others indicate the transposons that we were not able to classify.</small></br>
                  </div>


                </form>




                <div class="col-md-6 col-lg-4">

                    <div class="graphs">
                        <div id= "piechart_order"; style="width: 500px; height: 300px;"></div>
                        <div id= "piechart_fam"; style="width: 500px; height: 300px;"></div>

                    </div>





                </div>
            </div>
        </div>
</div>
<header>
''')






print('''
<script type="text/javascript">
function checkInput() {
    var search = document.getElementById('searchbar').value;


    if (search !== "DNA") {
        alert("Please select a Transposon Class.");
        return false;
    }

	else{
		return true;
	}

}
</script>
''')



#Store Values
form = cgi.FieldStorage()

#Set Variable
transposon_class = form.getvalue("class.dropdown")
#print("<div class='container'><h3>%s Transposon Class Information</h3></div>" %transposon_class)



query_order = '''SELECT class, myorder, count(*)
             FROM species JOIN transposon_relationship on species_id = sid JOIN demo_transposon on transposon_id = tid
             group by myorder
             having class = '%s';''' %(transposon_class)

query_superfam = '''SELECT class, superfamily, count(*)
             FROM species JOIN transposon_relationship on species_id = sid JOIN demo_transposon on transposon_id = tid
             group by superfamily
             having class = '%s';''' %(transposon_class)

query_all = '''SELECT class, superfamily, header
            FROM transposon_relationship JOIN demo_transposon on transposon_id = tid
            where class = '%s';'''%(transposon_class)




if form:


    #query values
    cursor.execute(query_order)
    order_dt = cursor.fetchall()
    cursor.execute(query_superfam)
    fam_dt = cursor.fetchall()
    cursor.execute(query_all)
    all_data = cursor.fetchall()


    #order
    t_order = []
    order_count = []

  
    print('''<table id="table1" class="table">
                <th scope="col">Transposon Order</th>
                <th scope="col">Count</th>
            ''')

    for r in order_dt:

      print("<tr><td>%s</td><td>%s</td></tr>" %(r[1], r[2]))
      t_order.append(r[1])
      order_count.append(r[2])
    combined = list(zip(t_order, order_count))
    combined = [['Transposon Order', 'Count']] + list(list(i) for i in combined)


    #superfam
    t_superfam = []
    fam_count = []

    print('''<table id="table2" class="table">
          <th scope="col">Transposon Superfamily</th>
          <th scope="col">Count</th>
      ''')


    for r in fam_dt:

      print("<tr><td>%s</td><td>%s</td></tr>" %(r[1], r[2]))
      t_superfam.append(r[1])
      fam_count.append(r[2])
    famCombined = list(zip(t_superfam, fam_count))
    famCombined = [['Transposon Superfamily', 'Count']] + list(list(i) for i in famCombined)


    #table all
    print('''<table id="table3" class="table">
      <th scope="col">Transposon Class</th>
      <th scope="col">Transposon Superfamily</th>
      <th scope="col">Transposon Header</th>
       ''')

    for r in all_data:
      print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(r[0], r[1], r[2]))




    #piechart for order
    print("""<script type = 'text/javascript' src = 'https://www.gstatic.com/charts/loader.js'></script>
         <script type = 'text/javascript'>
          google.charts.load('current', {'packages' : ['corechart']});
          google.charts.setOnLoadCallback(drawChart);


          function drawChart() {
            var data = google.visualization.arrayToDataTable(%s);

            var options = {title: '%s Transposon Order Distribution'};


            var chart = new google.visualization.PieChart(document.getElementById('piechart_order'));
            chart.draw(data, options)
          };
        </script>""" %(combined, transposon_class))



    #piechart for superfamily
    print("""<script type = 'text/javascript' src = 'https://www.gstatic.com/charts/loader.js'></script>
         <script type = 'text/javascript'>
          google.charts.load('current', {'packages' : ['corechart']});
          google.charts.setOnLoadCallback(drawChart);


          function drawChart() {
            var data = google.visualization.arrayToDataTable(%s);

            var options = {
                title: '%s Transposon Superfamily Distribution',
                is3D: true,
            };
            var chart = new google.visualization.PieChart(document.getElementById('piechart_fam'));
            chart.draw(data, options)
          }
        </script>""" %(famCombined, transposon_class))


      #chart for length











#DL test
#var = 'download dis'

# print('''<a id="download_link" download="my_exported_file.txt" href=”” >Download as Text File</a>
#          <script>
#           var text = '%s';
#           var data = new Blob([text], {type: 'text/plain'});
#           var url = window.URL.createObjectURL(data);
#           document.getElementById('download_link').href = url;
#           </script>''' %(var))










print('</div>')
# Bootstrap and JQuery
print('''<script src="https://code.jquery.com/jquery-2.1.4.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>''')
print("</body></html>")
