import pathlib
import shutil
import subprocess

REPO_BASE_DIR = pathlib.Path(__file__).parent
SDK_DOWNLOAD_PATH = REPO_BASE_DIR / "sdk_download"

GIT_PATH = shutil.which("git")

def fetch_latest_sdk_repo(repo_name: str, git_url: str, git_branch: str = "main") -> pathlib.Path:
    """
    Fetch the latest version of a given Git repo.

    :param repo_name: Name of repo
    :param git_url: Git URL to fetch from
    :param git_branch: Git branch to check out

    :return: Path to the cloned repo.
    """

    cloned_path = SDK_DOWNLOAD_PATH / repo_name

    if (cloned_path / ".git").is_dir():
        print(f"{repo_name} already cloned, pulling latest...")
        subprocess.check_call([GIT_PATH, "checkout", git_branch], cwd=cloned_path)
        subprocess.check_call([GIT_PATH, "pull", "origin"], cwd=cloned_path)
    else:
        print(f"Cloning {repo_name} -> {cloned_path!s} ...")
        cloned_path.mkdir(parents=True, exist_ok=True)
        subprocess.check_call([GIT_PATH, "clone", "-b", git_branch, git_url, str(cloned_path)])

    return cloned_path


# Download SDKs
mcux_sdk_core_path = fetch_latest_sdk_repo("mcuxsdk-core", "https://github.com/nxp-mcuxpresso/mcuxsdk-core.git")
mcux_devices_rt_path = fetch_latest_sdk_repo("mcux-devices-rt", "https://github.com/nxp-mcuxpresso/mcux-devices-rt.git")
mcux_devices_lpc_path = fetch_latest_sdk_repo("mcux-devices-lpc", "https://github.com/nxp-mcuxpresso/mcux-devices-lpc.git")
mcux_devices_kinetis_path = fetch_latest_sdk_repo("mcux-devices-kinetis", "https://github.com/nxp-mcuxpresso/mcux-devices-kinetis.git")
legacy_mcux_sdk_path = fetch_latest_sdk_repo("legacy-mcux-sdk", "https://github.com/nxp-mcuxpresso/legacy-mcux-sdk.git")

# Copy MCU headers
devices_path = REPO_BASE_DIR / "devices"
devices_path.mkdir(exist_ok=True)
(devices_path / "kinetis").mkdir(exist_ok=True)

# Kinetis MCUs
shutil.copytree(mcux_devices_kinetis_path / "K" / "MK22F51212", devices_path / "kinetis" / "MK22F51212", dirs_exist_ok=True)
shutil.copytree(mcux_devices_kinetis_path / "K" / "periph20", devices_path / "kinetis" / "MK22F51212" / "periph", dirs_exist_ok=True)

# Legacy Kinetis MCUs
shutil.copytree(legacy_mcux_sdk_path / "devices" / "MKW41Z4", devices_path / "kinetis" / "MKW41Z4", dirs_exist_ok=True)
shutil.copytree(legacy_mcux_sdk_path / "devices" / "MK64F12", devices_path / "kinetis" / "MK64F12", dirs_exist_ok=True)
shutil.copytree(legacy_mcux_sdk_path / "devices" / "MK66F18", devices_path / "kinetis" / "MK66F18", dirs_exist_ok=True)
shutil.copytree(legacy_mcux_sdk_path / "devices" / "MK82F25615", devices_path / "kinetis" / "MK82F25615", dirs_exist_ok=True)

# i.MXRT MCUs
shutil.copytree(mcux_devices_rt_path / "RT1050" / "MIMXRT1052", devices_path / "mimxrt" / "MIMXRT1052", dirs_exist_ok=True)
shutil.copytree(mcux_devices_rt_path / "RT1050" / "periph", devices_path / "mimxrt" / "MIMXRT1052" / "periph", dirs_exist_ok=True)
shutil.copytree(mcux_devices_rt_path / "RT1060" / "MIMXRT1062", devices_path / "mimxrt" / "MIMXRT1062", dirs_exist_ok=True)
shutil.copytree(mcux_devices_rt_path / "RT1060" / "periph", devices_path / "mimxrt" / "MIMXRT1062" / "periph", dirs_exist_ok=True)
shutil.copytree(mcux_devices_rt_path / "RT1170" / "MIMXRT1176", devices_path / "mimxrt" / "MIMXRT1176", dirs_exist_ok=True)
shutil.copytree(mcux_devices_rt_path / "RT1170" / "periph", devices_path / "mimxrt" / "MIMXRT1176" / "periph", dirs_exist_ok=True)
shutil.copytree(mcux_devices_rt_path / "RT1180" / "MIMXRT1189", devices_path / "mimxrt" / "MIMXRT1189", dirs_exist_ok=True)
shutil.copytree(mcux_devices_rt_path / "RT1180" / "periph", devices_path / "mimxrt" / "MIMXRT1189" / "periph", dirs_exist_ok=True)

