# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
#from flask_mysqldb import MySQL
#import MySQLdb.cursors

import os 
import json
#from datetime import datetime




#now=datetime.now()

app = Flask(__name__)

j=os.getcwd()+"/static/img/product"

#l=os.listdir(j)
def datas(s):
	datas=open(s,"r")
	datas=datas.read()
	datas=datas[1:len(datas)-1]
	datas=datas.replace("'","\"")
	datas=json.loads(datas)
	return datas
	
def lod(e,rea):
		rea=rea.replace("'","")
		rea=rea.replace("'","\"")
		print(type(rea))
		print(rea)
		
		rea=json.loads(rea)	
		updic={e:rea}
		updic=str(updic)
		updic=updic.replace("'","\"")
		print(updic)
		print(type(updic))
		updic=json.loads(updic)
		return updic

@app.route('/', methods=['get'])
def index():
	print(os.getcwd())
	prod=datas("tryp")
	return render_template("index.html",prod=prod)
@app.route("/get_regi", methods=["GET","POST"])
def get_regi():
	name=request.form["uname"]
	email=request.form["email"]
	passw=request.form["pass"]
	passw1=request.form["pass1"]
	if passw==passw1:
		rea=str({f'"name":"{name}","email":"{email}","passw":"{passw}"'})
		

		up=lod(email,rea)
		up[email].update({"products":{}})
		dat=datas("regi")
		#print(dat,type(dat))
		dat.update(up)
		print(dat)
		file=open("regi","w")
		file.write(f"'{dat}'")
		file.close()
		return index()

@app.route('/post-ads/<record_id>', methods=['get','post'])
def user_addpage(record_id):
	id=record_id
	print(os.getcwd())
	return render_template("post-ads.html",id=id)
@app.route('/user-addproduct', methods=['get','post'])
def user_addproduct():
	print(os.getcwd())
	title=request.form["Title"]
	price=request.form["price"]
	details=request.form["details"]
	file=request.files["file"]
	pn=file.filename
	file.save(f'{j}/{pn}')
	name=request.form["name"]
	phone=request.form["phone"]
	address=request.form['address']
	email=request.form['email']
	rea=str({f'"name":"{name}","phone":"{phone}","title":"{title}","price":"{price}","address":"{address}","pic":"/static/img/product/{pn}","details":"{details}","email":"{email}"'})
	print(details)
	up=lod(phone,rea)
	dat=datas("product")
	dat.update(up)
	file=open("product","w")
	file.write(f"'{dat}'")
	file.close()
	dat=datas("regi")
	dat[email]["products"].update(up)
	file=open("regi","w")
	file.write(f"'{dat}'")
	file.close()
	return index()
@app.route("/get_login", methods=["GET","POST"])
def get_login():
	
	email=request.form["mail"]
	passw=request.form["passw"]
	k=datas("regi")
	if email in k and k[email]["passw"] == passw:
		return render_template("dashboard.html",id=email)
	elif email =="Smaronbi" and passw=="Smaronbi":
		return render_template("admin-index.html")
	return render_template("404.html")

@app.route('/product-req', methods=['get','post'])
def p_req():
	m=datas("product")
	dat=datas("tryp")
	print(os.getcwd())
	return render_template("product-req.html",m=m,dat=dat)
@app.route('/users', methods=['get','post'])
def users():
	m=datas("regi")
	print(os.getcwd())
	return render_template("users-table.html",m=m)

@app.route('/login', methods=['get','post'])
def login():
	print(os.getcwd())
	return render_template("login.html")
@app.route('/register', methods=['get','post'])
def register():
	print(os.getcwd())
	return render_template("register.html")
@app.route('/dashboard/<record_id>', methods=['get','post'])
def user_dash(record_id):
	print(os.getcwd())
	prod=datas("tryp")
	id=record_id
	return render_template("dashboard.html",prod=prod,id=id)
@app.route('/product/<record_id>', methods=['get','post'])
def product(record_id):
	dat=datas("tryp")
	dat=dat[record_id]
	return render_template("ads-details.html",l=0,dat=dat)

a=[]
e=[]
@app.route('/get_bid/<record_id>', methods=['get','post'])
def get_bid(record_id):
	print(os.getcwd())

	
	email=request.form["email"]
	price=request.form["price"]
	if email in datas("ragi"):
		
		print(email,price)
		a.append(price)
		e.append(email)
		a.sort()
		e.sort()
		l=len(e)
		print(e,a)
		dat=datas("tryp")
		dat=dat[record_id]
		return render_template("ads-details.html",e=e,a=a,l=l,dat=dat)
	else:
		return register()
