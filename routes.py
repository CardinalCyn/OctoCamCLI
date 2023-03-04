"""
creates routes for app
"""
from flask import Response,request
from pygrabber.dshow_graph import FilterGraph
from utils import generate_camera_obj,generate_feed,generate_snapshot
import pythoncom

def create_routes(app,arguments):
    """
    def for creating routes
    """
    # iterates through camera list, returns list. returns objects of devices and their indices
    @app.route('/getCameras')
    def get_cameras():
        # pythoncom.CoInitialize()
        available_cameras=generate_camera_obj()
        return available_cameras
    #returns an object with the stream/snapshot links based on the arguments passed into py app.py
    @app.route('/getUrls')
    def get_urls():
        print(arguments)
        camera_index = arguments["camera_index"]
        width = arguments["width"]
        height = arguments["height"]

        stream_url = f"http://127.0.0.1:8081/stream/{camera_index}/{width}/{height}"
        snapshot_url = f"http://127.0.0.1:8081/snapshot/{camera_index}/{width}/{height}"

        return {"stream_url": stream_url, "snapshot_url": snapshot_url}
    #Returns a video feed with width/height for the camera at the given index.
    @app.route('/stream/<int:camera_index>/<int:frame_width>/<int:frame_height>')
    def video_feed(camera_index,frame_width,frame_height):
        user_agent=request.headers.get('User-Agent')
        if "SuccessCode" in user_agent:
            return Response("success")
        return Response(generate_feed(camera_index,frame_width,frame_height),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    #returns snapshot jpg with width/height for the camera at given index
    @app.route('/snapshot/<int:camera_index>/<int:frame_width>/<int:frame_height>')
    def snapshot(camera_index,frame_width,frame_height):
        user_agent=request.headers.get('User-Agent')
        if "SuccessCode" in user_agent:
            return Response("success")
        return next(generate_snapshot(camera_index,frame_width,frame_height))
