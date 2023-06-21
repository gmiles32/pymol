from pymol import cmd 

def matte():
    cmd.set('ray_trace_mode', 0)
    cmd.set('spec_reflect', 0)
    cmd.set('spec_power', 1500)
    cmd.set('ambient', 0)
    cmd.set('hash_max', 300)
    cmd.set('antialias', 2)
    cmd.set('depth_cue', 1)
    cmd.set('ray_texture', 1)
    cmd.bg_color('black')
    cmd.set('opaque_background', 1)

cmd.extend('matte', matte)