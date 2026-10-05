Full-resolution files: https://github.com/cherryland32/dlblp-creatives/tree/main/outputs/2026-10-05

# Weekly ad batch — 2026-10-05

10 Meta creatives for "De la Bobiță la Pepene" — Setul 2 în 1, **419 lei** (redus de la **548 lei**),
**Economisești 129 lei**, **Livrare gratuită**. 9 remixes of the proven recipe pool + 1 new concept.
Statics are 1080x1350 JPEG q92-94. Produced with pure PIL from repo assets (no Higgsfield generation
was used this week — the repo's pre-approved generated scenes, `base_giftbox.png`, `base_delivery.png`,
`bump.png`, `cutout_giftbox.png` and `page_05_week8.jpg`, already satisfy the "real covers, no AI
redesign" rule, so no new Higgsfield calls were needed).

| # | File | Recipe / angle | Notes |
|---|------|-----------------|-------|
| 01 | `01_email_inbox.jpg` | Fake-UI: e-mail inbox | New fake-UI format (inbox list, not chat/notes/lockscreen); price drop reveal in the unread brand e-mail. |
| 02 | `02_bump_poster.jpg` | Generated/real photo + typographic overlay | `bump.png` lifestyle photo, present-moment/future-memory hook, dark contrast panel for price legibility. |
| 03 | `03_phone_paper_poster.jpg` | Typographic poster | Cream/gold frame, phone-vs-paper claim, pill badges for savings + free shipping. |
| 04 | `04_ie_invitation.jpg` | Folk/Romanian aesthetic | "Ie"-motif diamond border framing an invitation-style layout; new folk treatment (not cross-stitch poster or recipe card). |
| 05 | `05_reels_cutout.jpg` | Split-depth IG-frame static | Reels UI chrome (progress bar, like/comment/share, caption) with `cutout_giftbox.png` breaking out of frame. |
| 06 | `06_ig_stories.mp4` | Screen-life VIDEO | 1080x1920, 30fps, 12.1s, libx264 crf18 +faststart, `music.mp3` bed with fade in/out. 3-scene auto-advancing IG Stories sequence (progress bar segments): phone-vs-paper hook -> price reveal on giftbox photo -> brand/CTA close. |
| 07 | `07_claim_card.jpg` | Emotional claim card | New claim ("Peste 20 de ani, copilul tău te va întreba cum a fost.") + the approved Ebbinghaus line, cream card. |
| 08 | `08_gift_tag.jpg` | Gift angle (soacra/sora) | Handwritten gift-tag mockup ("Pentru: Ana / De la: soacra ta") pinned to `base_giftbox.png`. |
| 09 | `09_letter_future.jpg` | Generations/legacy angle | Handwritten letter-to-the-future-child overlay on `page_05_week8.jpg` journal spread. |
| 10 | `10_storage_settings.jpg` | **NEW CONCEPT** | iPhone Settings > Stocare fake-UI: phone storage nearly full with photos, contrasted with "68 de pagini, memoria lor nu se umple niciodată." Not used in any prior batch. |

`contact_sheet.jpg` — all 10 creatives (video represented by a representative frame) for review.

## Self-review checklist
- Legibility at thumbnail size: checked via contact sheet, all headlines/prices readable.
- Margins: no text clipped against frame edges (fixed two overflow bugs found in self-review: bump
  poster price contrast, letter-to-future-child panel overflow).
- Prices: 419 lei / 548 lei crossed / Economisești 129 lei present on all 10 creatives.
- Livrare gratuită: present on all 10 creatives.
- Diacritics: verified ăâîșț render correctly with EBGaramond-Bold/Italic and Inter-Regular (no Cormorant used).
- No tofu: no emoji glyphs used; hearts/icons are hand-drawn vector shapes.
- No em dash: verified via grep across all ad-copy source, only "-" used.
- Covers accurate: only repo photos/pre-approved generated assets used, no AI redesign of covers.
- Claims: only the verified claims list + the approved Ebbinghaus line; no invented statistics or testimonials.

## Flags
- Higgsfield was not called this week (not needed — see note above); no credits were consumed.
- Video audio: `assets/music.mp3` trimmed to 12.13s with 0.5s fade-in / 0.6s fade-out.
