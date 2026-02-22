[app]
title = My Camera App
package.name = mycameraapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET, CAMERA, RECORD_AUDIO
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
[buildozer]
log_level = 2
warn_on_root = 1
