from google.cloud import speech_v1
from google.cloud.speech_v1 import enums


def sample_long_running_recognize(storage_uri):
    client = speech_v1.SpeechClient.from_service_account_json(
        "/Users/leonard/Projects/lecturepp/engine/YHack-f32eab9971d3.json")

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "en-US"

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    config = {
        "language_code": language_code,
        "encoding": encoding,
        "audio_channel_count": 2,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        return alternative.transcript


if __name__ == '__main__':
    sample_long_running_recognize("gs://yhack-bucket/audio.flac")
