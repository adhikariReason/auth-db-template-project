from website import create_app
from flask import Flask


app = create_app()

if __name__ == '__main__':
	app.run(debug=True)		#auto updates server when fileis saved, during production phase turn it off
