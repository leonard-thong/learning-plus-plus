import get_words
import get_video
import dictionary
import Speech2Text
import sys

t = sys.argv[1]

s = input("Please input Youtube URL: ")
download_vid.get_mp3(s)
transcript = Speech2Text.sample_long_running_recognize("gs://yhack-bucket/audio.flac")
with open("input.txt", "w") as file:
    file.write("%s" % transcript)
words = get_words.main()
open("dictionary.txt", "w").close()
with open("dictionary.txt", "a+") as file:
    for word in words:
        t = dictionary.main(word)
        if t is not None:
            file.write(word + ": " + t + "\n")
            print(word + ": " + t)