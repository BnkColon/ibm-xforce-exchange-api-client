#!/usr/bin/python

#
# Python application that provide the 
# URL category information for a given URL 
# using the IBM X-Force Exchange
#
# Information about the X-Force Exchange:
#	 * Exchange: https://exchange.xforce.ibmcloud.com/
# 	 * API:https://api.xforce.ibmcloud.com/doc/
# Reference links used:
#        * Python httplib: https://docs.python.org/2/library/httplib.html#httplib.HTTPResponse
# 		

import httplib
import json
import string

# To get an anonymous authorization token
conn = httplib.HTTPSConnection('api.xforce.ibmcloud.com:443')
conn.request('GET', '/auth/anonymousToken')
anonymousToken = conn.getresponse() # Return httplib.HTTPResponse instance
t = anonymousToken.read()   # Make it able to operate
t = t.replace('"','')				# Eliminate the ""
t = t.replace('}','')				# Eliminate the final }
t = t.split(":")					
token = t[1]					# Select just the token
conn.close() 					# Close connection
#print 'TOKEN '+token

# To create the Authorization header
hToken = 'Bearer '+ token 			# "Create" the token		
headers = {'Authorization': hToken} 		# Add token to the header

# Ask for URL 
url = raw_input('Enter url: ') 			# Request an URL
urlConn = httplib.HTTPSConnection('api.xforce.ibmcloud.com')
urlConn.request('GET', '/url/'+url, headers=headers)
resp = urlConn.getresponse() 			# Response with all info about url
m = resp.read()						
urlConn.close() 				# Close connection

# Return categories or error message
m = json.loads(m)
if ('error' in m):				# if can split by error it's because have an error
	print m 				# Display error message
else:
	print m['result']['cats']  		# Display the categories
	

