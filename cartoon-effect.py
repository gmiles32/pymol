from pymol import cmd 

def cartoon():
    cmd.set('ray_trace_mode', 3)
    cmd.set('ray_texture', 5)
    cmd.bg_color('white')
    cmd.set('ambient', 0.2)
    cmd.set('spec_reflect', 2)
    cmd.set('spec_power', 500)
    cmd.set('ray_trace_gain', 3)
    cmd.set('antialias', 2)
    cmd.set('hash_max', 300)

cmd.extend('cartoon', cartoon)
