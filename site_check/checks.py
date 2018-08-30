import requests

def check_site(site):
    
    print('Checking: ' + site['name'])

    try:
        # make the request to the url
        request = requests.get(site['url'], timeout=10)
        
        # if we don't hit an error, then let's check for the presense of the string, if provided
        if site['string'] != None:
            if request.status_code == 200:
                if site['string'] in request.text:
                    stringfound=True
                else:
                    stringfound=False
            else:
                stringfound=False
        else:
            stringfound='No string provided. No string match performed.'
        
        # format the result
        result = {'name': site['name'], 'url': site['url'], 'string': site['string'], 'status_code': request.status_code, 'elapsed_time': request.elapsed.total_seconds(), 'stringfound': stringfound}
        return result
        
    except:
        # if the request encountered an error, send back an error result for this site
        result = {'name': site['name'], 'url': site['url'], 'string': site['string'], 'status_code': 'Error fetching site. Could not get status code', 'elapsed_time': 'No elapsed time available', 'stringfound': 'No string match performed'}
        return result
	    
	    
