# -*- coding: utf-8 -*-
import httplib2

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = './client_secret.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
  credentials = run(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)

messages = gmail_service.users().messages().list(userId='me',q='has:attachment').execute()

if messages['messages']:
  for message in messages['messages']:
    msg_id = message['id']
    print 'Message ID: %s' % (msg_id)
    msg = gmail_service.users().messages().get(userId='me',id=msg_id).execute()
    payload = msg['payload']
    for item in payload['headers']:
    	if item['name'] == 'From':
    		print "From:", item['value'].encode('utf-8')
    	if item['name'] == 'To':
    		print "To:", item['value'].encode('utf-8')
    	if item['name'] == 'Subject':
    		print 'Subject:', item['value'].encode('utf-8')
    for item in payload['parts']:
    	if item['filename']:
    		print 'File Name:', item['filename'].encode('utf-8')
    		body = item['body']
    		#print 'Attachment ID:', body['attachmentId']
    		print 'Size:', body['size']
    		print
    print