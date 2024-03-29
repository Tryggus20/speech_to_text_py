# followed this tutorial: https://www.youtube.com/watch?v=mYUyaKmvu6Y
# will need to 

import sys
from api_communication import *

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)
