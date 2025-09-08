import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# x 范围
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# 定义函数
def f(x, A, B, C, D):
    return A * np.sin(B * x + C) + D

# 基准参数
A0, B0, C0, D0 = 1, 1, 0, 0

# 创建 2x2 子图
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle(r"函数 $ f(x) = A \sin(Bx + C) + D $ 受各参数影响", fontsize=16, weight='bold')

# -----------------------------
# 图1：改变 A（振幅）
# -----------------------------
ax = axs[0, 0]
ax.plot(x, f(x, 1, 1, 0, 0), label=r'$A=1$', linewidth=2)
ax.plot(x, f(x, 2, 1, 0, 0), label=r'$A=2$', linestyle='--', linewidth=2)
ax.plot(x, f(x, 0.5, 1, 0, 0), label=r'$A=0.5$', linestyle=':', linewidth=2)
ax.set_title(r"1. 振幅 $A$ 的影响 ($B=1, C=0, D=0$)")
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)  # 中心线

# -----------------------------
# 图2：改变 B（频率）
# -----------------------------
ax = axs[0, 1]
ax.plot(x, f(x, 1, 1, 0, 0), label=r'$B=1$', linewidth=2)
ax.plot(x, f(x, 1, 2, 0, 0), label=r'$B=2$', linestyle='--', linewidth=2)
ax.plot(x, f(x, 1, 0.5, 0, 0), label=r'$B=0.5$', linestyle=':', linewidth=2)
ax.set_title(r"2. 频率 $B$ 的影响 ($A=1, C=0, D=0$)")
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)

# -----------------------------
# 图3：改变 C（相位）
# -----------------------------
ax = axs[1, 0]
ax.plot(x, f(x, 1, 1, 0, 0), label=r'$C=0$', linewidth=2)
ax.plot(x, f(x, 1, 1, np.pi/2, 0), label=r'$C=\pi/2$', linestyle='--', linewidth=2)
ax.plot(x, f(x, 1, 1, np.pi, 0), label=r'$C=\pi$', linestyle=':', linewidth=2)
ax.set_title(r"3. 相位 $C$ 的影响 ($A=1, B=1, D=0$)")
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)

# -----------------------------
# 图4：改变 D（垂直平移）
# -----------------------------
ax = axs[1, 1]
ax.plot(x, f(x, 1, 1, 0, 0), label=r'$D=0$', linewidth=2)
ax.plot(x, f(x, 1, 1, 0, 1), label=r'$D=1$', linestyle='--', linewidth=2)
ax.plot(x, f(x, 1, 1, 0, -1), label=r'$D=-1$', linestyle=':', linewidth=2)
ax.set_title(r"4. 垂直平移 $D$ 的影响 ($A=1, B=1, C=0$)")
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5, linestyle='-', alpha=0.3)  # 原始中心线
ax.axhline(y=1, color='k', linewidth=0.5, linestyle='--', alpha=0.5)  # D=1 中心线
ax.axhline(y=-1, color='k', linewidth=0.5, linestyle=':', alpha=0.5)  # D=-1 中心线

# 调整布局
plt.tight_layout(rect=[0, 0, 1, 0.96])

# 保存图像
plt.savefig('asin_bcd_all_effects.png', dpi=300, bbox_inches='tight')
plt.savefig('asin_bcd_all_effects.pdf', dpi=300, bbox_inches='tight', format='pdf')

print("✅ 图像已保存：")
print("   - asin_bcd_all_effects.png (高清 PNG)")
print("   - asin_bcd_all_effects.pdf (矢量 PDF)")

# 显示图像
plt.show()