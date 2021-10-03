# Email-Distance

List of 1000 most popular domains worldwide obtained from 'https://www.htmlstrip.com/alexa-top-1000-most-visited-websites'  

## Variables

input variables are placed in `config.py`  

- trusted_domains_file = path of trusted domains csv
- distance = input metric used as cutoff for distance calculation
- in_list = list containing domains to be checked

## Note

This application is optimized for speed. Each site's risk is calculated in parallel. Levenshtein distance is also calculated in parallel.
