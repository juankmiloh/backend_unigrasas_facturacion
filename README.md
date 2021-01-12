## Back-end para el manejo del módulo de facturacion de UNIGRASAS

# linux/MacOS
<!-- export FLASK_ENV=production -->
export FLASK_ENV=development
python3 app.py runserver -h 0.0.0.0 -p 5000

# Windows PowerShell
<!-- $env:FLASK_ENV = "production" -->
$env:FLASK_ENV = "development"
python app.py runserver -h 0.0.0.0 -p 5000

<!-- python3 app.py runserver -h 0.0.0.0 -p 5000 -->