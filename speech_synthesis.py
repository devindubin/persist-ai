import os
from dotenv import load_dotenv
load_dotenv()

import azure.cognitiveservices.speech as speechsdk

# Variable names set to SPEECH_KEY and SPEECH_REGION
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#Language the voice speaks
speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)
print(os.environ.get('SPEECH_KEY'),os.environ.get('SPEECH_REGION'))
print("Enter some text that you want to speak >")
text = input()

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"Speech synthesized for text [{text}]")
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print(f"Speech synthesis canceled {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print(f"Error Details: {cancellation_details.error_details}")
            print("Did you set the speech resource key and region values?")