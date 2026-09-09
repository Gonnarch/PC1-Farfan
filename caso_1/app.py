from pathlib import Path
from urllib.parse import urlparse
import os
from flask import Flask, render_template, request, send_from_directory, abort
import yt_dlp

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024
DOWNLOAD_DIR = Path(os.environ.get('DOWNLOAD_DIR', str(Path(__file__).parent / 'downloads'))).resolve()
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
HOSTS = ('youtube.com', 'youtu.be', 'instagram.com', 'tiktok.com', 'facebook.com', 'fb.watch', 'linkedin.com')

def videos():
    return sorted([p for p in DOWNLOAD_DIR.iterdir() if p.is_file() and p.suffix.lower() in ('.mp4', '.webm', '.mkv')], key=lambda p: p.stat().st_mtime, reverse=True)

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.route('/', methods=['GET', 'POST'])
def inicio():
    mensaje, error = '', False
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        parsed = urlparse(url)
        host = (parsed.hostname or '').lower()
        if parsed.scheme not in ('http', 'https') or not any(host == h or host.endswith('.' + h) for h in HOSTS):
            mensaje, error = 'Ingresa un enlace válido de una de las redes indicadas.', True
        else:
            try:
                options = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                           'outtmpl': str(DOWNLOAD_DIR / '%(title).150s [%(id)s].%(ext)s'),
                           'merge_output_format': 'mp4', 'noplaylist': True, 'restrictfilenames': True,
                           'socket_timeout': 30, 'retries': 2}
                with yt_dlp.YoutubeDL(options) as downloader:
                    downloader.download([url])
                mensaje = 'Descarga terminada. Encuentra el video en tu biblioteca.'
            except Exception:
                app.logger.exception('No se pudo descargar el video')
                mensaje, error = 'No se pudo descargar. Comprueba el enlace; la red puede exigir iniciar sesión o limitar el acceso.', True
    return render_template('index.html', title='Videoteca · Descargador', subtitle='Caso 1 / Videoteca', mensaje=mensaje, error=error, videos=videos())

@app.get('/videos/<path:filename>')
def archivo(filename):
    if filename not in [p.name for p in videos()]:
        abort(404)
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=request.args.get('guardar') == '1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
