from urllib import request
'''Alternate way to import'''
sample_url = "http://chart.finance.yahoo.com/table.csv?s=SNE&a=1&b=8&c=2017&d=2&e=8&f=2017&g=d&ignore=.csv"
def download_stocks(csv_url):
    response = request.urlopen(csv_url)#Program goes online to the url and save the connection in response
    csv = response.read()# Reads data from response.
    csv_str = str(csv)# Converts to string
    lines = csv_str.split("\\n")# Reads text file string and puts a new line where text ends
    des_url = r'sony.csv'#Puts data in a raw string location
    fx = open(des_url,'w')#Writes to the new file
    for line in lines: # For each end of line in the various text lines skip to a new line
        fx.write(line + "\n")
    fx.close()#Closes the file.

download_stocks(sample_url)