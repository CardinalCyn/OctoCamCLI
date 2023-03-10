import argparse
from flask import Flask
from utils import generate_camera_obj
import routes

app = Flask(__name__)

# Set up argparse to take in camera index, width, and height through the command line
parser = argparse.ArgumentParser(
    description='Run a Flask server for streaming video and generating snapshots from a camera.')
parser.add_argument('--c', type=int, default=None, help='Index of the camera to use')
parser.add_argument('--w', type=int, default=None, help='Width of the video feed')
parser.add_argument('--h', type=int, default=None, help='Height of the video feed')
parser.add_argument('-cameras', action='store_true', help='List available cameras')

args = parser.parse_args()

# Handle the -cameras flag
if args.cameras:
    # print all camera indices, camera names
    available_cameras = generate_camera_obj()
    for camera in available_cameras:
        print(camera + ": " + str(available_cameras[camera]))
    exit()

# Check if the required arguments have been provided
if not all([args.c is not None, args.w is not None, args.h is not None]):
    print("All positional arguments --c --w --h are required")
    parser.print_help()
    exit()

# Start the Flask server with the given camera index, width, and height
if __name__ == '__main__':
    arguments = {"camera_index":args.c, "width":args.w, "height":args.h}
    routes.create_routes(app, arguments)
    app.run(host='0.0.0.0', port=8081, debug=True, extra_files=None)
