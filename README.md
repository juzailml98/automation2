# automation2
<p>This project implemements drowsiness detection of drivers using cnn that runs on a raspberry pi4.</p>
<p>the require modules necessary to run the codeset are</p>
<ol>
  <li>pygame</li>
  <li>numpy</li>
  <li>tensorflow/keras</li>
  <li>opencv2</li>
  <li>matplotlib</li>
  <li>picamera</li>
</ol>
<p>the raspberry pi captures the livestream of drivers face.then video is segmented into frames using opencv.the face and eyes are detected from frames using haarcascade.the image of eye detected by haar cascade is passed through a cnn to detect whether eyes are opened or closed.if the eyes are closed or if the face is not detected then the counter set for alarm increments for each frame.if the counter reach a threshold value(50) then buzzer or sound is activated by raspberry pi.</p>



