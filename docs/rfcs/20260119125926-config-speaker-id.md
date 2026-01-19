20260119125926

# RFC: Configurable Default Speaker ID per Language

**Staging:** Development
**Request ZID:** 20260119125926

## Implementation Details

### Analytics
- Currently, the `--speaker` argument defaults to 0 in the CLI script, regardless of the language.
- For multi-speaker models like the Ukrainian `uk_UA-ukrainian_tts-medium`, users may want to set a specific speaker (e.g., Mykyta, ID 1) as the default for that language without specifying it every time in the command line.
- The configuration structure in `config.ini` needs to support an optional `speaker` key within each `[voice_LANG]` section.

### Decisions
- Modified `piper_tts.py` to change the `--speaker` argument default to `None`.
- Implemented logic in `piper_tts.py` to first check the `[voice_LANG]` section in `config.ini` for a `speaker` setting.
- If no `speaker` is specified in the config and no `--speaker` argument is provided in the CLI, the system defaults to speaker `0`.
- Updated `config.ini` with `speaker = 1` for the `[voice_uk]` section to set Mykyta as the default Ukrainian voice.
