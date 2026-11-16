from scipy.optimize import root_scalar

# Initial investment followed by annual cash inflows (PDF Baseline)
cash_flows = [-10000, 3000, 3500, 4000, 2500]

def npv(rate):
    return sum(
        cf / (1 + rate) ** t
        for t, cf in enumerate(cash_flows)
    )

def d_npv(rate):
    return sum(
        -t * cf / (1 + rate) ** (t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method:  {secant.root:.6%}")
print(f"NPV at Newton solution:   {npv(newton.root):.6f}")

# Parameter Modification (Item C): Increase final year cash inflow from 2500 to 4500
cash_flows_mod = [-10000, 3000, 3500, 4000, 4500]
def npv_mod(rate):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows_mod))
def d_npv_mod(rate):
    return sum(-t * cf / (1 + rate) ** (t + 1) for t, cf in enumerate(cash_flows_mod) if t > 0)

newton_mod = root_scalar(npv_mod, fprime=d_npv_mod, x0=0.10, method="newton", xtol=1e-12)
print(f"\nModified IRR (Year 4 cash flow = 4500): {newton_mod.root:.6%}")