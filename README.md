## Back-end para el manejo del módulo de facturacion de UNIGRASAS

# linux/MacOS
<!-- export FLASK_ENV=production -->
export FLASK_ENV=development
python3 manage.py runserver -h 0.0.0.0 -p 5000

# Windows PowerShell revisar el archivo manage.py y escoger el ambiente a utilizar desarrollo o produccion
<!-- $env:FLASK_ENV = "production" -->
$env:FLASK_ENV = "development"
python manage.py runserver -h 0.0.0.0 -p 5000

<!-- python3 manage.py runserver -h 0.0.0.0 -p 5000 -->