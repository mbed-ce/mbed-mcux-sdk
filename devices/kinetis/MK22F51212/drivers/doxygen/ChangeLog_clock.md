# CLOCK

## [2.5.3]

- Bug Fixes
  - Fixed an issue that in CLOCK_SetFbeMode() C4 register not updated.

## [2.5.2]

- Bug Fixes
  - Fixed violations of MISRA C-2012 rule 18.1.

## [2.5.1]

- Bug Fixes
  - Fixed violations of MISRA C-2012 rule 10.1, rule 10.8, rule 12.2 and so on.

## [2.5.0]

- New Features
  - Moved SDK_DelayAtLeastUs function from clock driver to common driver.
  - Fixed IAR warning Pa082 for the clock driver.

## [2.4.0]

- New Features
  - Added two APIs to set slow and fast internal reference clock variable.

## [2.3.0]

- Bug Fixes
  - Fixed the issue for MISRA-2012 check.
    - Fixed rule 10.4, rule 10.1, rule 10.6, rule 13.5, rule 10.8.
  - Fixed incorrect External Oscillator Configuration sequence and ensure oscillator
    configuration be executed before it be enabled.
- New Features
  - Added new API CLOCK_DelayAtLeastUs() implemented by DWT to allow users set delay in unit of microsecond.

## [2.2.1]

- Bug Fixes
  - Fixed the issue that MCG could not switch to FEE/FBE/PBE modes when
    OSCERCLK clock not enabled.

## [2.2.0]

- New Features
  - Updated CLOCK_SetFeiMode/CLOCK_SetFbiMode/CLOCK_BootToFeiMode()
    to support set MCG_C4[DMX32]=1 in FEI/FBI modes.
- Bug Fixes
  - Updated IP_CLOCKS array, remove unused gates and add missing gates.

## [2.1.0]

- Other Changes
  - Merged fsl_mcg and fsl_osc into fsl_clock.

## [2.0.0]

- Initial version.
