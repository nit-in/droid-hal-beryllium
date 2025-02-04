# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device beryllium
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty PocoF1
%define droid_target_aarch64 1

%define installable_zip 1

%define straggler_files \
/acct \
/cache \
/config \
/d \
/data \
/dev \
/mnt \
/odm \
/oem \
/proc \
/res \
/storage \
/sys \
/system \
/vendor \
/bt_firmware \
/bugreports \
/charger \
/default.prop \
/dsp \
/etc \
/firmware \
/persist \
/product \
/sdcard \
%{nil}

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define makefstab_skip_entries /sys/fs/pstore

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

