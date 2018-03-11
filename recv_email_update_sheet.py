# -*- coding: utf-8 -*-

import logging

from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

import googleapiclient.discovery
from google.oauth2 import service_account

import webapp2

SERVICE_ACCOUNT_FILE = 'gcp-procmail-a11210e7c724.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials = service_account.Credentials.from_service_account_file(
               SERVICE_ACCOUNT_FILE, scopes=SCOPES)

class LogSenderHandler(InboundMailHandler):
    
    def receive(self, mail_message):
        
        #bodies = mail_message.bodies()
        #logging.info( mail_message.subject )
        #logging.info( mail_message.message.Message )
        #for (encoding, bod) in bodies:
        #    logging.info( str(bod.decode()) )

        service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)
       
        spreadsheetId = '1Fjs2RK-Pe58MHNcth49gCF5UghZ_2Uq3cOjGJROiS0M'
        rangeName = 'Data!A1:E10'
        value_input_option = 'RAW'  # TODO: Update placeholder value.
        # How the input data should be inserted.
        insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.
        value_range_body = { "values" : [["Test", mail_message.subject]]}
        request = service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range=rangeName, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute() 
        
        del request
        del response 


class UpdateSheet(webapp2.RequestHandler):

    def get(self):
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
        
        #app.logger.addHandler(AppLogsHandler())

        #app.logger.error("MY ERROR")
        
        SERVICE_ACCOUNT_FILE = 'gcp-procmail-a11210e7c724.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)
        
        spreadsheetId = '1Fjs2RK-Pe58MHNcth49gCF5UghZ_2Uq3cOjGJROiS0M'
        rangeName = 'Data!A1:E10'

        #result = service.spreadsheets().values().get( spreadsheetId=spreadsheetId, range=rangeName).execute()
        
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write( "Service Account Name:" + app_identity.app_identity.get_service_account_name() )

        #values = result.get('values', [])
        #if not values:
        #    self.response.write('No data found.')
        #else:
        #    self.response.write('Name, Major:')
        #    for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
        #        self.response.write('%s, %s' % (row[0], row[1]))
                
        #del result
                
        value_input_option = 'RAW'  # TODO: Update placeholder value.
        # How the input data should be inserted.
        insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.

        value_range_body = { "values" : [["Test", "Test"]]}

        request = service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range=rangeName, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()
    
        self.response.write(response)
        del response 
        del request
        del service
        
        #import pdb; pdb.set_trace();

           
app = webapp2.WSGIApplication([
    #(decorator.callback_path, decorator.callback_handler()),
    #('/test', MainPage),
    LogSenderHandler.mapping(),
    ('/updatesheet', UpdateSheet),
], debug=True)