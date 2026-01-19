# Release Notes

All notable changes to this project will be documented in this file.

## [1.48.2] - 2026-01-19

### Added
-   **Ukrainian Support**: Added Support for the Ukrainian language (`uk`) using the `uk_UA-ukrainian_tts-medium` model. (ZID: 20260119125718)
-   **Configurable Default Speaker**: Added the ability to set a default speaker ID per language in `config.ini` using the `speaker` key. (ZID: 20260119125926)
-   **Multi-Speaker Support**: Clarified usage of the `--speaker` parameter to select different voices within a model (e.g., Mykyta voice for Ukrainian).

### Changed
-   **Environment**: Removed `config.ini` from the git index to ensure local path settings are not tracked. (ZID: 20260119130345)
