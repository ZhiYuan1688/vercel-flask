from flask import Flask, jsonify, request
import requests
from flask_cors import CORS  # 导入 CORS

app = Flask(__name__)
CORS(app)  # 应用 CORS 到你的 Flask 应用中，允许所有域访问

@app.route('/youtube_video', methods=['GET'])
def get_youtube_video():
    video_id = request.args.get('id', 'Y-kwlvhR7Z0')  # 默认视频ID，可以通过请求参数覆盖
    api_key = 'AIzaSyDrCl2nN6bH-i-_wS_HRHGD5Y8arhuSko4'  # 你的YouTube API密钥
    url = "https://www.googleapis.com/youtube/v3/videos"
    querystring = {
        "part": "contentDetails,snippet,statistics",
        "id": video_id,
        "key": api_key
    }

    response = requests.get(url, params=querystring)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)