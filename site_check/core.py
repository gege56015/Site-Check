import concurrent.futures
import sys
import click
from .configs import get_configuration_entries 
from .checks import check_site
from .results import parse_to_terminal

@click.command()
@click.option('--url', default=None, help='URL to check (in the form: https://www.google.com)')
@click.option('--string', default=None, help='String to look for at URL (in the form: "Google")')
@click.option('--config', default=None, help='Location of config file to use (ignored if --url provided)')
def site_check(url, string, config):
    
    # if url was provided on the command line, then populate sites list directly with the provided url and string
    # otherwise, attempt to populate the sites list from a config file
    if url != None:
        sites = [{'name':'Site Name Not Specified','url':url,'string': string}]
    else:
        sites = get_configuration_entries(config)
    
    # with a concurrency of 10, let's check the sites
    executor = concurrent.futures.ThreadPoolExecutor(10)
    futures = [executor.submit(check_site, site) for site in sites]
    concurrent.futures.wait(futures)
    
    # parse the results, print them to the terminal, and get back the number of errors found
    errors_found = parse_to_terminal(futures)

    print('All specified sites checked. Exiting.')
    
    if errors_found == 0:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    site_check()


