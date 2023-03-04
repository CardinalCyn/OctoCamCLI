# OctoCam using CLI instead of an app interface
To run, install required modules, and do py app.py --c x --w y --h z, where x is the desired camera index, y is the width, and z is the height of the desired dimensions of the feed
example: py app.py --c 0 --w 640 --h 480
Use 0 as your camera index if you don't know which one.
You can pull the camera indices and device names via py app.py -cameras

To get camera indices, make a get request to 127.0.0.1/getCameras

To get the urls, once it has started, make a get request to 127.0.0.1/getUrls, which will make the urls based on the arguments passed in

The stream url is passed to: '/stream/<int:camera_index>/<int:frame_width>/<int:frame_height>'

The snapshot url is passed to '/snapshot/<int:camera_index>/<int:frame_width>/<int:frame_height>'
