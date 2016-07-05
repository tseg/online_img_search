# online_img_search

Installing necessary runtime libraries
Install nltk
	$sudo pip install -U nltk
	$sudo pip install -U numpy

installing 
First, update the package index (package list) in your pc.
	$sudo apt-get update 

Then use the apt-cache command to search for dependencies (missing packages). In your case:

apt-cache search libxml
apt-cache search libxml | grep dev
libxml2-dev - Development files for the GNOME XML library
...

Install it.
	$sudo apt-get install libxml2-dev

libxml2 in Ubuntu has version 2.6.31 so that's no problem.
	$apt-cache show libxml2-dev

Compilation from source needs the header files (*.h), therefore you must install the xxx-dev package. That's why I limited the listing with | grep dev. Dev package will in turn pull out all necessary runtime libraries. 

Installing dependancy file of in nlkt on python trminal(open python terminal)
	>>import nlkt
	>>nltk.download('punkt')



Runing 

sample
 
$python img_search.py  'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Raymond_Kurzweil_Fantastic_Voyage.jpg/220px-Raymond_Kurzweil_Fantastic_Voyage.jpg'
