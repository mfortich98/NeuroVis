
from types import SimpleNamespace

settings_dict = {
    # Size of the square window of the visualization
    'display_size': 900,

    # Number of particles to display
    'num_particles': 100,

    # How anchors are assigned to particles
    #   options are: random, even_odd, halves
    'anchor_assignment': "random",

    # Particle movement speed
    #   (position updates at 60fps, so keep to small numbers)
    'particle_speed': 0.0015,

    # How far from anchor value particles can move
    #   (multiplied by radius)
    #   (if set to 0, particles will stop when reach tether, instead of bounce back)
    'particle_tether_range': 0,

    # How close to the center particles get at max synch
    #   1 means they hit the center at max synch,
    #   1.5 would mean that max synch would be at half the circle
    'particle_distance_from_center': 0.5,

    # Defines if label with synch values is shown
    'label_on': False,

    # How often values are sent from the data mocking thread
    #   Measured in seconds
    'mock_update_rate': 0.1,

    # What range of values are mocked and sent to the visualization
    'mock_value_range': [0.1, 1.0]
}


settings = SimpleNamespace(**settings_dict)
