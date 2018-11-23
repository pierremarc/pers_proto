# a prototype/playground for perspective 

it's a django project, so as usual:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements
./manage.py migrate
./manage.py createsuperuser --username admin
```
Then the specific, importing data. I just made one importer to test.

```bash
./manage.py import_strat path/to/the/strat/excel/turned/into/csv admin
```

run the server with 
```bash
./manage.py runserver
```

One can see the imported data at http://localhost:8000/pers/data/


After having created polygons to attach to  projects at http://localhost:8000/admin/perspective_pp/polygon/add/


You can have a geojson at http://localhost:8000/pers/layer/polygon/projectname/intent

