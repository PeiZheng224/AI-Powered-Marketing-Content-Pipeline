# 🧪 Palona AI Take-Home Assignment: AI-Powered Marketing Content Pipeline
## 🧠 Objective
Build a **lightweight, automated marketing pipeline** that generates, distributes, and optimizes blog and newsletter content using AI and CRM integrations.

Your system should:

1. **Ideate and generate content** (e.g., blog + newsletter copy) using an AI model.
2. **Distribute** that content to a targeted audience through a marketing CRM (like HubSpot or a similar platform).
3. **Collect and analyze** engagement data to inform future content optimizations.

The end goal:

A well-greased, mostly hands-free AI pipeline for producing **highly targeted and customizable marketing content** that continuously improves based on performance metrics. This could be hosted on a website or just be a program run on your local machine.

---

## 🧭 Scenario
You’re the Content & Growth Analyst for **NovaMind**, a fictional early-stage AI startup that helps small creative agencies automate their daily workflows (think Notion + Zapier + ChatGPT combined).

NovaMind wants to grow inbound traffic and newsletter conversions using AI-assisted content. The company publishes **one weekly blog** about automation trends, then promotes it via **personalized newsletters** segmented by audience type:
- **Founders / Decision-Makers** (focus on ROI, growth, efficiency)
- **Creative Professionals** (focus on inspiration, time-saving tools)
- **Operations Managers** (focus on workflows, integrations, reliability)
Your task: **design and implement an AI content automation system** that takes a blog idea all the way through to newsletter distribution and performance reporting.

---

## 🛠 Requirements
**1. AI Content Generation**
Build a process that can:
- Take a topic input (e.g., “AI in creative automation”) and generate:
  - A blog post outline and short-form draft (≈ 400–600 words).
  - Three short newsletter versions of that blog, each customized for a different persona.
- Use any language model (OpenAI, Claude, Gemini, etc.) via API or SDK.
- Store the generated content in a structured format (JSON, Markdown, or CMS entry).

---

**2. CRM + Newsletter Distribution**
Integrate your system with **HubSpot** (or a similar CRM if you prefer).

Your automation should:

- Create or update contacts in your CRM (mock data is fine).
- Tag or segment contacts by persona.
- Send out the appropriate newsletter version to each persona segment.
- Log each campaign (blog title, newsletter ID, send date) to your CRM.
💡 You can sign up for a HubSpot free developer or trial account or similar service and send API calls with test data — please show realistic endpoint usage and payload structure.

---

**3. Performance Logging & Analysis**
After “sending” your campaign, your system should:
- Fetch or simulate newsletter performance data (open rate, click rate, unsubscribe rate, etc.).
- Store the data for historical comparison.
- Generate a brief AI-powered performance summary (e.g., “Creative Professionals had a 12% higher click rate. Recommend using more visual case studies next time.”).

---

**4. Optional Bonus Features**
- Add AI-driven content optimization (e.g., suggest next blog topics or headlines based on engagement trends).
- Add multiple options for copy and content with the ability to add revisions and suggestions.
- Build a simple dashboard or web UI to view and trigger the workflow.

## 📦 Deliverables
Submit the following:
- **GitHub repo** (or similar) containing your code and documentation.
- **README or design doc** explaining:
  - Architecture overview and flow diagram
  - Tools, APIs, and models used
  - Assumptions made (e.g., mocked data, simulated responses)
  - Instructions to run locally
- **(Optional)** Short Loom/demo video walking through your pipeline

