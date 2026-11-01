# 大 N 非凸排除证明：qmd-prover 重建审计

本目录把附件 `source-original.md` 重建为 `workspace/large-n-proof.qmd`，并用 qmd-prover 的独立 `codex` 检查器配置进行检查：`model: gpt-6.1-sol`、`effort: high`、`citations: standard`、`rigor: standard`。项目保留默认的 unrestricted 外部数学基准；所有非平凡外部结果都在证明文本中点名。

最终项目检查的机械结果是：45 个语义事实、0 个结构错误、0 个循环、0 个未解析引用；45 个事实（包括主定理）全局 `verified`。检查器配置为 `codex / gpt-6.1-sol / high`。

检查器曾对基础定义和 `@lem-edge-moments` 给出通过 verdict；这些记录在后续源文件/外部基准变更后由 qmd-prover 标记为 stale，不能当作当前最终版本的已验证状态。修复后的 `@lem-toeplitz-positive-atoms` 当前缓存检查仍为 `verified`。

Toeplitz 引理的原稿确有错误。原稿写的正谱平方和下界系数不成立；例如 $p=1,\tau=0.9$ 时右端超过实际平方和。已改为
$$
\sum_i\alpha_i^2\ge
\frac{1+\tau^p}{(1-\tau^2)(1-\tau^p)},
$$
并补上了压缩交错、正惯性和严格凸约束最小化的说明。该修复后的引理由 `gpt-6.1-sol/high` 独立检查通过。

非线性谱核心以及单反角链均已拆分并通过独立检查：频率衰减替换、对数 Bergman 能量、Airy 边界二次计算、逆导数能量、正则多边形渐近、cotangent 单调边、物理压力矩换元、单调权比较、单反角小原子、能量缺口和原子删除均为 `verified`。

其中检查器曾指出：仅有统一 $W^{1,4}$ 界不能直接推出特征函数一致收敛和圆盘内包含；重建稿已补上紧性、极限识别和内圆包含的定性步骤。谱展开已改用固定 $H^1_0$ 上的形式扰动框架，Airy 计算也已拆成全局势、边界通量和二次响应接口。

单反角段修正了一处错误等式：原稿声称一般单调 $h$ 满足
$$
D=2\frac{\int(x-1/2)h^{-2}}{\int h^{-2}},
$$
该等式并不成立。重建稿删除该等式，改用已独立检查通过的一维单调权比较估计。

因此，当前 qmd-prover 状态是：机械层和全局数学检查均已通过，主定理 `@thm-main-large-n-convexity` 已 verified。附件原稿没有被覆盖，修订语义稿位于 `workspace/large-n-proof.qmd`。
