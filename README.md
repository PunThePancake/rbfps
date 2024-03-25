# rbfps | v0.1
rbfps (Roblox FPS) utilises a current modification that can be made to the Roblox Player using:

```json
{
    "DFIntTaskSchedulerTargetFps": int
}
```

>where ```int``` is a number (eg. 144)

Feel free to modify and suggest modifications. A modern UI is indented to be implemented to make software more user friendly at a later date.

*Developed and maintained by PunThePancake please report any bugs / issues [here.](https://github.com/PunThePancake/rbfps/issues)*
# Antivirus false positive fix
[ms-settings:windowsdefender-appbrowserOpen](Windows Defender App & Browser Control Settings) and disable "Check apps and files". Feel free to enable this settings again after download is complete however be aware that after downloading windows still can pick it up as malware, to circumvent this go to windows defender or your antivirus and "Allow on device".
![[Pasted image 20240325222624.png]]
 This will prevent any false positives likely caused by the script automatically installing necessary modules for rbfps to work.
# How it works
1. Initially checks whether required modules are installed
2. Prompts user to input their desired FPS limit.
3. Automatically locates users current Roblox install.
4. Deploys .json file that sets FPS limit to inputted value from user in step 2

---

More documentation and development coming soon...
