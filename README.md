# Roissingue Website

Landing page for [Roissingue API](https://github.com/lakonguina/roissingue-api), a unified API for gasless, multi-chain token swaps.

## Goal

Present the product to developers: value proposition, supported integrations and a ready-to-copy code example showing how to request a quote in a few lines.

## Stack

FastAPI serving Jinja2 templates and static assets, with SEO metadata, `robots.txt` and sitemap. Packaged with Docker.

## Run locally

```bash
uv sync
uv run fastapi dev
```
