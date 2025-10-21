import os
import json
from datetime import datetime
import time

# -------------------------------------------------------------------------
# Mock AI API Call Function (Replace with actual SDK calls)
# -------------------------------------------------------------------------

# NOTE: This function demonstrates how to structure the prompt for structured output
# using a system instruction.
# In a real project, you would replace the sleep and mock data with your chosen SDK.
# Example for OpenAI: from openai import OpenAI; client = OpenAI()
# Example for Google GenAI: from google import genai; client = genai.Client()

def generate_content_data(topic: str, model_name: str = "gemini-2.5-flash-preview-09-2025") -> dict:
    """
    Simulates calling the AI model API to generate structured content 
    (blog + 3 newsletters) based on a topic.
    
    Args:
        topic (str): The subject of the blog post.
        model_name (str): The name of the AI model planned for use.
        
    Returns:
        dict: A dictionary containing all generated content (mock JSON structure).
    """
    print(f"--- 1. Preparing Content Generation Task ---")
    print(f"Topic: {topic}")
    print(f"Target Model: {model_name}")
    
    # Define the personas and their specific focus points
    personas = [
        {"name": "Founders / Decision-Makers", "focus": "ROI, Growth, Efficiency (Use results-driven, financial language)"},
        {"name": "Creative Professionals", "focus": "Inspiration, Time-saving tools, Boosting creativity (Use motivational, inspiring language)"},
        {"name": "Operations Managers", "focus": "Workflows, Integrations, Reliability, Automation (Use practical, structured, and reliable language)"}
    ]

    # Build the System Instruction for the AI
    # This strictly enforces the required JSON output format.
    system_instruction = f"""
    You are a world-class content marketing specialist for an AI startup named NovaMind.
    Your task is to generate a blog draft and three personalized newsletters based on the given topic.
    
    Blog requirements: Include a title, outline, and a draft of approximately 400-600 words.
    Newsletter requirements: Each must be short, personalized, and include a compelling subject line customized for the target persona.

    You MUST strictly adhere to the following JSON Schema for your entire output. All content must be written in English.
    """
    
    # Build the User Prompt
    user_prompt = f"""
    Please generate content for the following topic: "{topic}".
    
    Blog Requirements:
    - The title should be engaging.
    - The outline must contain at least 4 bullet points.
    - The draft content must be 400-600 words.
    
    Customize the three newsletters based on the following personas and their focus areas:
    {json.dumps(personas, indent=2)}
    """
    
    # -------------------------------------------------------------------------
    # Actual API call code would go here
    # E.g.: response = client.generate_content(..., system_instruction=system_instruction, contents=user_prompt, config={response_mime_type: "application/json", ...})
    # -------------------------------------------------------------------------
    
    print("\n--- 2. Simulating AI Generation (Waiting 3 seconds)... ---")
    time.sleep(3) # Simulate network latency and processing time
    
    # Mock AI output as a Python dictionary simulating the parsed JSON response
    mock_ai_output = {
      "topic": topic,
      "blog": {
        "title": f"The AI Revolution in Creative Workflows: Say Goodbye to Repetitive Tasks",
        "outline": [
          "Introduction: The Automation Challenge for Creative Agencies",
          "AI's Core Role in Content Generation and Iteration",
          "Boosting Efficiency: How AI Handles Repetitive Tasks (e.g., asset management, formatting)",
          "Future Outlook: The New Paradigm of Human-AI Collaboration and NovaMind's Role"
        ],
        "draft_content": "Creative agencies have long struggled with the dilemma of efficiency versus innovation. Designers and copywriters spend significant time on low-value, repetitive tasks like asset management, format conversions, and minor draft corrections. However, this is rapidly changing with the advancements in artificial intelligence. Tools like NovaMind are becoming powerful aids in the creative workflow, acting as intelligent collaborators rather than simple automation scripts. AI can take over time-consuming data processing, preliminary layout designs, and automatic ad resizing according to brand guidelines. This liberation allows creative professionals to focus on work that truly requires human insight and emotional intelligence: strategic planning and high-concept ideation. AI isn't replacing human creativity; it's replacing drudgery. By outsourcing the tedious parts of daily operations to AI, creative teams can dedicate more energy to experimentation and innovation, ultimately maximizing the Return on Investment (ROI) for creative projects and delivering faster, more customized services to clients."
      },
      "newsletters": [
        {
          "persona": "Founders / Decision-Makers",
          "focus": "ROI, Growth, Efficiency",
          "subject_line": "30% Margin Growth: How AI Minimizes Your Agency's Operational Costs",
          "body": "Founders, tired of manual labor eating into your margins? Our latest blog reveals how AI delivers unprecedented efficiency in creative workflows. NovaMind automation can handle 40% of low-value tasks, letting your team focus on high-revenue projects. Read the full post to see how AI ensures your growth targets are met and delivers tangible ROI."
        },
        {
          "persona": "Creative Professionals",
          "focus": "Inspiration, Time-saving tools",
          "subject_line": "Unleash Your Superpower: AI is Your Creativity Accelerator",
          "body": "Fellow creatives, stop getting bogged down by details! AI doesn't limit your imagination—it powers it. It quickly generates mockups and explores different styles, giving you more time for deep conceptual thinking and experimentation. Click to read our blog and discover how NovaMind saves you hours, keeping your creative flow unstoppable!"
        },
        {
          "persona": "Operations Managers",
          "focus": "Workflows, Integrations, Reliability",
          "subject_line": "One-Click Deployment: The Integration Secrets to Reliable AI Workflows",
          "body": "Ops Managers, workflow reliability is everything. Our new blog focuses on how AI tools seamlessly integrate into your existing Notion and Zapier environments. Learn how NovaMind ensures data sync, task automation, and stable workflow execution, minimizing bottlenecks and boosting team efficiency. Check out the detailed integration strategies!"
        }
      ],
      "generation_date": datetime.now().isoformat()
    }
    
    return mock_ai_output

def main(topic: str = "AI in Creative Automation"):
    """
    Main function: executes the content generation process and saves the result to a JSON file.
    """
    output_data = generate_content_data(topic)
    
    # Ensure the output directory exists
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate a safe filename based on the topic and timestamp
    safe_topic = topic.replace(" ", "_").replace("/", "_").replace(":", "_").lower()
    filename = f"{safe_topic}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join(output_dir, filename)
    
    # Save the JSON file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            # Use indent=2 for readability
            json.dump(output_data, f, indent=2)
        print(f"\n--- 3. Results Saved Successfully ---")
        print(f"Content successfully saved to: {filepath}")
        print("This JSON file is the input for Phase 2: CRM Distribution and Performance Analysis.")
        
    except IOError as e:
        print(f"Failed to save file: {e}")

if __name__ == "__main__":
    # You can change your topic here
    main(topic="AI in Creative Automation")
