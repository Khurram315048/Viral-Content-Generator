"""
Prompt templates for TrendPilot Agentic AI Assistant.
Designed for dynamic content generation across any user-provided topic.
"""

TREND_IDEA_PROMPT="""You are an expert social media viral strategist.
Generate 3 creative and high-performing content angles or viral concepts for Instagram Reels based on the following topic.

Topic:{topic}
Tone:{tone}

Provide output as a structured list with clear titles and brief concept explanations.
"""

REEL_SCRIPT_PROMPT="""You are a professional short-form video scriptwriter specializing in Instagram Reels.
Write a fast-paced 30-60 second Instagram Reel script based on these content concepts.

Concept:
{concept}

Tone:{tone}

Required Structure:
- Opening Hook (0-3s): High attention-grabbing statement or visual hook.
- Main Body (3-45s): Core value/explanation broken down clearly.
- Visual & Audio Cues: Scene description, text overlays, and audio vibe.
- Call to Action (CTA): Strong closing encouraging engagement.
"""

HASHTAG_PROMPT="""You are a social media hashtag optimizer.
Generate 12-15 highly relevant and trending Instagram hashtags for the topic below.

Topic: {topic}

Mix high-volume, niche, and topic-specific hashtags. Format output clearly with '#' symbols.
"""

CONTENT_REVIEW_PROMPT = """You are a senior social media content reviewer and editor.
Review the generated Instagram Reel content for engagement, clarity, and viral potential.

Generated Content:
{content}

Provide concise feedback covering:
1. Hook Strength (Rating 1-10)
2. Pacing & Clarity
3. Key Viral Optimization Tip (1 specific actionable improvement)
"""