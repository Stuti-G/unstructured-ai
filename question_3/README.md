# Question 3: Zero-Shot Classification with LLMs (Unexecuted)

## ❗ Context

This task required developing a zero-shot text classification pipeline using Large Language Models (LLMs) **without task-specific fine-tuning**. The goal was to:

- Implement prompt engineering techniques
- Compare different prompt templates
- Evaluate on a dataset with **unseen class labels**
- Analyze classification **confidence** and **thresholds**
- Propose improvements to boost zero-shot performance

---

## ⚠️ Why This Could Not Be Executed

Despite preparing the code and designing the prompts, the actual execution could not be completed due to technical and resource-related issues:

### 🔑 API Quota Exhaustion
All attempts to use popular cloud-hosted LLMs (e.g., GPT, Mistral via OpenAI/Mistral APIs) resulted in **"Quota Exceeded"** errors. API usage limits were exhausted and couldn't be refreshed during the timeframe.

### 🖥️ Local Model Load Crashes
An alternative plan to use open-source LLMs like **Mistral-7B** and **Flan-T5** in **Google Colab** was attempted. However:
- The Colab environment with **T4 GPU** repeatedly **crashed** while loading or running inference with large models like Mistral.
- Even memory-efficient variants caused instability due to limited RAM and compute resources.

---

## ✅ What Was Prepared (but Not Executed)

- Prompt engineering templates for 3 types of classification prompts
- Code for loading open-source models using Hugging Face `transformers`
- Evaluation and thresholding logic using cosine similarity and logit confidence

---

## 📌 Note

If run locally with sufficient GPU (e.g., A100, V100) or on paid cloud (e.g., AWS, Paperspace, HF Spaces), the prepared setup is expected to work.

For now, this question remains documented and designed — **but not executed** due to the above constraints.
