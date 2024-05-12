from api import create_app
import config as config

app = create_app(config.ProductionConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
