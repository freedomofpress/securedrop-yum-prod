## Description

Package being released: `securedrop-workstation-dom0-config x.y.z`
Package tag: https://github.com/freedomofpress/securedrop-workstation/releases/tag/x.y.z
Build logs: https://github.com/freedomofpress/build-logs/commit/1234
Prod signing key used to sign package and tag: https://github.com/freedomofpress/securedrop-workstation-prod-rpm-packages-lfs/blob/HEAD/pubkeys/prod.key

Release tracking issue: https://github.com/freedomofpress/securedrop-workstation/issues/1234

## Checklist for PR owner

- [ ] Links in this PR template have been updated as required
- [ ] https://github.com/freedomofpress/securedrop-workstation-prod-rpm-packages-lfs/blob/HEAD/pubkeys/prod.key points to the correct prod signing key

## Checklist for reviewer
- [ ] CI is passing
- [ ] The build logs show that the tag is verified and signed with the prod signing key
- [ ] The build logs show that the tag is checked out and used to build the RPM
- [ ] The tag in the build logs is the correct tag: https://github.com/freedomofpress/securedrop-workstation/releases/tag/x.y.z
- [ ] The commits being released are what you expect (see https://github.com/freedomofpress/securedrop-workstation/compare/a.b.c...x.y.z)
- [ ] The build logs show that the RPM is signed with the prod signing key
    > * Download the signed RPM from this PR
    > * Run `rpm qi <signed-rpm>` to get the KEY ID
    > * Run `gpg -k <KEY ID>` to verify that it matches the prod signing key (make sure you have the prod signing key referenced in the PR description in your GPG keyring)
- [ ] The Unsigned RPM checksum matches what's in the build logs
    > * Download the signed RPM from this PR (if you haven't already)
    > * Run `rpm --delsign <signed-rpm>` to remove the signature
    > * Run `sha256sum <unsigned-rpm>` and compare
