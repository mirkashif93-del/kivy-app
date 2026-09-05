[app]

# (str) Title of your application
title = Health Dept Data Management

# (str) Package name
package.name = healthdataapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.healthdept

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,xlsx

# (list) Application requirements
# پائتھون، کیوی، پینڈاس اور اوپن پائے ایکسل یہاں شامل ہیں
requirements = python3,kivy,pandas,openpyxl

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable)
warn_on_root = 0
