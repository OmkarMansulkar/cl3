{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e73f9030",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from sklearn.datasets import make_classification\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "# Simulate structure damage dataset (1 = damaged, 0 = normal)\n",
    "X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)\n",
    "\n",
    "# Initialize population of random classifiers (weights)\n",
    "pop = [np.random.randn(5) for _ in range(20)]\n",
    "\n",
    "def classify(x, w):\n",
    "    return int(np.dot(x, w) > 0)\n",
    "\n",
    "def fitness(w):\n",
    "    preds = [classify(x, w) for x in X]\n",
    "    return accuracy_score(y, preds)\n",
    "\n",
    "# Evolution loop\n",
    "for _ in range(50):  # 50 generations\n",
    "    scores = [fitness(w) for w in pop]\n",
    "    # Sort by fitness (descending)\n",
    "    sorted_pop = [w for _, w in sorted(zip(scores, pop), key=lambda x: x[0], reverse=True)]\n",
    "    top = sorted_pop[:10]  # Select top 10\n",
    "    # Create clones with mutation\n",
    "    clones = [w + np.random.normal(0, 0.1, 5) for w in top for _ in range(2)]\n",
    "    pop = clones  # New generation\n",
    "\n",
    "# Evaluate best individual\n",
    "best = max(pop, key=fitness)\n",
    "print(\"Best Accuracy:\", fitness(best))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ccbe2fb",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
