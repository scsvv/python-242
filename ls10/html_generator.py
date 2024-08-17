import os

def content(data, filename):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        {data}
    </body>
    </html>
    """

    with open(f'{filename}.html', 'w+') as file:
        file.write(html)

