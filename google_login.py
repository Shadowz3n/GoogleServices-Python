#!/usr/bin/python
#  -*- coding: utf-8 -*-
import mechanize, urllib, sys

def doLoginGoogle(user,passw):
	print "\033[92m[Creating Google Session]\033[0m"
	br				= mechanize.Browser(factory=mechanize.RobustFactory())
	br.set_handle_robots(False)
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_refresh(False)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders	= [('User-agent', 'Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11')]
	br.open("https://accounts.google.com/AddSession")
	session			= br.response().read()
	br.select_form(nr=0)
	br.form.set_all_readonly(False)
	br.form.new_control('text','Email',{'value':user})
	br.form.fixup()
	res				= br.submit()
	sessionn		= br.response().read()
	br.select_form(nr=0)
	br.form.set_all_readonly(False)
	br.form.new_control('text','Passwd',{'value':passw})
	br.form.fixup()
	login			= br.submit()
	if login.geturl().find("myaccount.google.com")>0:
		print "\033[92m[Logged in Google]\033[0m"
		
		# List files with paste ID
		#br.open("https://drive.google.com/act", urllib.urlencode({docId:'',authuser:0,minResultCount:20,recursive:true,token:}))
		
		# Download file ID
		br.open("https://drive.google.com/uc?id=0B6b4BiW-o9hxNk1veEJVa1FrU1E&authuser=0&export=download")
		services	= br.response().read()
		print services
	else:
		print "\033[91m[The email and password you entered don't match]\033[0m"

if len(sys.argv)>2:
	doLoginGoogle(sys.argv[1], sys.argv[2])
else:
	print "Usage: "+sys.argv[0]+" <login> <pass>"
