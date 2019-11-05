# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device beryllium
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty PocoF1
%define droid_target_aarch64 1

%define installable_zip 1

%define straggler_files \
/d \
/bt_firmware \
/bugreports \
/cache \
/charger \
/default.prop \
/d \
/dsp \
/etc \
/firmware \
/odm \
/persist \
/product \
/sdcard \
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