@app.route('/contact', methods=['get','post'])
def contact():
	return render_template("contact.html",l=0)


@app.route('/faq', methods=['get','post'])
def faq():
	return render_template("faq.html",l=0)



@app.route('/about', methods=['get','post'])
def about():
	return render_template("about.html",l=0)


@app.route('/category', methods=['get','post'])
def category():
	dat=datas("tryp")
	print(dat)
	return render_template("category.html",dat=dat)


'''@app.route('/faq', methods=['get','post'])
def faq():
	return render_template("faq.html",l=0)


@app.route('/about', methods=['get','post'])
def about():
	return render_template("about.html",l=0)'''


#delete somthing 
@app.route('/pr_u/<record_id>', methods=["GET","POST"])
def user_confirm(record_id):
	id=record_id
	time=request.form["time"]
	price=request.form["price"]
	#isdel=request.form["idDeli"]
	#idpay=request.form["isPay"]
	rea=str({f'"time":"{time}","price":"{price}","iddel":"s","ispay":"s"'})
	rea=rea.replace("'","")
	rea=rea.replace("'","\"")
	r=json.loads(rea)
	dat=datas("product")
	dat[id].update(r)
	da=dat[id]
	du=datas("tryp")
	du.update({id:da})
	file=open("tryp","w")
	file.write(str(f"'{du}'"))
	file.close()
	dat.pop(id)
	file=open("product","w")
	file.write(str(f"'{dat}'"))
	file.close()
	d=datas("regi")




	file=open("regi")

	return p_req()

@app.route('/user_delete/<record_id>', methods=["GET","POST"])
def user_delete(record_id):
	id=record_id
	dat=datas("regi")

	dat.pop(id)
	print(dat)
	file=open("regi","w")
	file.write(str(f"'{dat}'"))
	file.close()
	return render_template("users-table.html",m=dat)
@app.route('/pr_d/<record_id>', methods=["GET","POST"])
def pr_d(record_id):
	id=record_id
	dat=datas("product")
	dat.pop(id)
	file=open("product","w")
	file.write(str(f"'{dat}'"))
	file.close()

	return p_req()




@app.route('/product_del/<record_id>', methods=["GET","POST"])
def product_del(record_id):
	id=record_id
	dat=datas("tryp")
	dat.pop(id)
	file=open("tryp","w")
	file.write(str(f"'{dat}'"))
	file.close()

	return p_req()

#user ads
@app.route('/account-myads/<record_id>', methods=['get','post'])
def myads(record_id):
	dat=datas("regi")
	prod=dat[record_id]["products"]


	return render_template("account-myads.html",prod=prod,id=record_id)

#auc history
@app.route('/history', methods=['get','post'])
def history():
	m=datas("regi")
	return render_template("history.html",m=m)
#winer
'''app.route('/winer', methods=['get','post'])
def winer():
	dat=datas("tryp")
	dat1=datas("hist")
	naw_=now.strftime("%B %d, %Y")
	now_t=now.strftime("%H:%M:%S")
	sf=(f"{naw_} {now_t}").split(" ")
	print(sf)
	for i in dat:
		print(dat)
		k=dat[i]["time"].split(" ")
		if k[:2]== sf[:2]:
			#e=sum(list(map(int, k[3].split(":"))))
			e1=k[3].split(":")
			e2=sf[3].split(":")
			print("e")
			if (int(e1[0]) == int(e2[0]) and int(e2[1])>int(e1[1])) or int(e2[0])> int(e1[0]):
				print("yes")
				f=lod(i,dat[i])
				dat1.update(f)
				r=open("hist","w")
				r.write(str(f"'{dat1}'"))
				r.close()
				r=open("tryp","w")
				dat.pop(i)
				r.write(str(f"'{dat}'"))
				r.close()
			elif int(k[1])<int(sf[1]):
				print("yes")
				f=lod(i,dat[i])
				dat1.update(f)
				r=open("hist","w")
				r.write(str(f"'{dat1}'"))
				r.close()
				r=open("tryp","w")
				dat.pop(i)
				r.write(str(f"'{dat}'"))
				r.close()
			else:
				pass
	return index() 
#'''

if __name__ == '__main__':
       app.run(debug=True,port=1234)


'''
import imageio,os
o=[]
inp=input("Enter the images (separet wiht space) : ")
inp=inp.replace("'","")
images = inp.split(" ")
print(images)
for i in images:
	o.append(imageio.imread(i))
imageio.mimsave(f'{os.getcwd()}/movie.gif', o)'''