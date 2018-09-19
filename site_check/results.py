
def parse_to_terminal(results):

    # set the initial count of errors found
    errors_found = 0

    # loop through each site result and print out the details
    for result in results:
        result = result.result() # yes, this is ugly
        print('-------------------------------------------------------------')
        print('Site Name: ' + result['name'])
        print('Site URL: ' + result['url'])
        print('String To Find: ' + str(result['string']))
        print('-')
        print('Status Code: ' + str(result['status_code']))
        print('String Match Result: ' + str(result['stringfound']))
        print('Loaded In: ' + str(result['elapsed_time']) + ' seconds')
        
        # if any of the results didn't produce a 200 response code or if the strings weren't found for every result, then add to the error count
        if result['status_code'] != 200 or result['stringfound'] != True:
            errors_found += 1
            
    print('-------------------------------------------------------------')

    return errors_found
