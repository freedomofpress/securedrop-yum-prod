# securedrop-workstation-prod-rpm-packages-lfs

Repository for storing stable builds of [SecureDrop Workstation](https://github.com/freedomofpress/securedrop-workstation)
packages for distribution to production Workstation installs. The packages here are RPMs, intended for installation
in `dom0` within [QubesOS](https://qubesos.org/)

## git-lfs

The repository requires use of [git-lfs](https://git-lfs.github.com/) to store large files.

## Publishing packages

Merging into the `main` branch will automatically deploy packages to
https://yum.securedrop.org/. Publishing happens every 15m.
