# Threshold Prism Bleed — research basis

`ATD-FX-001` is a stylized production compositor, not a physically exact optical simulator.

Research used for the design:
- NASA Science, **Wave Behaviors**: diffraction is the bending/spreading of waves around obstacles; scattering redirects light in multiple directions; wavelength and material/geometry affect the visible result. https://science.nasa.gov/ems/03_behaviors/
- NASA Science, **Webb's Diffraction Spikes**: diffraction patterns depend on aperture/edge geometry and support structures. https://science.nasa.gov/asset/webb/webbs-diffraction-spikes/

Production translation:
1. confine spectral separation to illuminated threshold edges;
2. use multi-scale bloom for scattering-like light spread;
3. emit anisotropic rays from the door geometry rather than a full-frame rainbow overlay;
4. allow a low-opacity alternate-room exposure only inside the threshold opening;
5. preserve the underlying composition and traveler silhouette.

The effect's truthful claim is therefore: **optics-inspired localized spectral threshold compositor**.
