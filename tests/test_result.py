def test_get_result():
    # Testing to get result from file system

    from athena.model import Result

    obj = Result()
    result = obj.value

    assert result is not None
    assert type(result) is dict


def test_set_result():
    # testing to set result to json file

    from athena.model import Result

    obj = Result()

    new_result = {
        "random": "random"
    }
    obj.value = new_result

    assert obj.value is not None
    assert type(obj.value) is dict
    assert obj.value == new_result
