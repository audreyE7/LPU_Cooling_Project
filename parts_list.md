# Parts List (Budget Loop)

Below are example components; feel free to substitute equivalents you already have.

| Component | Example Spec | Notes |
|---|---|---|
| Mini DC pump | 12 V, ~240 L/h | Any small PC water‑cooling pump works |
| Cold plate (water block) | Copper or Al, 1/4" barbs | Mount to heat source (resistor or Peltier) |
| Tubing | 1/4" ID silicone, 1–2 m | Add clamps or zip ties for safety |
| Reservoir | Small bottle/cup | Keep inlet submerged to avoid cavitation |
| Radiator (optional) | 120 mm PC rad + fan | Not required for short tests |
| Heat source | 5–30 W power resistor *or* Peltier | Power via DC supply; heats the cold plate |
| Thermocouples | 2× Type‑K + MAX6675/31855 | Inlet and outlet coolant temperatures |
| Microcontroller | Arduino Uno/Nano | USB power + serial logging |
| Flow sensor (optional) | Hall‑effect, G1/4 | Or measure manually by timed volume |
| Power supply | 12 V DC (≥3 A) | For pump + heat source |

## Loop Schematic
Reservoir → Pump → Cold Plate (on heat source) → (Radiator) → Reservoir

### Safety
- Leak‑test with water first; keep electronics above/beside the loop.
- Do not touch powered resistors or exposed wiring; avoid short circuits.
- Add a towel tray or bin under the setup for splash protection.
