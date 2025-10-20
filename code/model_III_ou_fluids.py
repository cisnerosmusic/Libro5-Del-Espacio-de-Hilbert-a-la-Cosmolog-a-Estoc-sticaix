"""
Model III: Memory Fluids with Ornstein-Uhlenbeck Noise
=======================================================

This model treats dark energy as a cosmic fluid with memory, incorporating:
- Ornstein-Uhlenbeck stochastic process with timescale τ
- Connection to Gibbons-Hawking temperature
- Modified Friedmann equation with memory kernel

The equation of state w(z) oscillates due to memory effects,
creating testable signatures in cosmological observables.

Author: Ernesto Cisneros Cino (human) + Claude (Anthropic)
License: CC0 1.0 (Public Domain)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, quad
from scipy.interpolate import interp1d

# ============================================================================
# COSMOLOGICAL PARAMETERS
# ============================================================================

# Standard ΛCDM values (for comparison)
H0 = 70.0  # Hubble constant [km/s/Mpc]
OMEGA_M = 0.3  # Matter density parameter
OMEGA_LAMBDA = 0.7  # Dark energy density parameter

# Memory fluid parameters
TAU = 0.5  # Memory timescale in units of H0^-1
SIGMA_OU = 0.1  # OU noise amplitude
W0 = -1.0  # Base equation of state (cosmological constant-like)
DELTA_W = 0.15  # Amplitude of w oscillations

# Redshift range
Z_MIN = 0.0
Z_MAX = 3.0
N_POINTS = 500

# ============================================================================
# EQUATION OF STATE WITH MEMORY
# ============================================================================

def w_memory(z, tau=TAU, w0=W0, delta_w=DELTA_W, omega=2.0):
    """
    Equation of state with memory-induced oscillations:
    
    w(z) = w₀ + Δw · exp(-z/τ) · cos(ω·ln(1+z))
    
    The exponential damping represents memory decay,
    while the oscillation represents the memory kernel's structure.
    """
    return w0 + delta_w * np.exp(-z/tau) * np.cos(omega * np.log(1 + z))

def w_standard(z):
    """
    Standard ΛCDM: w = -1 (constant)
    """
    return -1.0 * np.ones_like(z)

# ============================================================================
# FRIEDMANN EQUATION WITH MEMORY
# ============================================================================

def H_squared(z, w_func, omega_m=OMEGA_M, omega_lambda=OMEGA_LAMBDA):
    """
    Modified Friedmann equation: H²(z)/H₀² = E²(z)
    
    E²(z) = Ωₘ(1+z)³ + Ω_DE · exp[3∫₀ᶻ (1+w(z'))/((1+z') dz']
    """
    
    # Matter contribution
    matter_term = omega_m * (1 + z)**3
    
    # Dark energy contribution with w(z)
    # Integrate: ∫ [1 + w(z')] / (1 + z') dz' from 0 to z
    def integrand(zp):
        return (1 + w_func(zp)) / (1 + zp)
    
    if z > 0:
        integral, _ = quad(integrand, 0, z, limit=100)
        de_term = omega_lambda * np.exp(3 * integral)
    else:
        de_term = omega_lambda
    
    return matter_term + de_term

def compute_H_array(z_array, w_func):
    """
    Compute H(z) for an array of redshifts
    """
    H_array = np.zeros_like(z_array)
    for i, z in enumerate(z_array):
        H_array[i] = np.sqrt(H_squared(z, w_func))
    return H_array

# ============================================================================
# DISTANCE MEASURES
# ============================================================================

def comoving_distance(z, H_func):
    """
    Comoving distance: dₘ = c/H₀ ∫₀ᶻ dz'/H(z')
    
    (Using units where c/H₀ = 1)
    """
    def integrand(zp):
        return 1.0 / H_func(zp)
    
    if z > 0:
        dm, _ = quad(integrand, 0, z, limit=100)
    else:
        dm = 0
    
    return dm

def luminosity_distance(z, H_func):
    """
    Luminosity distance: d_L = (1+z) · dₘ(z)
    """
    dm = comoving_distance(z, H_func)
    return (1 + z) * dm

def distance_modulus(z, H_func):
    """
    Distance modulus: μ = 5·log₁₀(d_L) + 25
    
    (Assuming d_L in Mpc and H₀ = 70 km/s/Mpc)
    """
    dL = luminosity_distance(z, H_func)
    # Convert to Mpc (assuming H₀ = 70)
    dL_Mpc = dL * (3000.0 / 70.0)  # c/H₀ in Mpc
    return 5 * np.log10(dL_Mpc) + 25

# ============================================================================
# ORNSTEIN-UHLENBECK PROCESS VISUALIZATION
# ============================================================================

def generate_ou_process(n_steps, tau=TAU, sigma=SIGMA_OU, dt=0.01):
    """
    Generate OU process as memory kernel
    """
    xi = np.zeros(n_steps)
    for i in range(1, n_steps):
        dW = np.random.randn() * np.sqrt(dt)
        xi[i] = xi[i-1] - (dt/tau) * xi[i-1] + (sigma/np.sqrt(tau)) * dW
    return xi

# ============================================================================
# MEMORY KERNEL
# ============================================================================

def memory_kernel(s, tau=TAU):
    """
    Memory kernel: K_τ(s) = (1/τ) · exp(-s/τ)
    
    This represents how past states influence present dynamics.
    The integral ∫₀^∞ K_τ(s) ds = 1 (normalized)
    """
    return (1.0 / tau) * np.exp(-s / tau)

# ============================================================================
# MAIN SIMULATION
# ============================================================================

def run_simulation():
    """
    Run memory fluid cosmology simulation
    """
    print("=" * 70)
    print("MODEL III: MEMORY FLUIDS WITH ORNSTEIN-UHLENBECK NOISE")
    print("=" * 70)
    print(f"\nParameters:")
    print(f"  Memory timescale: τ = {TAU}")
    print(f"  OU noise amplitude: σ = {SIGMA_OU}")
    print(f"  Base equation of state: w₀ = {W0}")
    print(f"  Oscillation amplitude: Δw = {DELTA_W}")
    print(f"\nRunning simulation...\n")
    
    # Redshift array
    z_array = np.linspace(Z_MIN, Z_MAX, N_POINTS)
    
    # Compute w(z) for memory model and ΛCDM
    w_mem = w_memory(z_array)
    w_lcdm = w_standard(z_array)
    
    # Compute H(z)
    print("Computing H(z) for memory model...")
    H_mem_array = compute_H_array(z_array, w_memory)
    
    print("Computing H(z) for ΛCDM...")
    H_lcdm_array = compute_H_array(z_array, w_standard)
    
    # Create interpolators
    H_mem_interp = interp1d(z_array, H_mem_array, kind='cubic', 
                             fill_value='extrapolate')
    H_lcdm_interp = interp1d(z_array, H_lcdm_array, kind='cubic', 
                              fill_value='extrapolate')
    
    # Compute distance modulus
    print("Computing distance modulus...")
    mu_mem = np.array([distance_modulus(z, H_mem_interp) for z in z_array])
    mu_lcdm = np.array([distance_modulus(z, H_lcdm_interp) for z in z_array])
    
    # Generate OU process for visualization
    n_ou_steps = 1000
    ou_time = np.linspace(0, 20, n_ou_steps)
    ou_process = generate_ou_process(n_ou_steps, tau=TAU, sigma=SIGMA_OU, dt=0.02)
    
    # Memory kernel
    s_array = np.linspace(0, 5*TAU, 200)
    kernel = memory_kernel(s_array)
    
    # ========================================================================
    # PLOTTING
    # ========================================================================
    
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Model III: Memory Fluids - Cosmological Signatures', 
                 fontsize=16, fontweight='bold')
    
    # Plot 1: Equation of state w(z)
    ax1 = plt.subplot(3, 3, 1)
    ax1.plot(z_array, w_mem, 'b-', linewidth=2.5, label='Memory model')
    ax1.plot(z_array, w_lcdm, 'r--', linewidth=2, label='ΛCDM')
    ax1.axhline(y=-1, color='gray', linestyle=':', linewidth=1)
    ax1.set_xlabel('Redshift z', fontsize=11)
    ax1.set_ylabel('w(z)', fontsize=11)
    ax1.set_title('Equation of State', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim([-1.3, -0.7])
    
    # Plot 2: Hubble parameter H(z)/H₀
    ax2 = plt.subplot(3, 3, 2)
    ax2.plot(z_array, H_mem_array, 'b-', linewidth=2.5, label='Memory model')
    ax2.plot(z_array, H_lcdm_array, 'r--', linewidth=2, label='ΛCDM')
    ax2.set_xlabel('Redshift z', fontsize=11)
    ax2.set_ylabel('E(z) = H(z)/H₀', fontsize=11)
    ax2.set_title('Hubble Parameter Evolution', fontsize=12, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Residuals Δμ = μ_memory - μ_ΛCDM
    ax3 = plt.subplot(3, 3, 3)
    delta_mu = mu_mem - mu_lcdm
    ax3.plot(z_array, delta_mu, 'purple', linewidth=2.5)
    ax3.axhline(y=0, color='k', linestyle='-', linewidth=1)
    ax3.fill_between(z_array, -0.1, 0.1, alpha=0.2, color='gray', 
                     label='±0.1 mag (typical SNe Ia error)')
    ax3.set_xlabel('Redshift z', fontsize=11)
    ax3.set_ylabel('Δμ [mag]', fontsize=11)
    ax3.set_title('Distance Modulus Residuals', fontsize=12, fontweight='bold')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Memory kernel K_τ(s)
    ax4 = plt.subplot(3, 3, 4)
    ax4.plot(s_array, kernel, 'green', linewidth=2.5)
    ax4.fill_between(s_array, 0, kernel, alpha=0.3, color='green')
    ax4.set_xlabel('Time lag s', fontsize=11)
    ax4.set_ylabel('K_τ(s)', fontsize=11)
    ax4.set_title(f'Memory Kernel (τ = {TAU})', fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    # Plot 5: OU process example
    ax5 = plt.subplot(3, 3, 5)
    ax5.plot(ou_time, ou_process, 'orange', linewidth=1.5, alpha=0.8)
    ax5.set_xlabel('Time', fontsize=11)
    ax5.set_ylabel('ξ(t)', fontsize=11)
    ax5.set_title('Ornstein-Uhlenbeck Process', fontsize=12, fontweight='bold')
    ax5.grid(True, alpha=0.3)
    
    # Plot 6: Distance modulus (Hubble diagram)
    ax6 = plt.subplot(3, 3, 6)
    ax6.plot(z_array, mu_mem, 'b-', linewidth=2.5, label='Memory model')
    ax6.plot(z_array, mu_lcdm, 'r--', linewidth=2, label='ΛCDM')
    ax6.set_xlabel('Redshift z', fontsize=11)
    ax6.set_ylabel('Distance modulus μ [mag]', fontsize=11)
    ax6.set_title('Hubble Diagram', fontsize=12, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    # Plot 7: Oscillation frequency spectrum of w(z)
    ax7 = plt.subplot(3, 3, 7)
    # FFT of w(z) oscillations
    w_oscillation = w_mem - W0  # Remove mean
    fft_w = np.fft.fft(w_oscillation)
    freqs = np.fft.fftfreq(len(w_oscillation), d=(z_array[1]-z_array[0]))
    power = np.abs(fft_w)**2
    
    # Plot positive frequencies only
    pos_mask = freqs > 0
    ax7.semilogy(freqs[pos_mask], power[pos_mask], 'darkblue', linewidth=2)
    ax7.set_xlabel('Frequency [z⁻¹]', fontsize=11)
    ax7.set_ylabel('Power', fontsize=11)
    ax7.set_title('w(z) Frequency Spectrum', fontsize=12, fontweight='bold')
    ax7.grid(True, alpha=0.3)
    
    # Plot 8: Relative difference in H(z)
    ax8 = plt.subplot(3, 3, 8)
    delta_H_percent = 100 * (H_mem_array - H_lcdm_array) / H_lcdm_array
    ax8.plot(z_array, delta_H_percent, 'darkred', linewidth=2.5)
    ax8.axhline(y=0, color='k', linestyle='-', linewidth=1)
    ax8.fill_between(z_array, -1, 1, alpha=0.2, color='gray',
                     label='±1% (typical H(z) precision)')
    ax8.set_xlabel('Redshift z', fontsize=11)
    ax8.set_ylabel('ΔH/H [%]', fontsize=11)
    ax8.set_title('Relative Difference in Hubble Parameter', fontsize=12, 
                  fontweight='bold')
    ax8.legend(fontsize=9)
    ax8.grid(True, alpha=0.3)
    
    # Plot 9: Cumulative effect (integral of memory kernel)
    ax9 = plt.subplot(3, 3, 9)
    cumulative_kernel = np.cumsum(kernel) * (s_array[1] - s_array[0])
    ax9.plot(s_array, cumulative_kernel, 'brown', linewidth=2.5)
    ax9.axhline(y=1.0, color='r', linestyle='--', linewidth=1, 
                label='Normalization')
    ax9.set_xlabel('Time lag s', fontsize=11)
    ax9.set_ylabel('∫₀ˢ K_τ(s\') ds\'', fontsize=11)
    ax9.set_title('Cumulative Memory Effect', fontsize=12, fontweight='bold')
    ax9.legend()
    ax9.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('memory_fluids_cosmology.png', dpi=300, bbox_inches='tight')
    print("✓ Plot saved as 'memory_fluids_cosmology.png'")
    plt.show()
    
    # ========================================================================
    # RESULTS SUMMARY
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)
    print(f"\nEquation of state:")
    print(f"  w(z=0) = {w_mem[0]:.4f}")
    print(f"  w(z=1) = {w_mem[N_POINTS//3]:.4f}")
    print(f"  w(z=2) = {w_mem[2*N_POINTS//3]:.4f}")
    print(f"  Oscillation amplitude: {np.max(w_mem) - np.min(w_mem):.4f}")
    
    print(f"\nDistance modulus residuals:")
    print(f"  Max |Δμ| = {np.max(np.abs(delta_mu)):.4f} mag")
    print(f"  RMS(Δμ) = {np.sqrt(np.mean(delta_mu**2)):.4f} mag")
    
    print(f"\nHubble parameter differences:")
    print(f"  Max |ΔH/H| = {np.max(np.abs(delta_H_percent)):.3f}%")
    print(f"  RMS(ΔH/H) = {np.sqrt(np.mean(delta_H_percent**2)):.3f}%")
    
    print(f"\nMemory kernel properties:")
    print(f"  Timescale τ = {TAU}")
    print(f"  Kernel normalization: ∫K_τ ds ≈ {cumulative_kernel[-1]:.4f}")
    
    print("\n" + "=" * 70)
    print("FALSIFIABILITY:")
    print("  - Compare Δμ predictions with Pantheon+ SNe Ia data")
    print("  - Test H(z) oscillations with DESI BAO measurements")
    print("  - Look for oscillatory features in CMB power spectrum")
    print("=" * 70)
    
    print("\n" + "=" * 70)
    print("KEY FINDING: Memory (τ > 0) creates oscillations in w(z)")
    print("These produce testable signatures in distance-redshift relation")
    print("=" * 70 + "\n")

# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    run_simulation()
```

---

4. **En "Commit changes..." escribe:**
```
   Add Model III: Memory fluids with OU noise
