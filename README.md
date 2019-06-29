# get_projectsize
estimate size of packages before downloading via pip


⚠️ does not consider depencencies

sample call with sample output

```bash
$ python get_projectsize.py [location/to/requitements.txt]

...

{'packagename': 'SQLAlchemy==1.3.2', 'version': '1.3.2', 'size': 5851340}
{'packagename': 'statsmodels==0.9.0', 'version': '0.9.0', 'size': 9801794}
{'packagename': 'traitlets==4.3.2', 'version': '4.3.2', 'size': 74730}
{'packagename': 'ua-parser==0.8.0', 'version': '0.8.0', 'size': 34785}
{'packagename': 'urllib3==1.24.1', 'version': '1.24.1', 'size': 118086}
{'packagename': 'Werkzeug==0.15.2', 'version': '0.15.2', 'size': 328938}
total: 138597 kb - 138.597 Mb

```
