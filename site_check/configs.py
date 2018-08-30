import os
import sys
from configparser import SafeConfigParser

def get_configuration_entries(config):

    # create a list (in order of priority) of default config file paths
    default_config_paths = ['./site-check.cfg',os.path.expanduser("~") + '/.site-check.cfg']
    
    # add user-specified config file to beginning of list if specified
    if config != None:
        default_config_paths.insert(0, config)

    # loop through list (in order) and stop when we either 1) can't find the cli-specified 
    # config file or 2) can't find any config files from the default config paths
    for index, config in enumerate(default_config_paths):
        if os.path.isfile(config):
            valid_config = config
            print('Using Config: ' + str(config))
            break
        elif index==0 and len(default_config_paths)>2:
            print('Specified config file ' + str(config) + ' not found')
            break

    # if no valid config was found after trying all options for our situation, then exit
    try:
        valid_config
    except NameError:
        print('Unable to find a valid config file')
        sys.exit(1)
    
    # if valid config was found, read individual site configs from it and return them to
    # the calling function as an array of dicts
    if valid_config != None:
        sites = []
        configfile = SafeConfigParser()
        configfile.read(valid_config)
        for section in (section for section in configfile if section != 'DEFAULT'):
            site = {'name': section, 'url': configfile.get(section, 'url'), 'string': configfile.get(section, 'string')}
            sites.append(site)
        return sites
