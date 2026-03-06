# Presentation Project

This directory contains presentation and proposal materials for the **Manah Group website revamp** project.

## Project Context

- **Client**: Manah Group (business conglomerate serving multiple industries)
- **Agency**: Toss The Coin Ltd (TTC) — BSE-listed B2B marketing agency, Chennai HQ
- **Project**: Website revamp to position Manah Group as a serious business conglomerate
- **Scope**: 9 web pages, 60 working days, WordPress platform
- **Investor Pitch**: Liberin Technologies investor pitch deck (PPTX)

## Key Files

| File | Description |
|------|-------------|
| `TTC_Proposal_Liberinfor_Manah_Website_06March2026.pdf` | TTC's website revamp proposal for Manah Group |
| `Liberin-Investor-Pitch-2026.pptx` | Liberin Technologies investor pitch deck |
| `.env` | API keys (NEVER commit to version control) |

## Website Revamp Phases (from TTC Proposal)

1. Discovery Session (1.5hr video call)
2. Website Strategy — Messaging & Positioning, IA/Site Map
3. Content & Copywriting
4. Design Layout & UX/UI
5. Custom WordPress Development (9 pages, responsive, CMS admin)
6. Project Management

## Pricing

- Strategy + Content + Design: INR 9,60,000
- WordPress Development: INR 2,00,000
- Project Management: Included
- All prices + 18% GST

## Image & Asset Generation

Use **Google Nano Banana 2** (`google/nano-banana-2`) via Replicate for generating high-quality images, charts, and graphs for presentations and website assets.

- Model: `google/nano-banana-2`
- Use for: presentation visuals, infographics, charts, graphs, website imagery
- Auth: Uses `REPLICATE_API_TOKEN` from `~/Desktop/asset-generator/.env`
- Gemini API available for prompt generation/refinement before image generation

## Environment Variables

API keys are stored in `.env`. See the parent `~/Desktop/CLAUDE.md` for Replicate API details.

- `GEMINI_API_KEY` — Google Gemini API key
