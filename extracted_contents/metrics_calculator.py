# © 2025 Czink Ákos József | SECUND AI Research Initiative
# Cognitive Recursive Convergence Loop Metrics Calculator

def compute_rbb(truth, believability):
    return round((truth * 0.6 + believability * 0.4), 3)

def compute_cgas(clarity, grounding):
    return round((clarity * grounding) ** 0.5, 3)

def compute_sr(stability, deviation):
    return round(stability / (1 + deviation), 3)
