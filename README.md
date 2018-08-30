## Site-Check

Site-Check is a simple Python utility intended to be run on the command-line. As input, it takes either an individual URL and string or a config file of many such URLs and strings. It then makes requests to the URL(s) and searches for the presence of the associated string. It uses threading to process requests in batches of 10 (adjustable in the code, of course), so it can be used to check many sites and/or APIs quickly. When it's done running, it outputs a report of results. After outputting the report, it will finally exit with a non-zero status code if either 1) any of the requests had anything other than a 200 status response or 2) any of the strings associated with a given URL were not found in the response. 

NOTE: This is essentially the result of some scratch code and is not intended as a fully baked project. 

## How To Use

1) Install via Pip3 (NOTE: this was only tested on Linux) as follows: 
```
pip3 install git+https://github.com/gege56015/Site-Check.git
```

2) Run site-check with the help option for instructions
```
site-check --help
```

3) Optionally place a config file in either your home directory (~/.site-check.cfg) or in the same directory that you run the site check command in ($PWD/.site-check.cfg) in order to have the same set of sites checked whenever you run 'site-check'. An example config file can be found in the repo with the name 'sample_config.cfg'.

## Caveat

This utility is not designed to parse the mountains of Javascript in use on websites today. For that, a good solution is Selenium with headless Firefox or headless Chrome. 
