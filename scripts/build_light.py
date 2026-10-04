#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

ipa_url = sys.argv[1]
version = sys.argv[2]

repo = Path.cwd()
ipa_dir = repo / "ipa"
ipa_dir.mkdir(exist_ok=True)

print("Downloading decrypted IPA...")
subprocess.run([
    "curl", "-L", "--fail", "--retry", "3",
    "-o", str(ipa_dir / "input.ipa"),
    ipa_url
], check=True)

# Use the repository's own build script where possible.
# The upstream project evolves its CLI; inspect help and choose only
# flags that are actually present instead of hard-coding unsupported flags.
help_text = subprocess.run(
    ["./build.sh", "--help"],
    text=True, capture_output=True
).stdout

cmd = ["./build.sh", "--ipa", str(ipa_dir / "input.ipa"),
       "--tweak-version", version]

def add(flag, enabled=True):
    if enabled and flag in help_text:
        cmd.append(flag)

# LIGHT profile for the A9/iOS 15 test device.
add("--enable-youpip", True)
add("--enable-ytuhd", False)
add("--enable-yq", False)
add("--enable-ryd", True)
add("--enable-ytabc", False)
add("--enable-demc", False)

print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)
