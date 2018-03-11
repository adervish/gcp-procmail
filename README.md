# gcp-procmail
Use google App engine to receive incoming mail, process the mail and log it to a google spreadsheet

This uses GAE's recieve email functionality to process an incoming email message, parse out the header, then use the Google API to connect to Google sheets and append the subject of the message to a google spreadsheet. 

There is a memory leak in the Google Sheets API, which causes the GAE instance to chrew through about 50mb of memory per request. It seems to restart and que the next message until it has restarted the instance. 


Required libs for GAE need to go in the lib directory
- I think this is just Google Python API which will pull in httplib2 and oauth2client

Credentials json for the service account that has access to the spreadsheet should be in the local directory 
