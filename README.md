# munge-operator

## Description

MUNGE is an authentication service for creating and validating credentials in
high-performance computing environments.

## Usage

> Usage information is currently a work in progress. Stay tuned for more information.  

## Integrations

[Integrations](https://juju.is/docs/olm/integration) are defined in `metadata.yaml` as:

* Provides: `auth-munge`
  * The `auth-munge` integration provides the MUNGE key needed by clients.
* Requires: `munge-ready`
  * The `munge-ready` integration is used to connect the MUNGE operator to a principle HPC node operator.

## License

The MUNGE Operator is free software, distributed under the Apache Software License, version 2. See [LICENSE](./LICENSE) 
for more information.

## Security

Security issues in the MUNGE Operator can be reported through
[Launchpad](https://wiki.ubuntu.com/DebuggingSecurity#How%20to%20File). Please
do not file GitHub issues about security issues.

## Contributing

Please see the [Juju SDK documentation](https://juju.is/docs/sdk) for more information about
developing and improving the charmed MUNGE operator, and this charm's 
[contributing guidelines](./CONTRIBUTING.md) for specific contribution information.

## Other resources

- [MUNGE website](https://dun.github.io/munge/)
- [MUNGE Man Pages](https://github.com/dun/munge/wiki/Man-Pages)
- [MUNGE License](https://github.com/dun/munge/wiki/License-Info)