# LPC MCUs
shutil.copytree(mcux_devices_lpc_path / "LPC54000" / "LPC54628", devices_path / "lpc" / "LPC54628", dirs_exist_ok=True)

# Legacy LPC MCUs
shutil.copytree(legacy_mcux_sdk_path / "devices" / "LPC54114", devices_path / "lpc" / "LPC54114", dirs_exist_ok=True)

# Drivers
# This list is the sum total of all MCUX SDK drivers need by any and all NXP MCUs supported by Mbed.
# Upper-level CMake code is responsible for adding the correct drivers to the correct MCUs.
needed_fsl_hal_drivers = [
    "common",

    # Communications
    "lpi2c", # All RT & most Kinetis MCUs
    "lpspi", # All RT & some Kinetis MCUs
    "lpuart", # All RT & most Kinetis MCUs
    "flexio", # All RT & Kinetis MCUs
    "i2c", # Kxx
    "spi", # KL43Z
    "uart", # Kxx
    "dspi", # K6x

    # Audio (not currently used by Mbed)
    "sai", # KL43Z

    # ADCs
    "adc16", # KL43Z
    "adc_12b1msps_sar", # MIMXRT10xx
    "adc_etc", # MIMXRT10xx

    # Other analog
    "cmp", # KL43Z
    "dac", # KL43Z
    "vref", # Kxx

    # Power & general control
    "dcdc_1", # MIMXRT10xx
    "gpc_1", # MIMXRT10xx
    "snvs_lp", # MIMXRT10xx
    "pmc", # KL43Z
    "rcm", # Kxx
    "smc", # Kxx
    "sim", # K6x

    # DMA
    "edma", # Kxx & RT
    "dmamux", # All RT & Kinetis MCUs
    "dma", # KL43Z

    # Network
    "enet", # MIMXRT10xx

    # GPIO
    "igpio", # MIMXRT10xx
    "gpio", # Kxx
    "llwu", # Kxx
    "port", # KL43Z

    # Timing
    "qtmr_1", # MIMXRT10xx
    "pwm", # MIMXRT10xx
    "gpt", # MIMXRT10xx
    "pit", # All RT & Kinetis MCUs
    "lptmr", # KL43Z
    "rtc", # KL43Z
    "tpm", # KL43Z
    "cmt", #K6x
    "ftm", #K6x

    # Watchdogs
    "cop", # KL43Z
    "rtwdog", # MIMXRT
    "wdog01", # MIMXRT10xx
    "wdog", # K6x

    # Flash memory
    "dsc_flash", # KL43Z
    "flexspi", # MIMXRT
    "flash", #K6x

    # Interconnects
    "xbara", # MIMXRT105x_6x

    # RNG
    "trng", # MIMXRT105x_6x
    "rnga", # K6x

    # Security
    "sysmpu", # K6x

    # CRC
    "crc" # K6x
]

drivers_path = REPO_BASE_DIR / "drivers"
drivers_path.mkdir(exist_ok=True)
for driver in needed_fsl_hal_drivers:
    shutil.copytree(mcux_sdk_core_path / "drivers" / driver, drivers_path / driver, dirs_exist_ok=True)

# Apply patch files
for patch_file in sorted((REPO_BASE_DIR / "patches").glob("*.patch")):
    print(f"Applying {patch_file.name}...")
    subprocess.check_call([GIT_PATH, "apply", "--ignore-whitespace", str(patch_file.absolute())], cwd=REPO_BASE_DIR)