from flask import Flask
from flask import send_file,current_app,request
import time
import os
import fire
import time
from flask_cors import CORS


os.environ['TZ']='Asia/Kolkata'
time.tzset()

app = Flask(__name__)
CORS(app)

data={}
with open("allpapers.html","r") as f:
	print("Loaded all papers site")
	allpapers=f.read()

with open("onepaper.html","r",encoding="utf-8") as f:
	print("Loaded one paper site")
	onepaper=f.read()


@app.route('/')
def home1():
	return "this site is closed due to some technical error"
#dummy
@app.route('/allPapers')
def home():
	with open("logs.txt","a") as f:
		f.write(time.strftime("%d-%m-%Y$%T")+":   Opened All Papers<br>")
	return allpapers

@app.route('/today')
def today():
	return str(os.listdir())

@app.route('/eenadu/<flid>/<flname>/<quality>', methods=['GET', 'POST'])
def download(flid,flname,quality):
	flname=flname.replace('_','-')
	if ('date' in request.args):
		date=request.args['date']
		date=date.split('/')
		date=date[1]+'-'+date[0]+'-'+date[2]
	else:
		date=time.strftime("%d-%m-%Y")
	with open("logs.txt","a") as f:
		f.write(time.strftime("%d-%m-%Y$%T")+":   opened "+flname+'('+str(flid)+') of '+date+'<br>')
	date1=date
	date=date.split('-')
	date=date[1]+'-'+date[0]+'-'+date[2]
	arr={1: 'https://tmklink.com/F0VFVU', 25: 'https://tmklink.com/WS6RsU3k', 26: 'https://tmklink.com/jh7B4QZQ', 239: 'https://tmklink.com/eLeQ', 28: 'https://tmklink.com/alcoV', 29: 'https://tmklink.com/YRKt0', 30: 'https://tmklink.com/xhyr', 31: 'https://tmklink.com/x7bH', 32: 'https://tmklink.com/ejsaqrk', 33: 'https://tmklink.com/A1Lo', 13: 'https://tmklink.com/NDJA', 34: 'https://tmklink.com/db85', 35: 'https://tmklink.com/wDY6xhk', 36: 'https://tmklink.com/wiDoM2B', 37: 'https://tmklink.com/a7kQK7', 38: 'https://tmklink.com/mG02h5Ni', 2: 'https://tmklink.com/cueIGjdE', 39: 'https://tmklink.com/lEmmkj', 275: 'https://tmklink.com/Hl9Cs', 40: 'https://tmklink.com/9s0bMt', 41: 'https://tmklink.com/Ju02', 301: 'https://tmklink.com/xMxE', 42: 'https://tmklink.com/abnD', 43: 'https://tmklink.com/hIw0io', 17: 'https://tmklink.com/HOpbz', 44: 'https://tmklink.com/Za2lQQ', 45: 'https://tmklink.com/qw2Dv', 46: 'https://tmklink.com/lYsB', 238: 'https://tmklink.com/BZjxO', 47: 'https://tmklink.com/d8vNe5lb', 48: 'https://tmklink.com/1RjCNOB', 20: 'https://tmklink.com/CrOvUF1', 49: 'https://tmklink.com/fV8N', 50: 'https://tmklink.com/32PnYQMb', 51: 'https://tmklink.com/hW5G5vuc', 52: 'https://tmklink.com/uR7i', 3: 'https://tmklink.com/QZdZYYN', 53: 'https://tmklink.com/PHTbzH', 6: 'https://tmklink.com/A1za6u', 7: 'https://tmklink.com/YvZuU', 8: 'https://tmklink.com/sq9DuQ', 9: 'https://tmklink.com/sPrjL', 10: 'https://tmklink.com/NV5E', 11: 'https://tmklink.com/81zmCp', 12: 'https://tmklink.com/SBhN', 14: 'https://tmklink.com/jbHJkUp', 15: 'https://tmklink.com/sbz1aQW', 16: 'https://tmklink.com/sZ3OYPO', 21: 'https://tmklink.com/JOiiqE', 22: 'https://tmklink.com/CJPT', 23: 'https://tmklink.com/AY1J', 24: 'https://tmklink.com/d3SQh', 27: 'https://tmklink.com/BoHor6sD',18:'https://tmklink.com/BQevV',19:'https://tmklink.com/ACROJpm',4:'https://tmklink.com/JNmMg'}
	outPage=onepaper
	outPage=outPage.replace("$state$",flname)
	outPage=outPage.replace("$link$",arr[int(flid)])
	outPage=outPage.replace("$imglink$",'https://raw.githubusercontent.com/GarudadevDataServices/imagebin/master/eenadu.png')
	outPage=outPage.replace("$date$",date)
	return outPage
	#return '''<html><head><title>'''+flname+'''</title><link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">  <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.5.0/css/bootstrap-datepicker.css" rel="stylesheet">  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.js"></script>  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>  <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.5.0/js/bootstrap-datepicker.js"></script><script type="text/javascript">$(document).ready(function () {$('#example1').datepicker({dateFormat: "dd-mm-yyyy",onSelect: function(dateText) {$(this).change();}}).change(function() {window.location.href = "?date=" + this.value;});});</script></head><body><a href="" id="Download" download=""></a><script>function register(){var request = new XMLHttpRequest();request.onload = function () {link=request.responseText;link=link.slice(1,-1);document.getElementById("Download").href=link;document.getElementById("Download").click();};request.open('GET','https://eenadu.firebaseio.com/een/'''+date1+'''/'''+str(flid)+'''/.json');link=request.send();}</script><br><center><img alt="https://drive.google.com/uc?id=1cOMzqhqHYI4QNyEZk6DUR6pS9l2ES19U&export=download" src="https://raw.githubusercontent.com/GarudadevDataServices/imagebin/master/eenadu.png" width="600" height="200" ></center><br><center><h2><b>Date :   </b><input class="button"  value ="'''+date+'''"  id="example1" style="color:black;font-size:30;width:175px;height:50px;" readonly></h2></center><h1><center><b>Download '''+flname+'''</b></center><br><center><button style="color:black;font-size:30;width:600px;height:70px;" onclick="register()"> Download </button></center><h1><center><a href="https://garudadev.herokuapp.com/allPapers" ><button style="color:black;font-size:30;width:600px;height:70px;"> More Papers</button></a></center></h1><script>function feedback(){var http = new XMLHttpRequest();http.onreadystatechange = function() {if(http.readyState == 4 && http.status == 200) {alert("Thankyou for sending feedback");document.getElementById('feedback').value='';}};if (document.getElementById('feedback').value!=''){http.open('post', 'https://guvi-41d93.firebaseio.com/feedback/.json');http.send(JSON.stringify({'feedback':document.getElementById('feedback').value}));}}</script><br><center><textarea id="feedback" placeholder="ask me anything.." style="border:3px dashed #000000;height:200px;width: 800px;font-size:30;" ></textarea><br><button onclick="feedback()" style="color:black;width:300px;height:90px;font-size:30;" >Submit</button><br><h2>Sunday magzine will be updated</h2></center></body></html>'''

@app.route("/sgol")
def sendtxt():
	with open("logs.txt","r") as f:
		matter=f.read()
	with open("logs.txt","a") as f:
		f.write(time.strftime("%d-%m-%Y$%T")+":   Opened logs<br>")
	return matter

@app.route("/updateData")
def updateData():
	global data
	data=fire.all_firebase()
	return 'data is updated'

#app.run()
