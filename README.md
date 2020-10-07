[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.22-blue.svg)](https://doi.org/10.25663/bl.app.22)

# app-converttck2trk

This service will convert a .tck file (MRtrix format) to a .trk file in dwi space using nipype. 

### Authors
- Lindsey Kitchell (kitchell@indiana.edu)

### Contributors
- Soichi Hayashi (hayashis@iu.edu)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### References 
[1. MRTrix2TrackVis](https://nipype.readthedocs.io/en/latest/interfaces/generated/interfaces.mrtrix/convert.html)

### Citation
We kindly ask that you cite the following article when publishing papers and code using this code. 

Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.22](https://doi.org/10.25663/bl.app.22) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "track": "./input/track/track.tck",
	"dwi": "./input/dtiinit/dwi.nii.gz"
}
```

If you have singularity installed on your local machine:

3. Launch the App by executing `main`

```bash
./main
```

Otherwise:

3. Ensure you have the proper dependencies installed for python and execute main.py directly. 

## Output

The main output of this App is a file called `track.trk`. 


### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.  

  - NIPYPE: https://nipype.readthedocs.io/en/latest/
  - H5PY: https://www.h5py.org/

