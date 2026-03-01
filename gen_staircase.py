"""
CHB multilevel PWM summation figure — n = 1, 2, 3, 4 cells
Unipolar sinusoidal PWM, phase-shifted carriers (360/n degrees apart), fc = 6f
fc = 6f chosen so each PWM block is wide enough to read the error height clearly.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

FC_RATIO = 6
M        = 0.95
Vdc      = 1.0
N        = 7200    # 1200 pts per carrier cycle

theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
t     = theta / (2 * np.pi)

def triangular(t_norm, fc_ratio, phase_deg):
    phi = np.deg2rad(phase_deg)
    return (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * fc_ratio * t_norm + phi))

def unipolar_pwm(t_norm, fc_ratio, carrier_phase_deg, M, Vdc):
    ref     = M * np.sin(2 * np.pi * t_norm)
    carrier = triangular(t_norm, fc_ratio, carrier_phase_deg)
    ac = np.abs(carrier)
    return np.where(ref > ac, Vdc, np.where(ref < -ac, -Vdc, 0.0))

n_list = [1, 2, 3, 4]

fig, axes = plt.subplots(4, 1, figsize=(12, 12), sharex=True)
fig.patch.set_facecolor('white')
fig.subplots_adjust(right=0.88, hspace=0.50)

for ax, n in zip(axes, n_list):
    carrier_phases = [360 * k / n for k in range(n)]
    v_cells = [unipolar_pwm(t, FC_RATIO, cp, M, Vdc) for cp in carrier_phases]
    v_total = sum(v_cells)
    ideal   = n * Vdc * M * np.sin(2 * np.pi * t)

    # Normalise by n*Vdc so every panel has the same y-scale.
    # The ideal sinusoid now has amplitude M=0.95 in every panel;
    # each voltage step equals 1/n of the full scale, shrinking visibly with n.
    scale   = n * Vdc
    v_n     = v_total / scale
    ideal_n = ideal   / scale   # = M * sin(2π t) — same shape for all n

    ax.fill_between(theta, v_n, ideal_n,
                    alpha=0.22, color='#f4a582', zorder=2,
                    label='Error vs ideal sinusoid')
    ax.plot(theta, v_n, color='#2166ac', lw=0.85,
            label=f'{2*n+1}-level PWM output ($n={n}$)', zorder=3)
    ax.plot(theta, ideal_n, color='#d73027', lw=2.0, ls='--',
            label='Ideal sinusoid (fundamental)', zorder=4)

    for k in range(-n, n + 1):
        ax.axhline(k / n, color='gray', lw=0.4, ls=':', alpha=0.4)
        lbl = f'${k:+d}V_{{dc}}$' if k != 0 else '$0$'
        ax.text(2 * np.pi + 0.07, k / n, lbl,
                va='center', ha='left', fontsize=7.5,
                color='#2166ac', clip_on=False)

    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.30, 1.45)          # same for every panel
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels([f'$-{n}V_{{dc}}$', '$0$', f'$+{n}V_{{dc}}$'], fontsize=9)
    ax.set_ylabel('Norm. voltage', fontsize=10)
    ns = 'cell' if n == 1 else 'cells'
    ax.set_title(
        f'  $n = {n}$ {ns}  \u2192  $2n+1 = {2*n+1}$ voltage levels'
        f'  (carrier phase shift = {int(360/n)}\u00b0, effective output $f_c = {n*FC_RATIO}f$)',
        fontsize=10.5, fontweight='bold', loc='left', pad=4, color='#1a1a2e')
    ax.legend(fontsize=8.5, loc='upper right', framealpha=0.92)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

axes[-1].set_xlabel('Phase angle (one full cycle)', fontsize=11)
axes[-1].set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
axes[-1].set_xticklabels(
    ['$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=11)

fig.suptitle(
    'CHB Multilevel PWM Output: Effect of Number of Cells\n'
    r'Unipolar sinusoidal PWM, phase-shifted carriers ($f_c = 6f$, $M = 0.95$)'
    '\nMore cells \u2192 more voltage levels \u2192 smaller error (orange) \u2192 smaller $L_f$ needed',
    fontsize=11.5, fontweight='bold')

plt.savefig(
    'C:/Users/tmouli/Documents/AI_trainig_data/Vasishta/figures/'
    'CHB_staircase_summation.png',
    dpi=150, bbox_inches='tight', facecolor='white')
print('staircase_summation saved.')
