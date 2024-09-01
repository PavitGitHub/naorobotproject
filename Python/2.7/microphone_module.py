import unittest
from mock import MagicMock, patch
import sys

sys.path.append('/Users/xiaokan/Desktop/it project/naorobotproject/Python/2.7/pynaoqi-python2.7-2.8.6.23-mac64-20191127_144231 2/lib/python2.7/site-packages')
from naoqi import ALProxy

class TestNaoFunctionality(unittest.TestCase):

    @patch('naoqi.ALProxy')
    def test_microphone_data_retrieval(self, MockALProxy):
        # Mocking the ALAudioDevice proxy for microphone
        mock_audio_proxy = MagicMock()
        mock_audio_proxy.getFrontMicEnergy.return_value = [0.1, 0.2, 0.3, 0.4]

        # Return the mocked audio proxy when ALProxy is called
        MockALProxy.return_value = mock_audio_proxy

        # Use the mock instead of trying to connect to the actual robot
        audio_proxy = MockALProxy("ALAudioDevice", "127.0.0.1", 9559)

        # Test getting microphone energy levels
        mic_energy = audio_proxy.getFrontMicEnergy()
        self.assertEqual(mic_energy, [0.1, 0.2, 0.3, 0.4])

        # Verify that the microphone function was called
        mock_audio_proxy.getFrontMicEnergy.assert_called_once()

        # Simulate setting client preferences
        audio_proxy.setClientPreferences("python_client", 16000, 0, 0)
        mock_audio_proxy.setClientPreferences.assert_called_once_with("python_client", 16000, 0, 0)

        # Simulate unsubscribing
        audio_proxy.unsubscribe("python_client")
        mock_audio_proxy.unsubscribe.assert_called_once_with("python_client")

    @patch('naoqi.ALProxy')
    def test_speaker_functionality(self, MockALProxy):
        # Mocking the ALAudioDevice proxy for speaker
        mock_audio_proxy = MagicMock()
        
        # Return the mocked audio proxy when ALProxy is called
        MockALProxy.return_value = mock_audio_proxy

        # Use the mock instead of trying to connect to the actual robot
        audio_proxy = MockALProxy("ALAudioDevice", "127.0.0.1", 9559)

        # Test setting speaker volume
        audio_proxy.setVolume(50)

        # Verify that the speaker volume was set
        mock_audio_proxy.setVolume.assert_called_once_with(50)

    @patch('naoqi.ALProxy')
    def test_speech_synthesis(self, MockALProxy):
        # Mocking the ALTextToSpeech proxy
        mock_tts_proxy = MagicMock()
        
        # Return the mocked tts proxy when ALProxy is called
        MockALProxy.return_value = mock_tts_proxy

        # Use the mock instead of trying to connect to the actual robot
        tts_proxy = MockALProxy("ALTextToSpeech", "127.0.0.1", 9559)

        # Test speech synthesis
        tts_proxy.say("Hello, I am NAO robot.")

        # Verify that the say method was called
        mock_tts_proxy.say.assert_called_once_with("Hello, I am NAO robot.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
