import cv2
def resize(input, output, scale=50):
    # Opening the file to read
    video_capture = cv2.VideoCapture(input)

    #Getting the Frame width and height of the Video
    Fwidth = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    Fheight = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # New Dimensions calculation
    new_width = int(Fwidth * scale / 100)
    new_height = int(Fheight * scale / 100)

    # Creating a VideoWriter object in order to save the resized video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output, fourcc, 20.0, (new_width, new_height))
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Frame resizing
        resizedF = cv2.resize(frame, (new_width, new_height))

        # Writing the resized frame to the output video
        out.write(resizedF)

    # Freeing/Releasing the video objects
    video_capture.release()
    out.release()
    print("The video was successfully resized!")

input = 'D:\Coding\Python programmming\summer_school\color_vid.mp4'
output = 'resized_color.mp4'
resize(input, output, scale=50)