###
Name of package:


### Test plan

- [ ] Tag in securedrop-workstation repository is correct: https://github.com/freedomofpress/securedrop-workstation/releases/tag/x.y.z
- [ ] Build logs are included: https://github.com/freedomofpress/build-logs/commit/1234
- [ ] CI is passing, the rpm is properly signed with the prod key
- [ ] Manually verify that the rpm is properly signed with the prod key by running `rpm -qi <rpm>` and copy pasting the Signature KEY ID into `gpg -k <KEY ID>`
- [ ] Unsigned RPM after running `rpm --delsign` (in Debian Stable) on the signed RPM results in the checksum found in the build logs
