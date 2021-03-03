#!/usr/local/Python-3.7/bin/python

import pymysql
import sys
import cgi
import mysql.connector

import cgitb
cgitb.enable()


connection = pymysql.connect(host="bioed.bu.edu", user="daisyhan", password="daisyhan", db="groupA", port=4253)
cursor = connection.cursor()

# print content-type
print("Content-type: text/html\n")
print("<html><head><title>Mosquito Transposon Database</title></head>")

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

#Jumbotron Header
print('''<div class="container">
		<div class="jumbotron text-center">
			<h1><span class="glyphicon glyphicon-search" aria-hidden="true"></span> Mosquito Transposon Database</h1>
			<p>Student Creators: Daisy Han, Simran Makwana, Nicholas Mosca, Evie Wan</p>
			<small>This database was developed as a BF768 Final Project Spring 2020, in affiliation with Dr. Nelson Lau, under the supervision of Dr. Gary Benson.<br/></small>
			<hr></hr>
			<small class="text-muted">The objective of our project is to create a database to classify transposable elements within four closely related mosquito species. Doing so will help achieve the biological goal of comparing transposons between species by percent abundance, and more.
			Mosquitos are known to be one of the most dangerous disease carrying vectors on earth. Among closely related species, their genome size can vary from .28 Gigabases (GB) to 2.54 (GB).  Despite large differences in genome size, variance in number of genes is small. It is unclear as to why mosquito genome sizes vary so much between species yet still seem to code for similar genes.
	Investigating transposable elements may provide insight on these differences. Transposable elements are DNA sequences that can change position within the genome, which may lead to mutations in the host genome. Differences in transposable element distribution within related mosquito species may explain differences in genome size. Understanding the large difference in genome sizes among species could give valuable insight to the evolution and integration of transposons.</small>
		</div>''')

#Links to search pages
print('''
	<div class="row">
		<div class="col-lg-3 col-sm-6">
			<div class="card mb-4 box-shadow thumbnail text-center">
				<img class="card-img-top" data-src="holder.js/100px225? theme-thumb&bg=55595c&fg=eceeef&text=Thumbnail" alt="Thumbtail [100%x225]" src = "https://images.unsplash.com/photo-1572262086204-3909bfc93ea0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80" data-holder-renedered="true">
				<div class="card-body">
					<h6 class="lead">Search Species</h6>
					<p class="card-text">This database contains information on four species of mosquitos. To return transposon class, order and superfamily distributions by species, search here.</p>
				<div class="d-flex justify-content-between align-items-center">
					<div class="btn-group">
						<button type="button" class="btn btn-sm btn-outline-secondary"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_copy.py">Search</a></button>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="col-lg-3 col-sm-6">
		<div class="card mb-4 box-shadow thumbnail text-center">
			<img class="card-img-top" data-src="holder.js/100px225? theme-thumb&bg=55595c&fg=eceeef&text=Thumbnail" alt="Thumbtail [100%x225]" src = "https://images.unsplash.com/photo-1574170609519-d1d8d4b71f60?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80" data-holder-renedered="true">
			<div class="card-body">
				<h6 class="lead">Search Transposon Class</h6>
				<p class="card-text">This database contains transposons of Class I (Retroposons) and Class II (DNA Transposons). To see a summary of transposons by class, search here.</p>
				<div class="d-flex justify-content-between align-items-center">
				<div class="btn-group">
					<button type="button" class="btn btn-sm btn-outline-secondary"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/webpage_evie.py">Search</a></button>
				</div>
			</div>
		</div>
	</div>
	</div>
<div class="col-lg-3 col-sm-6">
		<div class="card mb-4 box-shadow thumbnail text-center">
			<img class="card-img-top" data-src="holder.js/100px225? theme-thumb&bg=55595c&fg=eceeef&text=Thumbnail" alt="Thumbtail [100%x225]" src = "https://images.unsplash.com/photo-1453847668862-487637052f8a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1355&q=80" data-holder-renedered="true">
			<div class="card-body">
				<h6 class="lead">Search Transposon Order</h6>
				<p class="card-text">This database contains twelve different transposon orders, such as LINE or SINE. To see a summary of transposons by order, search here.</p>
				<div class="d-flex justify-content-between align-items-center">
				<div class="btn-group">
					<button type="button" class="btn btn-sm btn-outline-secondary"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/transposon_order_page.py">Search</a></button>
				</div>
			</div>
		</div>
	</div>
	</div>
	<div class="col-lg-3 col-sm-6">
		<div class="card mb-4 box-shadow thumbnail text-center">
			<img class="card-img-top" data-src="holder.js/100px225? theme-thumb&bg=55595c&fg=eceeef&text=Thumbnail" alt="Thumbtail [100%x225]" src = "https://images.unsplash.com/photo-1575909492048-9df0a4e121fb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80" data-holder-renedered="true">
			<div class="card-body">
				<h6 class="lead">Browse All Data</h6>
				<p class="card-text">To browse all entries in the database, including original FASTA header information, click here. Individual filters can be applied to narrow search results.</p>
				<div class="d-flex justify-content-between align-items-center">
				<div class="btn-group">
					<button type="button" class="btn btn-sm btn-outline-secondary"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupA/explore.py">Explore</a></button>
				</div>
			</div>
		</div>
	</div>
	</div>

</div>''')

#CSS Links
print('''<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">''')

# Bootstrap and JQuery
print('''<script src="https://code.jquery.com/jquery-2.1.4.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>''')
print("</body></html>")
