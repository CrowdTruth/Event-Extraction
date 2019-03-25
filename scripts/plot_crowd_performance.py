import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("../data/main_crowd_data/results/train_experts_eval_crowd.csv")
experts = 0.788

plt.rcParams['figure.figsize'] = 6, 4
plt.plot(data["Thresh"], data["F1-score"], 'bo-', color = 'green', lw = 2, label = "F1-score: Train Experts, Test Crowd")

plt.axhline(y = experts, ls = '--', color = 'red', lw = 2, label = "F1-score: Train Experts, Test Experts")
plt.xlim(0.05,1.0)
plt.xlabel("ESS neg/pos threshold", fontsize=18)
plt.ylabel("F1-score", fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0.0,1.0)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
leg = plt.legend(loc="lower left")
leg.get_frame().set_alpha(0.8)
plt.grid(ls=':')
plt.savefig("../plots/train_experts_test_crowd.pdf", bbox_inches='tight', dpi=1000)
plt.close()

data = pd.read_csv("../data/main_crowd_data/results/train_crowd_eval_experts.csv")
experts = 0.788

plt.rcParams['figure.figsize'] = 6, 4
plt.plot(data["Thresh"], data["F1-score"], 'bo-', color = 'green', lw = 2, label = "F1-score: Train Crowd, Test Experts")

plt.axhline(y = experts, ls = '--', color = 'red', lw = 2, label = "F1-score: Train Experts, Test Experts")
plt.xlim(0.05,1.0)
plt.xlabel("ESS neg/pos threshold", fontsize=18)
plt.ylabel("F1-score", fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0.0,1.0)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
leg = plt.legend(loc="lower left")
leg.get_frame().set_alpha(0.8)
plt.grid(ls=':')
plt.savefig("../plots/train_crowd_test_experts.pdf", bbox_inches='tight', dpi=1000)