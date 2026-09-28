# CLOCK

## [2.5.4]

- Improvements
  - Added lost comments for some enumerations.

## [2.5.3]

- Bug Fixes
  - Fixed violations of MISRA C-2012 rule 18.1 and rule 5.7.

## [2.5.2]

- Bug Fixes:
  - Fixed violations of MISRA C-2012 violation rules: 10.1, 10.3.
  - Fixed IAR warning Pa082 for the clock driver.

## [2.5.1]

- Bug Fix:
  - Correct the access time when 180MHz < Freq <= 220MHz in CLOCK_SetFLASHAccessCyclesForFreq.

## [2.5.0]

- New feature:
  - Moved SDK_DelayAtLeastUs function from clock driver to common driver.

## [2.4.0]

- Replace the delay function

## [2.3.0]

- Optimization:
  - remove some peripheral clock parameters in CLOCK_GetFreq function

## [2.2.0]

- New Feature:
  - add new APIs including CLOCK_GetEmcClkFreq and CLOCK_GetMCanClkFreq to replace CLOCK_GetFreq(kCLOCK_MCAN0) and CLOCK_GetFreq(kCLOCK_EMC)

## [2.1.0]

- New feature
  - Adding new API CLOCK_DelayAtLeastUs() implemented by DWT to allow users set delay in unit of microsecond.

## [2.0.5]

- Bug Fix:
  - Correct the return frequency of CLOCK_GetFrgClkFreq.
  - Fix the bug in function CLOCK_GetPllConfig() to refine the cache feature.
  - Fix C++ build errors in CLOCK_GetClockAttachId() and CLOCK_AttachClk().

## [2.0.4]

- Bug Fix:
  - Update the second clock source to Flexcomm from fro_hf to fro_hf_div.

## [2.0.3]

- Bug Fix:
  - Fix attach incorrect attach_id.

## [2.0.2]

- New Feature:
  - add get actual clock attach id api to allow users to obtain the actual
    clock source in target register.
- Bug Fix:
  - The attach clock and get actual clock attach id apis should check
    combination of two clock source.
- Optimization:
  - Make the judgement statments more clear.
  - Strengthen the compatibility of clock attatch id.
  - Remove some unmeaningful definitions and add some useful ones to
    enhance readability.

## [2.0.1]

- some minor fixes.

## [2.0.0]

- initial version.
