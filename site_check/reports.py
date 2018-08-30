
def output_to_terminal(results):

    # set the initial exit code
    exit_code = 0

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
        
    print('-------------------------------------------------------------')

    # if any of the results didn't produce a 200 response code or if the strings weren't found for every result, then set exit code to 1
    if result['status_code'] != 200 or result['stringfound'] != True:
        exit_code = 1

    return exit_code
