# RPi Camera
# DATE: 2021-02-11
# DESCRIPTION: Access the RPi (v2) Camera for streaming

import time
import io
import threading
import picamera

class Camera(object):
    thread = None #bg thread for cam
    frame = None # current frame stored by bg thread
    last_access = 0 # time of last client access to the camera
    
    def initialize(self):
        if Camera.thread is None:
            #start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            #wait frame to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame
    
    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            #setup
            camera.resolution = (640, 480)
            camera.hflip = True
            camera.vflip = True

            # warm up cam
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                
                #store frame
                stream.seek(0)
                cls.frame = stream.read()

                # reset stream for next frame 
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in last 10 seconds 
                # stop thread
                if time.time() - cls.last_access > 10:
                    break
        cls.thread = None