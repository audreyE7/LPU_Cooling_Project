# Analysis

Use `thermal_resistance_calc.py` to summarize your CSV logs:

```bash
python thermal_resistance_calc.py ../hardware/data_samples.csv
```

It reports:
- Average inlet/outlet temperatures and ΔT
- Thermal resistance Rθ = ΔT / Power (K/W)
- If flow is provided, coolant energy balance Q̇ = m·c_p·ΔT

You can paste outputs and plots into your report or README.
