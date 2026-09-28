# Mbed MCUX SDK Repo

This repo contains the pieces of the MCUX SDK needed to build the NXP chips present in Mbed OS.

## Importing the SDK
The latest (main branch) of the SDK can be imported by running

```
python3 import-mcux-sdk.py
```

## Creating Patches
If you need to change part of the SDK for its inclusion in Mbed OS, follow the following steps.

1. Make the desired change, and only the desired change, to the source files here.
2. Run one of the following commands to save as a patch file
    ```
    $ git diff . > patches/xx-my-patch.patch
    ```
    (Bash)
    ```
    PS > git diff . | Set-Content -Encoding utf8 patches\xx-my-patch.patch
    ```
    (Windows PowerShell)
3. Commit the patch file and the changes to the MCUX SDK code. The patch file should be automatically picked up by the importer script.