#!/usr/bin/python
#  -*- coding: utf-8 -*-
import mechanize, sys, json

def doLoginGoogle(user,passw):
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
		
		# Get Token
		# My paste: u/2/folders/0B2qbDxOlHLfPeThCYUFNQlQ0Wk0 or my-drive
		br.open("https://drive.google.com/drive/u/2/folders/0B2qbDxOlHLfPeThCYUFNQlQ0Wk0")
		token		= br.response().read().split(',[["xsrf","')[1].split('",["')[0]
		itens		= br.response().read().split("<script>window['_DRIVE_ivd'] = '")[1].split('\n'+"'"+';')[0]
		
		#br.open("https://drive.google.com/act", '{docId:"0B2qbDxOlHLfPdEplb1k3WnYyUTA",authuser:0,minResultCount:20,recursive:true,token:'+token+'}')
		print itens
		
		# List 2
		#br.open("https://clients6.google.com/drive/v2internal/files/0B6b4BiW-o9hxRlBnRVFlZzgwRVE?fields=kind%2Ctitle%2CmimeType%2CcreatedDate%2CmodifiedDate%2CmodifiedByMeDate%2ClastViewedByMeDate%2CfileSize%2ClastModifyingUser(kind%2C%20displayName%2C%20picture%2C%20permissionId%2C%20emailAddress)%2ChasThumbnail%2Cid%2Cshared%2CsharedWithMeDate%2CuserPermission(role)%2CexplicitlyTrashed%2CquotaBytesUsed%2Cshareable%2Ccopyable%2Csubscribed%2CfolderColor%2ChasChildFolders%2Cpermissions(kind%2Cid%2Cname%2CemailAddress%2Cdomain%2Crole%2Ctype%2CphotoLink%2CadditionalRoles%2CwithLink)%2CfileExtension%2CprimarySyncParentId%2CsharingUser(kind%2CdisplayName%2Cpicture%2CpermissionId%2CemailAddress)%2CflaggedForAbuse%2CfolderFeatures%2Cspaces%2CsourceAppId%2Crecency%2CrecencyReason%2Cparents(id)%2Clabels(starred%2Chidden%2Ctrashed%2Crestricted%2Cviewed)%2Cowners(permissionId%2CdisplayName%2Cpicture%2Cdomain%2Ckind)&openDrive=true&reason=102&syncType=0&errorRecovery=false&key="+token)
		
		
		
		# List files with paste ID
		#
		
		# Upload file
		#br.open("https://drive.google.com/upload/resumableuploadsc?authuser=0", '{"protocolVersion":"0.8","createSessionRequest":{"fields":[{"external":{"name":"file","filename":"Seguro Fian\u00e7a - Ficha Pessoa Fisica - RESIDENCIAL.pdf","put":{},"size":188113}},{"inlined":{"name":"parentId","content":"0B6b4BiW-o9hxRlBnRVFlZzgwRVE","contentType":"text/plain"}},{"inlined":{"name":"driveSourceClientService","content":"UploadWeb","contentType":"text/plain"}},{"inlined":{"name":"modifiedTime","content":"1452096907160","contentType":"text/plain"}}]}}')
		
		# Download file ID
		#br.open("https://drive.google.com/uc?id=0B6b4BiW-o9hxNk1veEJVa1FrU1E&authuser=0&export=download")
	else:
		print "\033[91m[The email and password you entered don't match]\033[0m"

if len(sys.argv)>2:
	doLoginGoogle(sys.argv[1], sys.argv[2])
else:
	print "Usage: "+sys.argv[0]+" <login> <pass>"
