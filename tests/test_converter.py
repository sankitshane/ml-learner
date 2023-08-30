def test_convert_speech_to_text():
    from athena.model import Converter

    converter = Converter()
    path = "tests/fixtures/audio.mp4"
    text = converter.speech_to_text(path)
    assert type(text) is dict
