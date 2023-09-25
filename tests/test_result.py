def test_get_result(mock_json_load):
    # Testing to get result from file system

    from athena.model import Result

    obj = Result()
    result = obj.value

    assert result is not None
    assert type(result) is dict


def test_save_summary(mock_url_without_cc, mock_json_load, mock_open_file):
    # Testing saving the generated summary in result

    from athena.model import Result

    result = Result()

    summary = "Dummy summary of the video"
    model = "facebook/cnn"
    result.save_summary(mock_url_without_cc, summary, model)

    res = result.value
    assert type(res[mock_url_without_cc]) is dict
    assert res[mock_url_without_cc]["summary"] == summary
    assert res[mock_url_without_cc]["model"] == model
    assert "timestamp" in res[mock_url_without_cc]
    assert res[mock_url_without_cc]["timestamp"] is not None
