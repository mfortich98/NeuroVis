
from types import SimpleNamespace

settings_dict = {
    'display_size': 900,
    'num_particles': 6000,
    'particle_speed': 0.005,
    'particle_tether_range': 0.05,
    'label_on': True,
    'mock_update_rate': 5,
    'mock_value_range': [0, 1],
}

settings = SimpleNamespace(**settings_dict)
