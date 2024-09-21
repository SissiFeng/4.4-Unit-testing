import pytest
from color_mixer import ColorMixer

def test_mix_colors():
    assert ColorMixer.mix_colors((255, 0, 0), (0, 255, 0)) == (255, 255, 0)
    assert ColorMixer.mix_colors((0, 0, 255), (255, 255, 0)) == (255, 255, 255)
    assert ColorMixer.mix_colors((128, 128, 128), (128, 128, 128)) == (128, 128, 128)

def test_lighten_color():
    assert ColorMixer.lighten_color((100, 100, 100), 0.5) == (178, 178, 178)
    assert ColorMixer.lighten_color((0, 0, 0), 1.0) == (255, 255, 255)
    assert ColorMixer.lighten_color((255, 255, 255), 0.1) == (255, 255, 255)

def test_darken_color():
    assert ColorMixer.darken_color((200, 200, 200), 0.5) == (100, 100, 100)
    assert ColorMixer.darken_color((255, 255, 255), 1.0) == (0, 0, 0)
    assert ColorMixer.darken_color((0, 0, 0), 0.1) == (0, 0, 0)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        ColorMixer.mix_colors((256, 0, 0), (0, 255, 0))
    with pytest.raises(ValueError):
        ColorMixer.lighten_color((100, 100, 100), 1.5)
    with pytest.raises(ValueError):
        ColorMixer.darken_color((100, 100, 100), -0.1)

# You can add more test functions as needed
