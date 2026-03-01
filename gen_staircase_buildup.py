"""
CHB staircase buildup figure — n = 3 cells
Unipolar sinusoidal PWM, carriers at 0/120/240 degrees, fc/f = 12
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

f        = 50
FC_RATIO = 12
M        = 0.95
Vdc      = 1.0
N        = 14400
n        = 3

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

carrier_phases = [0, 120, 240]
v_cells  = [unipolar_pwm(t, FC_RATIO, cp, M, Vdc) for cp in carrier_phases]
v_total  = sum(v_cells)
ideal    = n * Vdc * M * np.sin(2 * np.pi * t)
ref_norm = M * np.sin(2 * np.pi * t)

cell_colors = ['#2166ac', '#4dac26', '#d01c8b']
sum_color   = '#762a83'

fig, axes = plt.subplots(4, 1, figsize=(13, 12), sharex=True,
                         gridspec_kw={'hspace': 0.55})
fig.patch.set_facecolor('white')
fig.subplots_adjust(right=0.88)   # right margin for level labels

# ── Rows 1–3: individual cell PWM outputs ─────────────────────────────────
for i, (ax, v, c, cp) in enumerate(
        zip(axes[:3], v_cells, cell_colors, carrier_phases)):

    carrier_wave = triangular(t, FC_RATIO, cp)

    # triangular carrier (faint)
    ax.plot(theta, carrier_wave * Vdc, color='#bbbbbb', lw=0.9,
            alpha=0.6, zorder=1, label=f'Carrier ({cp}\u00b0 shift)')

    # sinusoidal reference
    ax.plot(theta, ref_norm * Vdc, color=c, lw=1.6, ls='--',
            alpha=0.7, zorder=2, label='Sinusoidal reference $MV_{dc}\\sin(\\omega t)$')

    # PWM output
    ax.plot(theta, v, color=c, lw=1.1, alpha=0.92, zorder=3,
            label=f'Cell {i+1} PWM output')

    # rule: output = +Vdc when ref > carrier, -Vdc when ref < -carrier, else 0
    ax.set_ylim(-1.65, 2.0)
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(['$-V_{dc}$', '$0$', '$+V_{dc}$'], fontsize=9)
    ax.set_ylabel(f'Cell {i+1}', fontsize=10, fontweight='bold')
    ax.set_title(
        f'  Cell {i+1}: carrier at {cp}\u00b0  '
        r'$\rightarrow$  output $\in \{+V_{dc},\ 0,\ -V_{dc}\}$',
        fontsize=10, fontweight='bold', loc='left', pad=4, color='#1a1a2e')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.92, ncol=3)
    ax.grid(True, lw=0.3, alpha=0.3, axis='x')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# ── Row 4: summed output ───────────────────────────────────────────────────
ax4 = axes[3]

ax4.fill_between(theta, v_total, ideal,
                 alpha=0.20, color='#f4a582', zorder=2, label='Error vs ideal')
ax4.plot(theta, v_total, color=sum_color, lw=1.2, zorder=3,
         label='$v_g = v_1 + v_2 + v_3$  (7-level PWM output)')
ax4.plot(theta, ideal, color='#d73027', lw=2.0, ls='--', zorder=4,
         label='Ideal sinusoid $3V_{dc}M\\sin(\\omega t)$')

for k in range(-n, n + 1):
    ax4.axhline(k * Vdc, color='gray', lw=0.4, ls=':', alpha=0.4)

ax4.set_ylim(-n * 1.35, n * 1.55)
ax4.yaxis.set_ticks_position('right')
ax4.yaxis.set_label_position('left')
ax4.set_yticks([k * Vdc for k in range(-n, n + 1)])
ax4.set_yticklabels(
    [f'${k:+d}V_{{dc}}$' if k != 0 else '$0$' for k in range(-n, n + 1)],
    fontsize=8, color=sum_color)
ax4.set_ylabel('Sum $v_g$', fontsize=10, fontweight='bold')
ax4.set_title(
    '  Sum of all 3 cells  \u2192  7-level multilevel PWM output',
    fontsize=10, fontweight='bold', loc='left', pad=4, color='#1a1a2e')
ax4.legend(fontsize=9, loc='upper right', framealpha=0.92)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

ax4.set_xlabel('Phase angle (one full cycle)', fontsize=11)
ax4.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax4.set_xticklabels(
    ['$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=11)

fig.suptitle(
    'n = 3 Cell CHB: How Individual Unipolar SPWM Outputs Build the Multilevel Waveform\n'
    r'Each cell: 3 levels ($+V_{dc}$, 0, $-V_{dc}$), carriers phase-shifted 120$^\circ$'
    r' ($f_c = 12f$)  $\rightarrow$  Sum: 7 levels',
    fontsize=11.5, fontweight='bold')

plt.savefig(
    'C:/Users/tmouli/Documents/AI_trainig_data/Vasishta/figures/'
    'CHB_staircase_buildup.png',
    dpi=150, bbox_inches='tight', facecolor='white')
print('staircase_buildup saved.')
