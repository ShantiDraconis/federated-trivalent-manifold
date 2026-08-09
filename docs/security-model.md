# Security model

## Assets

- Quest video/audio stream;
- ADB authorization and device serial;
- encryption master material;
- audit records;
- local ingest endpoint.

## Trust boundaries

The headset, host, OBS/FFmpeg process, network relay and any model provider are
distinct principals. No theorem about K3 or RH establishes confidentiality
across those boundaries.

## Controls

- never place secrets in source, command lines or logs;
- no shell interpolation for device identifiers or URLs;
- derive independent keys with distinct HKDF `info` contexts;
- AES-GCM nonces must be unique for each key;
- fail closed if the cryptography package is absent;
- make teardown idempotent and record each attempted step;
- bind local services to loopback unless remote access is explicitly required;
- authenticate and encrypt any non-loopback transport.

## Non-guarantees

The abstract theorem `teardown_closes_modelled_port` proves a field update in a
small state machine. It does not prove that an Android service, firewall or
physical radio changed state. Runtime evidence is still required.
