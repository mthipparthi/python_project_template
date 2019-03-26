from context import mypackage


def test_config():
    assert mypackage.config.config_1 == "config_val_2"
