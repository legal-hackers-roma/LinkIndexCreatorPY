from jinja2 import Template
from os import path


def createIndexTemplate(files, attorney, folder):
    template = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
            </head>
            <body>
            <style>
                h1{
                    text-align:center;
                }
                ul {
                    margin-top: 10%
                }
                li {
                    font-size:16px;
                }
                body {
                    margin-left: 6px;
                }
                .container {
                    margin-left: 10%;
                    padding-left: 10px;
                }
            </style>
                <h1>Indice atti e documenti</h1>
                <div class="container">
                <ul id="navigation">
                    {% for file in files %}
                    <li><a href="{{ file.url }}">{{ file.name }}</a></li>
                    {% endfor %}
                </ul>
                <br />
                <br />
                Avv. {{attorney}}
                </div>
            </body>
        </html>
        """

    compiledTemplate = Template(template)
    html = compiledTemplate.render(files=files, attorney=attorney)

    f = open(path.join(folder, '00_indice.html'), 'w')
    f.write(html)
    f.close

    return html
