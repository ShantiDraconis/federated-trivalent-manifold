# FTM operational runtime simulator

This directory is not an operating system or kernel. It is a user-space state
machine demonstrating the same regulator transition as the formal proofs.

A real operating system would additionally require boot code, memory and
process isolation, scheduling, drivers, filesystems, networking, access
control, update/recovery, threat modeling, and hardware-specific verification.
None of those properties follows from monotonicity of the regulator.
