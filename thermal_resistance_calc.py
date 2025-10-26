#!/usr/bin/env python3

"""
Compute basic thermal metrics from a CSV log:
time_s,T_in_C,T_out_C,deltaT_C,flow_L_min,power_W

Outputs summary to stdout and writes a simple plot if matplotlib exists.
"""
import sys, csv, math, statistics as stats

def load_rows(path):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        rows = [{
            "t": float(r["time_s"]),
            "Tin": float(r["T_in_C"]),
            "Tout": float(r["T_out_C"]),
            "dT": float(r["deltaT_C"]),
            "flow": float(r.get("flow_L_min", 0) or 0),
            "power": float(r.get("power_W", 0) or 0),
        } for r in reader]
    return rows

def summarize(rows):
    if not rows:
        print("No data rows.")
        return
    Tin = [r["Tin"] for r in rows]
    Tout = [r["Tout"] for r in rows]
    dT = [r["dT"] for r in rows]
    P = [r["power"] for r in rows]

    def safe_mean(v):
        v2 = [x for x in v if x==x]
        return sum(v2)/len(v2) if v2 else float("nan")

    mTin, mTout, mdT, mP = map(safe_mean, (Tin, Tout, dT, P))
    Rth = (mdT / mP) if (mP and mP==mP) else float("nan")

    print(f"Samples: {len(rows)}")
    print(f"Avg T_in:  {mTin:.2f} C")
    print(f"Avg T_out: {mTout:.2f} C")
    print(f"Avg ΔT:    {mdT:.2f} C")
    print(f"Avg Power: {mP:.2f} W")
    print(f"Thermal Resistance (ΔT/P): {Rth:.4f} K/W")

    # If flow given, estimate coolant heat pickup (energy balance)
    flows = [r["flow"] for r in rows if r["flow"]>0]
    if flows:
        rho = 997.0           # kg/m^3
        cp  = 4182.0          # J/kg-K (water)
        # Convert L/min to kg/s
        m_dot = sum([f/1000.0/60.0 * rho for f in flows]) / len(flows)
        Qdot = m_dot * cp * mdT  # W
        print(f"Estimated m_dot: {m_dot:.5f} kg/s")
        print(f"Coolant Q̇ (m·cp·ΔT): {Qdot:.2f} W (compare to electrical power)")

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage: python thermal_resistance_calc.py path/to/data.csv")
        sys.exit(1)
    rows = load_rows(sys.argv[1])
    summarize(rows)
