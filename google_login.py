#!/usr/bin/python
#  -*- coding: utf-8 -*-
# Google Services (IMPS)
# @autor: Henrique Bissoli Silva (emp.shad@gmail.com)
# Updates: https://github.com/Shadowz3n/Google-Services
import mechanize, sys, json

if len(sys.argv)>2:
	print "\033[92m[Creating Google Session]\033[0m"
	br				= mechanize.Browser(factory=mechanize.RobustFactory())
	br.set_handle_robots(False)
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_refresh(False)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders	= [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')]
	br.open("https://accounts.google.com/AddSession")
	session			= br.response().read()
	br.select_form(nr=0)
	br.form.set_all_readonly(False)
	br.form.new_control('text','Email',{'value':sys.argv[1]})
	br.form.fixup()
	res				= br.submit()
	sessionn		= br.response().read()
	br.select_form(nr=0)
	br.form.set_all_readonly(False)
	br.form.new_control('text','Passwd',{'value':sys.argv[2]})
	br.form.fixup()
	login			= br.submit()
	if login.geturl().find("myaccount.google.com")>0:
	
		# Get Token
		# My paste: u/2/folders/0B2qbDxOlHLfPeThCYUFNQlQ0Wk0 or my-drive
		br.open("https://drive.google.com/drive/u/0/folders/0B2qbDxOlHLfPeThCYUFNQlQ0Wk0")
		token		= br.response().read().split(',[["xsrf","')[1].split('",["')[0]
	
		print token
	
		# Itens
		#itens		= br.response().read().split("window['_DRIVE_ivd'] = '")[1].replace('\\x22', '"').replace('\\n', '').replace('\\\\', '').split(";")[0].replace('\/', '/')[:-1]
	
		# Upload file
		#br.open("https://drive.google.com/upload/resumableuploadsc?authuser=0", '{"protocolVersion":"0.8","createSessionRequest":{"fields":[{"external":{"name":"file","filename":"Seguro Fian\u00e7a - Ficha Pessoa Fisica - RESIDENCIAL.pdf","put":{},"size":188113}},{"inlined":{"name":"parentId","content":"0B6b4BiW-o9hxRlBnRVFlZzgwRVE","contentType":"text/plain"}},{"inlined":{"name":"driveSourceClientService","content":"UploadWeb","contentType":"text/plain"}},{"inlined":{"name":"modifiedTime","content":"1452096907160","contentType":"text/plain"}}]}}')
		
		# Download file ID
		#br.open("https://drive.google.com/uc?id=0B6b4BiW-o9hxNk1veEJVa1FrU1E&authuser=0&export=download")
		
		#upload		= br.response().read()
		#print upload
	else:
		print "\033[91m[The email and password you entered don't match]\033[0m"
else:
	print "Usage: "+sys.argv[0]+" <login> <pass>"
