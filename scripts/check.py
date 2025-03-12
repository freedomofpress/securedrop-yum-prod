#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
import json

PROD_SIGNING_KEY_PATH = "pubkeys/prod.key"
PROD_SIGNING_KEY_PATH_LEGACY = "pubkeys/prod-legacy.key"

RPM_DIR = "workstation"


def check_unsigned_rpm(path):
    subprocess.check_call(["rpm", "--delsign", path])
    subprocess.check_call(["sha256sum", path])


def check_unsigned_all_rpms():
    for root, dirs, files in os.walk(RPM_DIR):
        for name in files:
            check_unsigned_rpm(os.path.join(root, name))


def verify_sig_rpm(path):
    for key_path in [PROD_SIGNING_KEY_PATH, PROD_SIGNING_KEY_PATH_LEGACY]:
        try:
            subprocess.check_call(["rpmkeys", "--import", key_path])
        except subprocess.CalledProcessError as e:
            fail("Error importing key: {}".format(str(e)))

    # Check the signature
    try:
        output = subprocess.check_output(["rpm", "--checksig", path])
        # rpm --checksig returns 0 if there is *no* signature. I couldn't
        # find a way other than parsing stdout
        line = output.decode("utf-8").rstrip()
        print(line)
        expected_output = "{}: digests signatures OK".format(path)
        if line != expected_output:
            fail("Signture verification failed for {}:{}".format(expected_output, line))
    except subprocess.CalledProcessError as e:
        fail("Error checking signature: {}".format(str(e)))


def verify_all_rpms():
    for root, dirs, files in os.walk(RPM_DIR):
        for name in files:
            verify_sig_rpm(os.path.join(root, name))


def remove_keys_in_rpm_keyring():
    rpm_keys_exist = False
    try:
        # Returns non-zero if no keys are installed
        subprocess.check_call(["rpm", "-q", "gpg-pubkey"])
        rpm_keys_exist = True
    except subprocess.CalledProcessError:
        rpm_keys_exist = False

    # If a key is in the keyring, delete it
    if rpm_keys_exist:
        try:
            subprocess.check_call(["rpm", "--erase", "--allmatches", "gpg-pubkey"])
        except subprocess.CalledProcessError as e:
            fail("Failed to delete key: {}".format(str(e)))


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-unsigned", action="store_true", default=False)
    parser.add_argument("--verify", action="store_true", default=True)
    parser.add_argument("--all", action="store_true", default=False)
    parser.add_argument("packages", type=str, nargs="*", help="Files to sign/verify")
    args = parser.parse_args()

    # Fail if no package is specified or not using '--all'
    if not args.all and not args.packages:
        fail("Please specify a rpm package or --all")
    # Since we can't specify with which key to check sigs, we should clear the keyring
    remove_keys_in_rpm_keyring()

    if args.check_unsigned:
        output = subprocess.check_call(["rpm", "--version"])
        if args.all:
            check_unsigned_all_rpms()
        else:
            for package in args.packages:
                assert os.path.exists(package)
                check_unsigned_rpm(package)

    elif args.verify:
        if args.all:
            verify_all_rpms()
        else:
            for package in args.packages:
                assert os.path.exists(package)
                verify_sig_rpm(package)

    sys.exit(0)


if __name__ == "__main__":
    main()
