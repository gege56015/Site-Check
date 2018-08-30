import concurrent.futures
import sys
import click
from .configs import get_configuration_entries 
from .checks import check_site
from .reports import output_to_terminal

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
    
    # in batches of 10 at a time, let's check the sites
    executor = concurrent.futures.ThreadPoolExecutor(10)
    futures = [executor.submit(check_site, site) for site in sites]
    concurrent.futures.wait(futures)
    
    # output the results to the terminal
    exit_code = output_to_terminal(futures)

    print('All specified sites checked. Exiting.')
    sys.exit(exit_code)

if __name__ == '__main__':
    site_check()


