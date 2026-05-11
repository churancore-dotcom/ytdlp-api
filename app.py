from flask import Flask, request, jsonify
import yt_dlp, os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'yt-dlp API running'})

@app.route('/extract')
def extract():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'url required'}), 400
    ydl_opts = {'format': 'bestaudio/best', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return jsonify({'audio_url': info['url'], 'title': info['title']})
        port = int(os.environ.get('PORT', 8080))
app.run(host='0.0.0.0', port=port)
