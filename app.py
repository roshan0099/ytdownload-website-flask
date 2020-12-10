from flask import Flask,url_for,render_template,request, redirect 
from pytube import YouTube
# import requests
# requests.packages.urllib3.disable_warnings()
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def home():
	name = ""
	user = ""
	title =""
	global song
	global opt
	try:
		if request.method == 'POST' :

			if request.form['submit'] == 'search' :
				user = request.form['entry']
				print(user)
				# try :
				song = YouTube(user)
				print(song.streams.filter(type = 'audio'))
				name = song.title
				print(name)
				title = song.streams.filter(type='audio')
				return render_template('index.html', content = title, head = name, r = 1)
			if request.form['submit'] == 'submit':
				print("working")
				option = request.form['options']
				print(option)
				opt = song.streams.get_by_itag(option)
				return redirect(url_for('info'))

		# except :
		# 	return "<h1>No net it seems apparently</h1>"	

		# return redirect(url_for('info',usr = type))
			return render_template('index.html', content = title)
		else :
			return render_template('index.html')
	except:
			return "<h2>....something went wrong</h2>"	
					
@app.route('/download', methods = ['GET','POST'])
def info():
	try:
		if request.method == "POST":
			if request.form['search'] == 'submit':
				print("1")
				return redirect(url_for('home'))
		print(opt)
			# down.download()
			# return render_template('info.html', content = tag)
			# print(title)
		opt.download()
		return render_template("info.html", content = opt)	
	except :
		return "<h2>oops ......something is went wrong</h2>"

if __name__ == '__main__':
	app.run(debug= True)	