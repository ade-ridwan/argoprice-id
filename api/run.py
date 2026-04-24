from app import create_app

app = create_app()

if __name__ == '__main__':
    # Jalankan dalam mode debug untuk development
    app.run(debug=True, port=5000)
