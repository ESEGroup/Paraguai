from web import App
import os

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  App.run(host='0.0.0.0', port=port)
