# 简化版贝叶斯融合（带置信度加权）
def bayesian_fusion(models_output, prior=0.5):
    weighted_sum = 0
    total_weight = 0

    for m in models_output:
        weighted_sum += m["prob_up"] * m["confidence"]
        total_weight += m["confidence"]

    posterior = weighted_sum / total_weight

    return posterior
