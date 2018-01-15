import nipype.interfaces.mrtrix as mrt
import dipy
import os
import json

with open('config.json') as config_json:
    config = json.load(config_json)


tck2trk = mrt.MRTrix2TrackVis()
tck2trk.inputs.in_file = config["tracks"]
tck2trk.inputs.image_file = config["t1"]
tck2trk.inputs.out_filename = 'track.trk'
tck2trk.run()
