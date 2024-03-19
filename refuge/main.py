from website import create_app

app = create_app()

#runs a web server when u import 'website' folder only from main file directly
if __name__ == '__main__':
    app.run(debug=True) #runs flask application, start web server 



