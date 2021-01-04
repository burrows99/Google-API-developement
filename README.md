# Google-API-developement
1. Get a spreadsheet to work on
2. Open https://console.developers.google.com/apis/dashboard?project=raunak-300714
   *  Create your own new project
   *  Click on the project and find an option that says 'Explore and enable APIs'
   *  Click on Enable APIs and Services
   *  Click on Google sheets API
   *  Click on Enable
   *  Click on credentials on te left side of your screen
   *  Click on manage service accounts on the right (to create a service account) and then create a service account
   *  Give a name and permissions as 'Editor'
   *  Copy te email
   *  Click on share on the spreadsheet page and paste the email there
   *  Open the email in and click on 'add key' then click on 'create new key' and select the file type as .json file and download it.
3. Create a python file (paste the code given in the repositort with name read_write_spreadsheet.py) and keep the .json file in the same folder as the python file.
4. SERVICE_ACCOUNT_FILE is the name of your .json file
   SAMPLE_SPREADSHEET_ID is your partial spreadsheet link (for eg. in https://docs.google.com/spreadsheets/d/1XG-sQDgXxVO-b_qXW50cvJnzm2m9eYkHZUAlvMdsBRs/edit#gid=0 everything after d/ and before /edit is what we are concerned with.)
   
