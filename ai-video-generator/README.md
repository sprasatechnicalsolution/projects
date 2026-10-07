# AI Video Generator

**Turn a text prompt into a finished video, on your own machine**

![AI Video Generator overview](overview.jpg)

| | |
|---|---|
| **Client** | In-house R&D |
| **Type** | AI tool |
| **Year** | 2026 |
| **Status** | In development (architecture and job system in place) |
| **Platform** | Local web app |

## The idea

Small businesses need short videos for social media every week but can't afford a video team. This tool takes a written prompt (a product, an offer, a message) and produces a ready-to-post video, running locally so nothing is uploaded to a third party.

## How it works

1. **Prompt:** the user writes what the video should say, or uploads source material
2. **Plan:** a prompt service turns that into scenes
3. **Generate:** an AI engine produces the visuals and voice for each scene
4. **Assemble:** FFmpeg joins clips, audio and captions into one video
5. **Deliver:** the user downloads the finished file

Each video is a background job with its own status, so long renders don't block the app and several videos can queue up.

## Built so far

- A PHP front end on a small in-house MVC (router, request/response, database)
- A Python backend API with `generate`, `jobs`, `upload` and `health` endpoints
- A job model, queue and logger
- Service layers for the AI engine, prompts, jobs and FFmpeg

## Technology

| Area | Used |
|---|---|
| Front end | PHP, custom MVC |
| Backend | Python API, background queue |
| Video | FFmpeg |
| Database | MySQL |

---

**Built by Pradip Subedi · Sprasa Technical Solution**
Interested in AI tools for your business? [Get in touch](../README.md#contact).
