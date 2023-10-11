from Controller.Transactions import app


if __name__ == "__main__":
    try:
        app.run(debug=True, port=8000)
    except Exception as e:
        raise e
    