# 🌱 SeedSpark

**The open-source Movement Operating System for climate action.**

SeedSpark gives every person and community the tools to **start, grow, measure, and scale** grassroots climate movements — without platforms that own your data or dilute your message.

It is designed to create a global wave of hyper-local, high-impact climate actions that compound into real systemic change.

## Why SeedSpark?

Most climate tools are either:
- Corporate dashboards that track footprints but never turn into collective power, or
- Social media campaigns that burn out in weeks.

SeedSpark is different. It is a **protocol + toolkit** for building durable movements:

- **Local-first**: Actions start in neighborhoods, schools, workplaces, and towns.
- **Transparent & verifiable**: Impact is measured in real units (trees, kg CO₂ avoided, policy wins).
- **Composable**: Movements can fork, merge, and federate.
- **Ownership**: Communities own their data and narrative.

## Core Concepts

### 1. Seeds
A **Seed** is a concrete, time-bound climate action that anyone can start:
- "Car-Free Fridays in my neighborhood"
- "Plant 500 native trees this monsoon"
- "School zero-waste challenge"
- "Lobby for cool roofs in my city ward"

### 2. Sprouts
When people join a Seed and take action, they create **Sprouts** — verified contributions that are publicly countable.

### 3. Forests
Successful Seeds can grow into **Forests** — larger coordinated campaigns or permanent local climate clubs.

### 4. The Pulse
A live, open dashboard of collective impact across all Seeds in a region or the world.

## What is included (v0.1)

- **Seed Protocol** – simple JSON schema + API for defining and tracking actions
- **Impact Ledger** – lightweight, append-only log of contributions (can be backed by Git or local DB)
- **Starter Templates** – ready-to-run Seeds for common high-leverage actions
- **Local Dashboard** – minimal web UI to create Seeds, join them, and see progress
- **Movement Manifesto Generator** – structured prompts to write clear calls to action
- **Export & Share** – turn any Seed into a shareable campaign page or QR code

## Quick Start

```bash
# Clone
git clone https://github.com/rorito-alt/SeedSpark.git
cd SeedSpark

# Install (Python example)
pip install -r requirements.txt

# Run the local pulse server
python -m seedspark.server
```

Open http://localhost:8080

## Roadmap (what will make this a movement)

- [ ] Mobile-first PWA
- [ ] Offline-first capability
- [ ] Federated instances (ActivityPub or simple JSON feeds)
- [ ] Verified impact badges (optional cryptographic proofs)
- [ ] Integration with existing citizen science sensors
- [ ] Policy-win tracker (link Seeds to local government outcomes)
- [ ] Multi-language support from day one

## How to start a movement with SeedSpark today

1. Fork this repo or create a new Seed using the protocol.
2. Define a clear, measurable goal and a 30–90 day timeline.
3. Share the Seed link in your community (WhatsApp, Telegram, local groups).
4. Celebrate every Sprout publicly.
5. When you hit your goal, plant the next Seed and invite neighboring areas to fork it.

## Contributing

This project is intentionally simple so that non-coders can contribute ideas and organizers can shape the direction.

- Open an issue with a Seed idea
- Improve the protocol
- Translate templates
- Build UI components
- Document real-world use cases

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

Apache 2.0 — free for everyone to use, modify, and build upon, including commercial and non-profit use.

## The Vision

We believe the next climate movement will not be led by a single organization or celebrity.

It will be a million small, rooted, measurable actions that grow into forests.

SeedSpark is the open soil.

---

**Start your first Seed. The movement begins where you are.**
