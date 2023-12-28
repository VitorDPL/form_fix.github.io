# único objetivo desse arquivo é rodar o programa.
# como o arquivo __init__.py roda automaticamente, basta importar o app.

from form_fix import app

if __name__ == '__main__':
    app.run(debug= True)

