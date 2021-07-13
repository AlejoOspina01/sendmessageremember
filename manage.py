import requests

def main():
    payload = {"text":"Mensaje de prueba \n esto es una prueba con backslash"}
    r = requests.post('https://hooks.slack.com/services/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', json=payload)
    print(r.reason)
    print(r.content)

if __name__ == '__main__':
    main()

