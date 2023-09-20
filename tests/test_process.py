def test_input_video_urls():
    # Testing the input is a list of urls

    from athena.main import video_urls

    assert type(video_urls) is list
