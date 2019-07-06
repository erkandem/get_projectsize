# get_projectsize
estimate download size of package dependencies


## idea
before you actually install a debian/ubuntu or other package you're
getting an estimate on the disk and network usage. I feld the urge to write
this after recovering application code from old hard drives. Couöd give you an
idea on how much time you have to grab a coffee.


sample call with sample output

```bash
$ python3 get_projectsize.py [location/to/requitements.txt]
$ python3 -m get_projectsize [location/to/requitements.txt]
```

The output could look lik:

```bash
...
{'packagename': 'SQLAlchemy==1.3.2', 'version': '1.3.2', 'size': 5851340}
{'packagename': 'statsmodels==0.9.0', 'version': '0.9.0', 'size': 9801794}
{'packagename': 'traitlets==4.3.2', 'version': '4.3.2', 'size': 74730}
{'packagename': 'ua-parser==0.8.0', 'version': '0.8.0', 'size': 34785}
{'packagename': 'urllib3==1.24.1', 'version': '1.24.1', 'size': 118086}
{'packagename': 'Werkzeug==0.15.2', 'version': '0.15.2', 'size': 328938}
total: 138597 kb - 138.597 Mb

```

⚠️ does not recursively add subdependencies.
you already have specified list of ``requirements.txt`` 
pipenv doesn't need to be reinvented.


## it doesn't sove my use case!
a) skip back to search
b) fork this repo and use it as a boilerplate for something awesome

consider it a GIST rather than a traditional repo


