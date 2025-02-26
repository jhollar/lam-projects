# Large Action Model Projects
A large action model is a form of AI technology designed to process information and execute actions based on that information. Unlike large language models (LLMs), which primarily focus on understanding and generating language-based outputs, Large action models (LAMs) are capable of performing tangibleactions in the real world.

It is a shift from passive processing to active execution that marks a significant evolution in AI capabilities.

## How Do Large Action Models Work?

Large action models rely on a foundation of data and advanced machine learning techniques to perform their functions. Similar to AI agents, they’re designed to understand complex data inputs and take appropriate actions, making them highly effective across various real-world applications.

LAM AI technology, such as the xLAM series developed by Salesforce AI Research, is designed to enhance the capabilities of AI agents across a variety of tasks. These models incorporate both dense and mixture-of-experts architectures, ranging from 1B to 8x22B parameters. They use a scalable and flexible training pipeline, which allows them to integrate and synthesize diverse datasets, significantly improving the generalizability and performance of AI agents in different environments.

A key component of the LAMs’ training process is data unification, where data collected from multiple sources in various formats is standardized. Standardization reduces noise and simplifies further data processing tasks such as augmentation and quality verification.

For instance, in the xLAM series, data unification involves structuring data in a function-calling format, which consists of modules like task instruction, available tools, and query steps. As a result of this unified format, the model can generalize across different tasks and environments.

Following data unification, data augmentation plays a role in enhancing the diversity of the training data. This involves transforming existing datasets to generate new, synthetic data samples that help prevent model overfitting. Techniques used include prompt format augmentation, where the order of data elements is shuffled, and instruction-following augmentation, which involves rephrasing and verifying task instructions to improve the model’s capability to follow diverse instructions accurately.

## Neuro-symbolic programming

Neuro-symbolic programming is the real secret to how LAMs function. It allows them to process information and understand and execute tasks that require a blend of cognitive understanding and procedural execution. For instance, a LAM might use symbolic reasoning to plan a travel itinerary based on logical rules (like flight times and hotel check-in policies) and neural networks to understand and interpret user preferences and past behavior.

The symbolic part of neuro-symbolic programming helps make the decision-making process of LAMs more transparent and interpretable. In applications where understanding the rationale behind decisions is important, such as in healthcare or finance, this kind of transparency can be useful. When you combine this with neural networks, LAMs achieve a balance of high accuracy and the ability to justify their actions.

The hybrid nature of neuro-symbolic models enables LAMs to generalize across different domains. They can learn from specific instances in one domain and apply learned rules in another, which is beneficial for scaling AI applications across different industries without needing extensive retraining.

## Projects
Various example projects.

| Project    | Description |
| -------- | ------- |
| lavague_application  | This repository contains a Python application that demonstrates how to use LaVague to create web agents capable of navigating and interacting with web interfaces autonomously.   |
| lavague_weather | A simple Flask-based web application that provides news summaries and weather information through agent-based implementation.     |
******

